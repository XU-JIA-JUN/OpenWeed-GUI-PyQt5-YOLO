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

```bash
git clone https://github.com/XU-JIA-JUN/OpenWeed-GUI-PyQt5-YOLO.git
```
After downloading the project files, you can install the required libraries by running the following command:

```bash
pip install -r requirements.txt
```
It should be noted that you need to install [Vimba SDK](https://github.com/alliedvision/VimbaPython) , if you use a Vimba camera.

## Run

After downloading the project files and installing the required libraries, you can start the GUI by running the following command:

```bash
python WeedGUI.py
```
![Field Test](./Pictures/Test_video.gif "Field Test")


# Models

## CottonWeedDet12
OpenWeedGUI supports over 20 well-trained YOLO models for weed detection, offering the capability to identify more than 10 types of weeds. You can download weed detectors from YOLOv3 to YOLOv5 from this link:

https://drive.google.com/drive/mobile/folders/15AloANR9ol9NZukM4l50CcT7sw8KX0iS?usp=share_link

These models were trained based on [CottonWeedDet12](https://zenodo.org/records/7535814) dataset that contains 12-class weeds.

## Cross-season weed dataset 

It is noted that YOLOX and YOLOv8 models were not trained on CottonWeedDet12, but they were trained in a separate study based on [Cross-season](https://elibrary.asabe.org/abstract.asp?JID=5&AID=54499&CID=oma2023&T=1) weed dataset. You can download these models from this link:

https://drive.google.com/drive/folders/1l9rb8od7Jzt4aWahFW4bxQZKpMcD7XrR?usp=drive_link

## Note 
OpenWeedGUI integrates the models into the system. After you download these models, you may need to change the model path in the main code!


# Citing This Work

If you use OpenWeedGUI for your research, please consider citing our paper. This helps us to continue providing updates and support for the project. Below is the BibTeX entry for our paper:

```bibtex
@inproceedings{xu2023openweedgui,
  title={OpenWeedGUI: an open-source graphical user interface for weed imaging and detection},
  author={Xu, Jiajun and Lu, Yuzhen},
  booktitle={Autonomous Air and Ground Sensing Systems for Agricultural Optimization and Phenotyping VIII},
  volume={12539},
  pages={97--106},
  year={2023},
  organization={SPIE}
}
```





