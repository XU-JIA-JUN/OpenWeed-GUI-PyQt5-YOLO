import sys
import cv2
import torch
sys.path.append("/media/agfoodsensinglab/512ssd/WeedGUIProject/YOLOR")

from utilsr.general import  non_max_suppression

from utilsr.torch_utils import select_device, load_classifier, time_synchronized

from modelsr.models import Darknet
#from utilsr.datasets import *
#from utilsr.general import *
import numpy as np

def letterbox(img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, auto_size=32):
    # Resize image to a 32-pixel-multiple rectangle https://github.com/ultralytics/yolov3/issues/232
    shape = img.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, auto_size), np.mod(dh, auto_size)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)


def yolorDetector(img0,model,img_size,conf_thres):

    device = select_device("0")
    half = device.type != 'cpu'

    #img_size = 640
    auto_size = 32
    img = letterbox(img0, new_shape=img_size, auto_size=auto_size)[0]

    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    iou_thres = 0.5
    classes = None
    agnostic_nms = False

    pred = model(img)[0]
    pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes, agnostic=agnostic_nms)

    return pred

def LoadYolorModel(cfg,weights,imgsz):
    device = select_device("0")
    half = device.type != 'cpu'

    model = Darknet(cfg, imgsz).cuda()
    # model.load_state_dict(torch.load(weights, map_location={'0':'GPU'})['model'])
    model.load_state_dict(torch.load(weights, map_location=device)['model'])
    model.to(device).eval()
    model.half()

    if half:
        model.half()  # to FP16

    return model

def LoadYolos4Model(cfg,weights,imgsz):
    device = select_device("0")
    half = device.type != 'cpu'

    model = Darknet(cfg, imgsz).cuda()
    # model.load_state_dict(torch.load(weights, map_location={'0':'GPU'})['model'])
    model.load_state_dict(torch.load(weights, map_location=device)['model'])
    model.to(device).eval()
    model.half()

    if half:
        model.half()  # to FP16

    return model