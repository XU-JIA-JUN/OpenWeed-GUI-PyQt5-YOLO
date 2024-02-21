# OpenWeed-GUI
Welcome to the **OpenWeedGUI**! An Open-Source Graphical Tool for Weed Imaging and YOLO-based Weed Detection. We hope you can use it for many great applications and participate in the project. Don't be shy to ask questions, and provide feedback.
# Introduction
**OpenWeedGUI** is a graphical user interface (GUI) designed to bridge the gap between machine vision and artificial intelligence technologies for real-time weed detection in sustainable crop production. Built on the PyQt framework and leveraging open-source libraries, OpenWeedGUI simplifies the process of image acquisition and deployment of YOLO (You Only Look Once) models, making it a suitable tool for researchers, developers, and practitioners in the field of precision agriculture.

![GUI Layout](./Pictures/GUILayout.jpg "GUI Layout")

# Features
- Support image/video/camera stream (Vimba Camera) as input
- Temporarily change the model
- Change detection confidence
- Camera parameter setting
- Play/pause/stop
- Visualize detection results
- Result statistics
- Save detected image/JSON automatically

# Installing OpenWeedGUI:

## Environment Requirements:
OpenWeedGUI was developed using Linux but it also can be operated in Windows. It should be noted that some optional features cannot be used when run on Linux. OpenWeedGUI is based on Python and requires `python >= 3.8` to run, pay attention to OpenWeedGUI can only support Vimba Camera for now, if you use a customed camera, you should change the input source. 

## Install
To download this project, you can use the `git clone` command as follows:

'''bash
https://github.com/XU-JIA-JUN/OpenWeed-GUI.git

