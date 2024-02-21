import sys
from PyQt5.QtWidgets import *
import cv2
from vimba import *
from  PyQt5.QtGui import *
from  PyQt5.QtCore import *
#from  PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
#from  PyQt5.QtMultimediaWidgets import QVideoWidget
import torch
import json
import os
import threading
from typing import Optional
from time import time, sleep
import numpy as np
import sys
from queue import SimpleQueue
from itertools import count
from MyWeed import Ui_OpenWeedGUI
import datetime
from ultralytics import YOLO
from loguru import logger
from yolox.data.data_augment import ValTransform
from yolox.data.datasets import COCO_CLASSES
from yolox.exp import get_exp
from yolox.utils import fuse_model, get_model_info, postprocess, vis
from yoloxDetectClass import yoloxPredictor
from yolorDetector1 import yolorDetector,LoadYolorModel
import pycuda.autoinit
import pycuda.driver as cuda
import tensorrt as trt
from MyYoLov5TRT import YoLov5TRT,inferThread,warmUpThread
import ctypes
from drawing_label import DrawingLabel
from roi_window import ROI_Window
from speed_monitor import SpeedMonitor

import serial
need_start_relay = True
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        global need_start_relay
        with open('/home/agfoodsensinglab/Desktop/Arduino/signal.txt', 'w') as f:
            if need_start_relay:
                f.write('Y')
            else:
                f.write('N')
        need_start_relay = not need_start_relay
        self.finished.emit()

class ImageAdjustmentUI(QWidget):
    sliderValuesChanged = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        self.saturation_slider = QSlider()
        self.saturation_slider.setOrientation(1)
        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(200)
        self.saturation_slider.setValue(100)
        layout.addWidget(QLabel("Saturation"))
        layout.addWidget(self.saturation_slider)

        self.saturation_label = QLabel("Saturation: 1.00")
        layout.addWidget(self.saturation_label)

        self.hue_slider = QSlider()
        self.hue_slider.setOrientation(1)
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(360)
        layout.addWidget(QLabel("Hue"))
        layout.addWidget(self.hue_slider)

        self.hue_label = QLabel("Hue: 0")
        layout.addWidget(self.hue_label)

        self.value_slider = QSlider()
        self.value_slider.setOrientation(1)
        self.value_slider.setMinimum(0)
        self.value_slider.setMaximum(200)
        self.value_slider.setValue(100)
        layout.addWidget(QLabel("Value"))
        layout.addWidget(self.value_slider)

        self.value_label = QLabel("Value: 1.00")
        layout.addWidget(self.value_label)

        self.setLayout(layout)

        self.saturation_slider.valueChanged.connect(self.update_adjustments)
        self.hue_slider.valueChanged.connect(self.update_adjustments)
        self.value_slider.valueChanged.connect(self.update_adjustments)

    def update_adjustments(self):
        saturation_factor = self.saturation_slider.value() / 100.0
        hue_shift = self.hue_slider.value()
        value_factor = self.value_slider.value() / 100.0

        self.saturation_label.setText(f"Saturation: {saturation_factor:.2f}")
        self.hue_label.setText(f"Hue: {hue_shift}")
        self.value_label.setText(f"Value: {value_factor:.2f}")

        self.sliderValuesChanged.emit((saturation_factor, hue_shift, value_factor))


class MainWindow(QMainWindow, Ui_OpenWeedGUI):
    ExpClicked=pyqtSignal(str)
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkCam()
        self.timer_camera = QTimer() # inital some
        self.timer_video  = QTimer()
        self.timer_video.timeout.connect(self.show_video)
        self.queue = SimpleQueue()  # queue for video frames
        self.timer_camera.timeout.connect(self.show_camera)
        self.OpenCamButton.clicked.connect(self.button_open_camera_clicked)
        self.model = torch.hub.load("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5", 'custom', path="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/bestS.pt" , source='local', force_reload=True)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.YoloVersion="yolov5"
        self.comboBox_2.currentIndexChanged.connect(self.comboYoloIndexChanged)
        self.comboBox_pt.currentIndexChanged.connect(self.ModelChange)
        self.OpenVideoButton.clicked.connect(self.Video_path_dialog)
        self.fileButton.clicked.connect(self.show_img)
        self.runVideoButton.clicked.connect(self.playVideoWithThreading)
        self.stopVideoButton.clicked.connect(self.stopVideo)
        self.clearButton.clicked.connect(self.clearFrame)
        self.camMButton.clicked.connect(self.show_adjustment_window)
        self.ReControl.clicked.connect(self.relayControl)
        self.speed_monitor = SpeedMonitor()
        #self.speed_monitor.start_worker()
        self.mapped_rect = QRect()
        self.vclose=True
        self.videoPath=[]
        self.pause_flag=False
        self.next_capture_time=time()+self.save_num.value()
        self.names=self.model.names
        self.save_check.clicked.connect(self.createSavePath)
        self.ImgPath=[]
        self.JsonPath=[]
        self.Inum=1
        self.adjusted_image=None
        self.saturation_factor=1.00
        self.hue_shift=0
        self.value_factor=1.00
        self.group=QButtonGroup(self)
        self.group.setExclusive(True)
        self.Exposure_offBox.toggled.connect(self.setExp)
        self.Exposure_continueBox.toggled.connect(self.setExp)
        self.group.addButton(self.Exposure_offBox)
        self.group.addButton(self.Exposure_onceBox)
        self.group.addButton(self.Exposure_continueBox)
        self.actionSet_ROI.triggered.connect(self.openROIWindow)
        self.ExpState="Continous"
        self.makeResize = False
        self.scaled_size = (669, 717)
        self.original_size = (2056, 2464)
        self.yoloxExpL=get_exp("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOX-main/exps/example/custom/custom/yolox_l_weed_2021.py", None)
        self.yolov8sClass=["Lambsquarters", "Unknown", "Ragweed", "Purslane", "Pigweed", "Smartweed"]
        self.newClasses = ["Waterhemp", "MorningGlory", "Purslane", "SpottedSpurge", "Carpetweed", "Ragweed",
                   "Eclipta", "PricklySida", "PalmerAmaranth", "Sicklepod", "Goosegrass", "CutleafGroundcherry",
                   "Lambsquarters", "Pigweed", "Unknown", "Smartweed", "HophornbeamCopperleaf", "Cocklebur",
                   "Nutsedge", "VirginiaButtonweed", "PurpleAmmania", "GroundIvy", "Swinecress"]
        self.current_model = self.comboBox_pt.currentText()
    def show_adjustment_window(self):
        self.adjustment_window = QMainWindow(self)
        self.adjustment_ui = ImageAdjustmentUI(self.adjustment_window)
        self.adjustment_ui.sliderValuesChanged.connect(self.adjust_image)
        self.adjustment_window.setCentralWidget(self.adjustment_ui)
        self.adjustment_window.setWindowTitle("Image Adjustment")
        self.adjustment_window.setGeometry(200, 200, 300, 200)
        self.adjustment_window.show()

    def openROIWindow(self):
        frameSize=(self.label_pic.width(), self.label_pic.height())
        ROIWindow = ROI_Window(self)
        ROIWindow.size_signal.connect(self.resizeFrame)
        ROIWindow.show()
    def resizeFrame(self,size_data):
        print(size_data)
        self.makeResize=True
        if size_data[0] == "reset":
            self.makeResize=False
        else:
            self.makeResize = True
        #self.label_pic.resize(size_data[2],size_data[3])
            scale_factor_x=2464/self.label_pic.width()
            scale_factor_y=2056/self.label_pic.height()

            self.original_x = int(size_data[0] * scale_factor_x)
            self.original_y = int(size_data[1] * scale_factor_y)
            self.original_width = int(size_data[2] * scale_factor_x)
            self.original_height = int(size_data[3] * scale_factor_y)

            scale_factor_x = self.original_size[0] / self.scaled_size[0]
            scale_factor_y = self.original_size[1] / self.scaled_size[1]

            x,y,width,height=size_data[0],size_data[1],size_data[2],size_data[3]

            self.mapped_rect = QRect(
                int(x ),
                int(y ),
                int(width ),
                int(height ),
            )

        #x, y = map(int, position_text.split(","))


    def setExp(self):
        if self.Exposure_offBox.isChecked():
            print("off")
            self.ExpState="Off"
        elif self.Exposure_onceBox.isChecked():
            self.ExpState="Once"
        elif self.Exposure_continueBox.isChecked():
            print("continue")
            self.ExpState="Continuous"
        else:
            pass

        with Vimba.get_instance() as vimba:
            with vimba.get_all_cameras()[0] as camera:
                camera.ExposureAuto.set(self.ExpState)
                #width_feature = camera.getFeatureByName('Width')
                #print(width_feature)

    def comboYoloIndexChanged(self):
        self.YoloVersion = self.comboBox_2.currentText()
        self.updateComboBox_ptOptions()

    def updateComboBox_ptOptions(self):
        self.comboBox_pt.clear()
        if self.YoloVersion == "yolov5":
            self.comboBox_pt.addItems(["bestn.pt",'bestS.pt', 'bestL.pt', 'bestM.pt',"bestX.pt","bestS.engine","bestM.engine"])
            #self.model = torch.hub.load("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5", 'custom',
                                        #path="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/" + 'bestS.pt',
                                        #source='local')
        elif self.YoloVersion == "yolov3":
            self.comboBox_pt.addItems(['best3-tiny.pt', 'best3.pt', 'bestSPP.pt'])
            #self.model = torch.hub.load("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv3", 'custom',
                                        #path="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/" + "best3-tiny.pt",
                                        #source='local')
        elif self.YoloVersion == "yolov8":
            self.comboBox_pt.addItems(["yolov8.0.58.pt","yolov8bestS.pt","yolov8bestS1.pt","bestv8S.pt"])
            #self.modelv8=YOLO("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/yolov8.0.58.pt")
        elif self.YoloVersion == "yolox":
            self.comboBox_pt.addItems(["best_ckpt.pth","best_ckpt1.pth"])
        elif self.YoloVersion=="yolor":
            self.comboBox_pt.addItems(["bestR-P6.pt","bestR-CSP.pt","bestR-CSP-X.pt"])
        elif self.YoloVersion=="yolov4":
            self.comboBox_pt.addItems(["best_yolov4.pt", "best_yolov4_pacsp.pt", "best_yolov4_pacsp-s.pt","best_yolov4_pacsp-x.pt"])
        elif self.YoloVersion=="Scaled-yolov4":
            self.comboBox_pt.addItems(["best_yolov4-P5.pt", "best_yolov4-P6.pt", "best_yolov4-P7"])


    def createSavePath(self):
        if self.save_check.isChecked():
            nowTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
            pathS = os.getcwd() + '/DetectedImages/' + nowTime
            pathJ = os.getcwd() + '/json/' + nowTime
            pathO = os.getcwd() + '/OriginalImages/' + nowTime
            if not os.path.exists(pathS) and not os.path.exists(pathJ) and not os.path.exists(pathO):
                os.makedirs(pathS)
                os.makedirs(pathJ)
                os.makedirs(pathO)
                print("path maked")
                self.ImgPath=pathS
                self.JsonPath=pathJ
                self.OriPath=pathO
                self.Inum=1

    def Video_path_dialog(self):

        videoPath, _ = QFileDialog.getOpenFileName(self, "open video file",
                                                   ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        self.videoPath=videoPath
        #playVideoWithThreading()
    def stopVideo(self):
        self.vclose=False

    def relayControl(self):
        print('relayControl')
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def ModelChange(self):
        self.current_model = self.comboBox_pt.currentText()
        self.current_version=self.comboBox_2.currentText()

        if self.current_version=="yolov5" and len(self.current_model)>1:
            if "engine" in self.current_model:
                self.modelv5E=YoLov5TRT("/media/agfoodsensinglab/512ssd/WeedGUIProject/Models/YOLOV5sE/"+self.current_model)
            else:
                self.model = torch.hub.load("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5", 'custom', path="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/"+self.current_model, source='local',force_reload=True)
        elif self.current_version=="yolov3" and len(self.current_model)>1:
            self.model = torch.hub.load("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5", 'custom', path="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/" + self.current_model,source='local',force_reload=True)
        elif self.current_version=="yolov8" and len(self.current_model)>1:
            self.modelv8=YOLO("/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5/"+self.current_model)
        elif self.current_version=="yolox" and len(self.current_model)>1:
            if self.current_model=="best_ckpt1.pth":
                self.yoloxExpL.test_size = (800, 800)
            else:
                self.yoloxExpL.test_size=(640,640)
                self.modelx=self.yoloxExpL.get_model()
                self.modelx.cuda()
                self.modelx.eval()
                ckpt_file="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOX-main/"+self.current_model
                ckpt=torch.load(ckpt_file,map_location="cpu")
                self.modelx.load_state_dict(ckpt["model"])
                self.yoloxPredictor=yoloxPredictor(self.modelx,self.yoloxExpL,COCO_CLASSES,device="gpu")
        elif self.current_version=="yolor" and len(self.current_model)>1:
            yolor_cfg_key={"bestR-P6.pt":"yolor_p6.cfg","best-CSP.pt":"yolor_csp.cfg","best-CSP-X.pt":"yolor_csp_x.cfg"}
            ROOT = "/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOR"
            cfg = ROOT + "/cfg/yolor_p6.cfg"
            weights = "/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOR/bestR-p6.pt"
            imgsz=(640,640)
            pathv5="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv5"
            self.modelr = LoadYolorModel(cfg, weights, imgsz)
        elif self.current_version == "yolov4" and len(self.current_model) > 1:
            #yolor_cfg_key = {"bestR-P6.pt": "yolor_p6.cfg", "best-CSP.pt": "yolor_csp.cfg",
                             #"best-CSP-X.pt": "yolor_csp_x.cfg"}
            ROOT = "/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv4"
            cfg = ROOT + "/cfg/yolov4.cfg"
            weights = "/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv4/best_yolov4.pt"
            imgsz = (640, 640)
            self.modelv4 = LoadYolorModel(cfg, weights, imgsz)

        print("model is added")
        self.statusBar().showMessage("model is added")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def update_current_speed(self):
        cur_speed = 0
        cur_speed = self.speed_monitor.caculate_speed()

        self.label_speed.setText("Current Speed: {}".format(cur_speed))

    def show_video(self):
        if not self.queue.empty() and not self.detect_check.isChecked():
           c_frame=self.queue.get()
           #cv2.putText(c_frame, f'Time: {int(time())}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 6)
           label_width = self.label_pic.width()
           label_height = self.label_pic.height()
           c_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
           temp_imgSrc = QImage(c_frame, c_frame.shape[1], c_frame.shape[0], c_frame.shape[1] * 3,
                                QImage.Format_RGB888)
           pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
           self.label_pic.setPixmap(pixmap_imgSrc)
        elif not self.queue.empty() and  self.detect_check.isChecked():
            new_size = (640,640)
            c_frame = self.queue.get()
            start_time=time()
            c_frame=cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
            resize_frame=cv2.resize(c_frame,new_size)
            results=self.new_score_frame(resize_frame)
            final_frame=self.plot_boxes(results,resize_frame)
            end_time=time()
            fps=1/np.round(end_time-start_time,2)
            cv2.putText(final_frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            label_width = self.label_pic.width()
            label_height = self.label_pic.height()
            temp_imgSrc = QImage(final_frame, final_frame.shape[1], final_frame.shape[0], final_frame.shape[1] * 3,
                                 QImage.Format_RGB888)
            pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
            self.label_pic.setPixmap(pixmap_imgSrc)
            #print(JsonPath,results,Jnum)
            #print(c_frame.shape)
            if int(time() % self.save_num.value()) == 0 and self.save_check.isChecked():  # some  variable parameters
                Img_Name = str(self.Inum) + ".png"
                cv2.imwrite(".../DetectedImages/"+Img_Name, final_frame)
                JsonPath=".../json"

                self.save_json(results, JsonPath, self.Inum)
                print(self.Inum)-++++++++++++++.3

                self.Inum+=1

    def playVideoWithThreading(self):
        if self.timer_video.isActive() == False:
            self.statusBar().showMessage("is streaming")
            threading.Thread(target=self.video_streaming, args=(self.queue,), daemon=True).start()
            self.timer_video.start(1000)
            print("video start")
        else:
            self.vclose = False
            self.timer_video.stop()
            # is_streaming=False
            # cam.stop_streaming()
            self.label_pic.clear()
            #self.OpenCamButton.setText("Open Camera")

    def video_streaming(self,queue):
        global is_streaming
        is_streaming = True
        cap = cv2.VideoCapture(self.videoPath)
        frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.videoSlider.setMaximum(int(frames/24))
        if not cap.isOpened():
            print("Cannot open Video File")
            exit()
        print("video started")
        while self.vclose:
                    # print(is_streaming)
            ret, frame = cap.read()
            if not ret:
                if frame is None:
                    print("The video has end.")
                else:
                    print("Read video error!")
                    break
            queue.put(frame)
        #self.timer_video.stop()
        #self.label_pic.clear()
        print("video stopped")


    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:
            threading.Thread(target=self.camera_streaming, args=(self.queue,), daemon=True).start()
            # threading.Thread(target=saveImage_Runthread, daemon=True).start()
            self.timer_camera.start(25)
            self.OpenCamButton.setText('Close Camera')
        else:
            global is_streaming
            is_streaming = False
            self.timer_camera.stop()
            # is_streaming=False
            # cam.stop_streaming()
            self.label_pic.clear()
            self.OpenCamButton.setText("Open Camera")

    def camera_streaming(self,queue):
        global is_streaming
        is_streaming = True
        print("streaming started")
        self.statusBar().showMessage("streaming started")
        with Vimba.get_instance() as vimba:
            with vimba.get_all_cameras()[0] as camera:
                while is_streaming:
                    # print(is_streaming)
                    #f=camera.AcquireSingleImage()
                    frame = camera.get_frame()
                    # frame = frame.as_opencv_image()
                    # im = Image.fromarray(frame)
                    # img = ImageTk.PhotoImage(im)
                    queue.put(frame)  # put the capture image into queue
        print("streaming stopped")
        self.statusBar().showMessage("streaming stopped")

    def new_score_frame(self,frame):
        global model
        global device

        if self.YoloVersion=="yolov8":
            results=self.modelv8.predict(frame, show=False,save=False,save_txt=False,save_conf=False)
        elif self.YoloVersion=="yolox":
            results,_=self.yoloxPredictor.inference(frame)
        elif self.YoloVersion=="yolor":
            results = yolorDetector(frame, self.modelr, (640,640), 0.01)
        elif self.YoloVersion=="yolov4":
            results = yolorDetector(frame, self.modelv4, (640,640), 0.01)
        elif self.current_model=="bestS.engine":
            results = self.modelv5E.infer(frame)

        else:
            self.model.to(self.device)
            frame = [frame]
            results = self.model(frame)
        # results.save()
        return results
    def clearFrame(self):
        if "engine" in self.current_model:
            self.modelv5E.destroy()
            self.statusBar().showMessage("Release engine")

    def class_to_label(self,x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """
        global model
        classes = self.model.names

        if self.current_model=="yolov8bestS.pt":
            classes=["Lambsquarters", "Unknown", "Ragweed", "Purslane", "Pigweed", "Smartweed"]
        elif self.current_model=="yolov8bestS1.pt" or self.current_model=="best_ckpt1.pt":
            classes = ["Waterhemp", "MorningGlory", "Purslane", "SpottedSpurge", "Carpetweed", "Ragweed",
                       "Eclipta", "PricklySida", "PalmerAmaranth", "Sicklepod", "Goosegrass", "CutleafGroundcherry",
                       "Lambsquarters", "Pigweed", "Unknown", "Smartweed", "HophornbeamCopperleaf", "Cocklebur",
                       "Nutsedge", "VirginiaButtonweed", "PurpleAmmania", "GroundIvy", "Swinecress"]
        elif self.current_model=="bestv8S":
            classes=["Waterhemp", "MorningGlory", "Purslane", "SpottedSpurge", "Carpetweed", "Ragweed",
                       "Eclipta", "PricklySida", "PalmerAmaranth", "Sicklepod", "Goosegrass", "CutleafGroundcherry",
                       "Lambsquarters", "Pigweed", "Unknown", "Smartweed", "HophornbeamCopperleaf", "Cocklebur",
                       "Nutsedge", "VirginiaButtonweed", "PurpleAmmania", "GroundIvy", "Swinecress","15",
                     "21","10","11","15"]
        return classes[int(x)]

    def save_json(self,results, JsonPath, Jnum):
        #parsed = json.loads(results.pandas().xyxy[0].to_json(orient="records"))
        #parsed = json.loads(results.xyxy[0].to_json(orient="records"))
        f = open(JsonPath + "data%s.json" % Jnum, 'w')
        #json.dump(parsed, f)
        f.close()

    def plot_boxes(self,results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        if self.YoloVersion=="yolov8":
            labels=results[0].boxes.cls
            conf=results[0].boxes.conf
            cord=results[0].boxes.xyxyn
            conf=torch.unsqueeze(conf,dim=1)
            cord=torch.cat((cord,conf),axis=1)
        elif self.YoloVersion=="yolox":
            if self.current_model == "best_ckpt1.pth":
                size_ratio = 800.0/640
            else:
                size_ratio = 1.0
            results=results[0]
            if results is None:
                return frame
            labels=results[:,6]
            conf=results[:,4]*results[:,5]
            conf = torch.unsqueeze(conf, dim=1)
            cord=results[:,0:4]*size_ratio
            cord = torch.cat((cord, conf), axis=1)
        elif self.YoloVersion=="yolor" or self.YoloVersion=="yolov4":
            results=results[0]
            labels=results[:,5]
            conf=results[:,4]
            conf = torch.unsqueeze(conf, dim=1)
            cord=results[:,0:4]
            cord = torch.cat((cord, conf), axis=1)
        elif self.current_model=="bestS.engine":

            cord = np.concatenate((results[0], results[1].reshape(-1, 1)), axis=1)
            labels=results[2]
        else:
            labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= self.confSpinBox.value():

                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                if self.YoloVersion=="yolox" or self.current_model=="bestS.engine":
                    x1,y1,x2,y2=int(row[0]),int(row[1]),int(row[2]),int(row[3])
                elif self.YoloVersion=="yolor":
                    x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                bgr = (255, 0, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 3)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 3)
        self.show_statistic(results)
        return frame

    def plot_oriboxes(self,results, c_frame):
        if self.YoloVersion=="yolov8":
            labels=results[0].boxes.cls
            conf=results[0].boxes.conf
            cord=results[0].boxes.xyxyn
            conf=torch.unsqueeze(conf,dim=1)
            cord=torch.cat((cord,conf),axis=1)
        elif self.YoloVersion=="yolox":
            if self.current_model == "best_ckpt1.pth":
                size_ratio = 800.0 / 640
            else:
                size_ratio = 1.0
            results=results[0]
            if results is None:
                return c_frame
            labels=results[:,6]
            conf=results[:,4]*results[:,5]
            conf = torch.unsqueeze(conf, dim=1)
            cord=results[:,0:4]*size_ratio
            cord = torch.cat((cord, conf), axis=1)
        elif self.YoloVersion=="yolor" or self.YoloVersion=="yolov4":
            results=results[0]
            labels=results[:,5]
            conf=results[:,4]
            conf = torch.unsqueeze(conf, dim=1)
            cord=results[:,0:4]
            cord = torch.cat((cord, conf), axis=1)
        elif self.current_model == "bestS.engine":

            cord = np.concatenate((results[0], results[1].reshape(-1, 1)), axis=1)
            labels = results[2]
        else:
            labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

        n = len(labels)
        x_shape, y_shape = c_frame.shape[1], c_frame.shape[0]
        scale_x = x_shape/ 717
        scale_y = y_shape / 669
        for i in range(n):
            row = cord[i]
            if row[4] >= self.confSpinBox.value():

                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                if self.YoloVersion=="yolox" or self.current_model=="bestS,engine":
                    x1,y1,x2,y2=int(row[0]),int(row[1]),int(row[2]),int(row[3])
                    x1,y1,x2,y2=x1*scale_x,y1*scale_y,x2*scale_x,y2*scale_y
                elif self.YoloVersion=="yolor":
                    x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                    x1, y1, x2, y2 = x1 * scale_x, y1 * scale_y, x2 * scale_x, y2 * scale_y
                bgr = (255, 0, 0)
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                cv2.rectangle(c_frame, (x1, y1), (x2, y2), bgr, 3)
                cv2.putText(c_frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 3)

        return c_frame


    def show_statistic(self, results):
        if self.YoloVersion=="yolov8":
            labels=results[0].boxes.cls
            conf=results[0].boxes.conf
            cord=results[0].boxes.xyxyn
            conf=torch.unsqueeze(conf,dim=1)
            cord=torch.cat((cord,conf),axis=1)
        elif self.YoloVersion=="yolox":
            results=results
            labels = results[:, 6]
            conf = results[:, 4] * results[:, 5]
            conf = torch.unsqueeze(conf, dim=1)
            cord = results[:, 0:4]
            cord = torch.cat((cord, conf), axis=1)
        elif self.YoloVersion=="yolor" or self.YoloVersion=="yolov4" :
            results=results
            labels=results[:,5]
            conf=results[:,4]
            conf = torch.unsqueeze(conf, dim=1)
            cord=results[:,0:4]
            cord = torch.cat((cord, conf), axis=1)
        elif self.current_model == "bestS.engine":

            cord = np.concatenate((results[0], results[1].reshape(-1, 1)), axis=1)
            labels = results[2]
        else:
            labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        if self.current_model=="yolov8bestS.pt":
            statistic_dic = {name: 0 for name in self.yolov8sClass}
        elif self.current_model=="yolov8bestS1.pt" or self.current_model=="best_ckpt1.pth":
            statistic_dic = {name: 0 for name in self.newClasses}
        else:
            statistic_dic = {name: 0 for name in self.names}

        n = len(labels)
        for i in range(n):
            row = cord[i]
            if row[4] >= self.confSpinBox.value():

                statistic_dic[self.class_to_label(labels[i])] += 1
        try:
            self.resultWidget.clear()
            statistic_dic = sorted(statistic_dic.items(), key=lambda x: x[1], reverse=True)
            statistic_dic = [i for i in statistic_dic if i[1] > 0]
            results = [' ' + i[0]+ '：' + str(i[1]) for i in statistic_dic]
            self.resultWidget.addItems(results)
        except Exception as e:
            print(repr(e))

    def resizeCheck(self,c_frame):

        if self.makeResize:
            mapped_rect = self.mapped_rect
            scale_factor_x = self.original_size[0] / self.scaled_size[0]
            scale_factor_y = self.original_size[1] / self.scaled_size[1]
            original_rect = QRect(
                int(mapped_rect.x() * scale_factor_x),
                int(mapped_rect.y() * scale_factor_y),
                int(mapped_rect.width() * scale_factor_x),
                int(mapped_rect.height() * scale_factor_y),
            )
            c_frame = c_frame[original_rect.y():original_rect.y() + original_rect.height(),
                      original_rect.x():original_rect.x() + original_rect.width()]
        return c_frame


    def show_camera(self):
        global frame_num
        global Inum
        global Jnum

        self.update_current_speed()

        if not self.queue.empty() and not self.detect_check.isChecked():
           frame=self.queue.get()
           c_frame=frame.as_opencv_image()
           c_frame=self.resizeCheck(c_frame)
               #print(c_frame.shape)
          # cv2.putText(c_frame, f'Time: {int(time())}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 6)
           label_width = self.label_pic.width()
           label_height = self.label_pic.height()
           c_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
           temp_imgSrc = QImage(c_frame, c_frame.shape[1], c_frame.shape[0], c_frame.shape[1] * 3,
                                QImage.Format_RGB888)
           pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
           self.label_pic.setPixmap(pixmap_imgSrc)
           #if self.makeResize:
               #self.label_pic.setPixmap(pixmap_imgSrc.copy(self.mapped_rect))

           #else:
            #self.label_pic.setPixmap(pixmap_imgSrc)
           if int(time() % self.save_num.value()) == 0 and self.save_check.isChecked():  # some  variable parameters
               # current_time = time()
               # print(current_time)
               # print(1)
               # if self.next_capture_time>= current_time and self.save_check.isChecked():
               Img_Name = "/" + str(self.Inum) + ".jpg"
               cv2.imwrite(self.ImgPath + Img_Name, c_frame)
               #self.save_json(results, self.JsonPath + "/", self.Inum)
               self.statusBar().showMessage("Saving file:" + Img_Name)
               self.Inum += 1

        elif not self.queue.empty() and  self.detect_check.isChecked():
            frame = self.queue.get()
            c_frame = frame.as_opencv_image()
            c_frame = self.resizeCheck(c_frame)


            start_time=time()
            c_framer=cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
            if self.current_model=="yolov8bestS.pt":
                resize_frame = cv2.resize(c_framer, (800, 800))
            elif self.current_model=="best_ckpt1.pth":
                resize_frame = cv2.resize(c_framer, (800, 800))
            elif self.current_model=="yolov8bestS1.pt":
                #resize_frame = cv2.resize(c_framer, (1500, 1500))
                resize_frame = cv2.resize(c_framer, (800, 800))
            else:
                resize_frame=cv2.resize(c_framer,(717,669))
            cheight, cwidth, _ = c_frame.shape
            results=self.new_score_frame(resize_frame)
            final_frame=self.plot_boxes(results,resize_frame)
            final_oriframe=self.plot_oriboxes(results, c_framer)
            end_time=time()
            fps=1/np.round(end_time-start_time,2)
            cv2.putText(final_frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            label_width = self.label_pic.width()
            label_height = self.label_pic.height()
            temp_imgSrc = QImage(final_frame, final_frame.shape[1], final_frame.shape[0], final_frame.shape[1] * 3,
                                 QImage.Format_RGB888)
            pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
            self.label_pic.setPixmap(pixmap_imgSrc)
            if int(time()% self.save_num.value()) == 0 and self.save_check.isChecked():  # some  variable parameters

                Img_Name = "/"+str(self.Inum) + ".jpg"
                #cv2.imwrite(self.ImgPath+Img_Name, final_frame)
                #restored_image = cv2.resize(resized_image, original_size)
                cv2.imwrite(self.ImgPath+Img_Name, cv2.cvtColor(final_oriframe, cv2.COLOR_RGB2BGR))
                #cv2.imwrite (self.OriPath+Img_Name, cv2.resize(c_frame,(640,640))) #test
                cv2.imwrite(self.OriPath + Img_Name, c_frame)
                self.save_json(results, self.JsonPath+"/", self.Inum)
                self.statusBar().showMessage("Saving file:"+Img_Name)
                self.Inum+=1
                #self.next_capture_time = current_time + self.save_num.value()
                #print(self.next_capture_time)
            #print(self.save_num.value())
            #print(Inum)
    def adjust_image(self,slider_values):
        self.saturation_factor, self.hue_shift, self.value_factor = slider_values

    def adjust_image1(self,frame):
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * self.saturation_factor, 0, 255)
        hsv_image[:, :, 0] = (hsv_image[:, :, 0] + self.hue_shift) % 360
        hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * self.value_factor, 0, 255)
        adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        return adjusted_image

        #self.display_image()

    def show_img(self):
        imgPath, imgType = QFileDialog.getOpenFileName(self, "Open image file", "", "*.jpg;;*.png;;All Files(*)")

        if not self.detect_check.isChecked():

           c_frame=cv2.imread(imgPath)
           c_frame = self.resizeCheck(c_frame)
           cframe=c_frame.copy()
           c_frame=self.adjust_image1(cframe)
               #print(c_frame.shape)
          # cv2.putText(c_frame, f'Time: {int(time())}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 6)
           label_width = self.label_pic.width()
           label_height = self.label_pic.height()
           c_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
           temp_imgSrc = QImage(c_frame, c_frame.shape[1], c_frame.shape[0], c_frame.shape[1] * 3,
                                QImage.Format_RGB888)
           pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
           self.label_pic.setPixmap(pixmap_imgSrc)
           #if self.makeResize:
               #self.label_pic.setPixmap(pixmap_imgSrc.copy(self.mapped_rect))

           #else:
            #self.label_pic.setPixmap(pixmap_imgSrc)
           if self.save_check.isChecked():  # some  variable parameters

               Img_Name = "/" + str(self.Inum) + ".jpg"
               cv2.imwrite(self.ImgPath + Img_Name, c_frame)
               #self.save_json(results, self.JsonPath + "/", self.Inum)
               self.statusBar().showMessage("Saving file:" + Img_Name)
               self.Inum += 1

        elif self.detect_check.isChecked():

            c_frame=cv2.imread(imgPath)
            c_frame = self.resizeCheck(c_frame)
            cframe = c_frame.copy()
            c_frame = self.adjust_image1(cframe)

            start_time=time()
            c_framer=cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
            if self.current_model=="yolov8bestS.pt":
                resize_frame = cv2.resize(c_framer, (800, 800))
            elif self.current_model=="best_ckpt1.pth":
                resize_frame = cv2.resize(c_framer, (800, 800))
            elif self.current_model=="yolov8bestS1.pt":
                resize_frame = cv2.resize(c_framer, (1500, 1500))
            else:
                resize_frame=cv2.resize(c_framer,(717,669))
            cheight, cwidth, _ = c_frame.shape
            results=self.new_score_frame(resize_frame)
            final_frame=self.plot_boxes(results,resize_frame)
            final_oriframe=self.plot_oriboxes(results, c_framer)
            end_time=time()
            fps=1/np.round(end_time-start_time,2)
            cv2.putText(final_frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            label_width = self.label_pic.width()
            label_height = self.label_pic.height()
            temp_imgSrc = QImage(final_frame, final_frame.shape[1], final_frame.shape[0], final_frame.shape[1] * 3,
                                 QImage.Format_RGB888)
            pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
            self.label_pic.setPixmap(pixmap_imgSrc)
            if int(time()% self.save_num.value()) == 0 and self.save_check.isChecked():  # some  variable parameters

                Img_Name = "/"+str(self.Inum) + ".jpg"
                #cv2.imwrite(self.ImgPath+Img_Name, final_frame)
                #restored_image = cv2.resize(resized_image, original_size)
                cv2.imwrite(self.ImgPath+Img_Name, cv2.cvtColor(final_oriframe, cv2.COLOR_RGB2BGR))
                #cv2.imwrite (self.OriPath+Img_Name, cv2.resize(c_frame,(640,640))) #test
                cv2.imwrite(self.OriPath + Img_Name, c_frame)
                self.save_json(results, self.JsonPath+"/", self.Inum)
                self.statusBar().showMessage("Saving file:"+Img_Name)
                self.Inum+=1

    def setup_camera(self,cam: Camera):
        with cam:
            # Enable auto exposure time setting if camera supports it
            try:
                cam.ExposureAuto.set('Continuous')

            except (AttributeError, VimbaFeatureError):
                pass

            # Enable white balancing if camera supports it
            try:
                cam.BalanceWhiteAuto.set('Continuous')

            except (AttributeError, VimbaFeatureError):
                pass

            # Try to adjust GeV packet size. This Feature is only available for GigE - Cameras.
            try:
                cam.GVSPAdjustPacketSize.run()

                while not cam.GVSPAdjustPacketSize.is_done():
                    pass

            except (AttributeError, VimbaFeatureError):
                pass

            # Query available, open_cv compatible pixel formats
            # prefer color formats over monochrome formats
            cv_fmts = intersect_pixel_formats(cam.get_pixel_formats(), OPENCV_PIXEL_FORMATS)
            color_fmts = intersect_pixel_formats(cv_fmts, COLOR_PIXEL_FORMATS)

            if color_fmts:
                cam.set_pixel_format(color_fmts[0])

            else:
                mono_fmts = intersect_pixel_formats(cv_fmts, MONO_PIXEL_FORMATS)

                if mono_fmts:
                    cam.set_pixel_format(mono_fmts[0])

                else:
                    self.statusBar().showMessage('Camera does not support a OpenCV compatible format natively. Abort.')
    def checkCam(self):
        with Vimba.get_instance() as vimba:
            cams = vimba.get_all_cameras()
            if not cams:
                self.statusBar().showMessage('No Cameras accessible. Abort.')
            else:
                self.statusBar().showMessage("Camera is accessed")
                self.setup_camera(cams)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())


