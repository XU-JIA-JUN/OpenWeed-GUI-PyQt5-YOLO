from yolorDetector1 import yolorDetector,LoadYolorModel
import cv2

ROOT="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv4"
cfg=ROOT+'/cfg/yolov4.cfg'
imgsz=(640, 640)
weights="/media/agfoodsensinglab/512ssd/WeedGUIProject/DCW-main/YOLOv4/best_yolov4.pt"


model=LoadYolorModel(cfg,weights,imgsz)

path=ROOT+"/example1.jpg"
img0 = cv2.imread(path)
conf_thres=0.25
img_size=640
pred=yolorDetector(img0,model,img_size,conf_thres)
print(pred)