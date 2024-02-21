# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWeed.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenWeedGUI(object):
    def setupUi(self, OpenWeedGUI):
        OpenWeedGUI.setObjectName("OpenWeedGUI")
        OpenWeedGUI.resize(1160, 837)
        OpenWeedGUI.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(OpenWeedGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(1022, 670))
        self.widget.setStyleSheet("#widget{\n"
"    \n"
"    \n"
"    background-image: url(:/icon/icon/HD-Lime-Green-Background.jpg);\n"
"    \n"
"\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("#frame\n"
"{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 19, 0.5), stop:1 rgba(255, 209, 255, 255));\n"
"border-radius:22px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setStyleSheet("#groupBox_5{\n"
"background-color: rgba(48,148,243,0);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid #d9d9d9;\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_5)
        self.fileButton.setMinimumSize(QtCore.QSize(55, 28))
        self.fileButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.fileButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.fileButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/icon-image-513.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_8.addWidget(self.fileButton)
        self.OpenVideoButton = QtWidgets.QPushButton(self.groupBox_5)
        self.OpenVideoButton.setMinimumSize(QtCore.QSize(55, 28))
        self.OpenVideoButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.OpenVideoButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:black;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.OpenVideoButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/资源 3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenVideoButton.setIcon(icon1)
        self.OpenVideoButton.setObjectName("OpenVideoButton")
        self.horizontalLayout_8.addWidget(self.OpenVideoButton)
        self.cameraButton = QtWidgets.QPushButton(self.groupBox_5)
        self.cameraButton.setMinimumSize(QtCore.QSize(55, 28))
        self.cameraButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cameraButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.cameraButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/camera_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraButton.setIcon(icon2)
        self.cameraButton.setObjectName("cameraButton")
        self.horizontalLayout_8.addWidget(self.cameraButton)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 7, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_2.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:rgba(1, 1, 1,50);\n"
"selection-background-color: rgba(1, 200, 1,50);\n"
"color: rgb(218, 218, 218);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,30);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/img/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_pt = QtWidgets.QComboBox(self.frame)
        self.comboBox_pt.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_pt.setStyleSheet("\n"
"QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:rgba(1, 1, 1,50);\n"
"selection-background-color: rgba(1, 200, 1,50);\n"
"color: rgb(218, 218, 218);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,30);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/img/icon/下拉_白色.png);\n"
"}\n"
"\n"
"")
        self.comboBox_pt.setObjectName("comboBox_pt")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_pt)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.confSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.confSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.confSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.confSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.confSpinBox.setMinimum(0.1)
        self.confSpinBox.setMaximum(1.0)
        self.confSpinBox.setSingleStep(0.01)
        self.confSpinBox.setProperty("value", 0.25)
        self.confSpinBox.setObjectName("confSpinBox")
        self.horizontalLayout_3.addWidget(self.confSpinBox)
        self.confSlider = QtWidgets.QSlider(self.frame)
        self.confSlider.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     border-image: url(:/img/icon/圆.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;                  \n"
"} \n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.confSlider.setMaximum(100)
        self.confSlider.setProperty("value", 25)
        self.confSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.confSlider.setObjectName("confSlider")
        self.horizontalLayout_3.addWidget(self.confSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_check = QtWidgets.QCheckBox(self.frame)
        self.save_check.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.save_check.setChecked(False)
        self.save_check.setObjectName("save_check")
        self.horizontalLayout.addWidget(self.save_check)
        self.detect_check = QtWidgets.QCheckBox(self.frame)
        self.detect_check.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.detect_check.setChecked(False)
        self.detect_check.setObjectName("detect_check")
        self.horizontalLayout.addWidget(self.detect_check)
        self.clearButton = QtWidgets.QPushButton(self.frame)
        self.clearButton.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.save_num = QtWidgets.QDoubleSpinBox(self.frame)
        self.save_num.setMinimumSize(QtCore.QSize(50, 0))
        self.save_num.setMaximumSize(QtCore.QSize(50, 16777215))
        self.save_num.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.save_num.setMaximum(200.0)
        self.save_num.setSingleStep(1.0)
        self.save_num.setProperty("value", 5.0)
        self.save_num.setObjectName("save_num")
        self.horizontalLayout_6.addWidget(self.save_num)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_6.setStretch(0, 7)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setMinimumSize(QtCore.QSize(0, 35))
        self.label_25.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_25.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_26.addWidget(self.label_25)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_4.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:rgba(1, 1, 1,50);\n"
"selection-background-color: rgba(1, 200, 1,50);\n"
"color: rgb(218, 218, 218);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,30);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/img/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_26.addWidget(self.comboBox_4)
        self.pushButton_45 = QtWidgets.QPushButton(self.frame)
        self.pushButton_45.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"")
        self.pushButton_45.setObjectName("pushButton_45")
        self.horizontalLayout_26.addWidget(self.pushButton_45)
        self.horizontalLayout_26.setStretch(0, 10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setSpacing(4)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_25.addWidget(self.label_27)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.setImPathButton = QtWidgets.QPushButton(self.frame)
        self.setImPathButton.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"")
        self.setImPathButton.setObjectName("setImPathButton")
        self.horizontalLayout_27.addWidget(self.setImPathButton)
        self.saveCheckBox_6 = QtWidgets.QCheckBox(self.frame)
        self.saveCheckBox_6.setEnabled(True)
        self.saveCheckBox_6.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.saveCheckBox_6.setChecked(True)
        self.saveCheckBox_6.setObjectName("saveCheckBox_6")
        self.horizontalLayout_27.addWidget(self.saveCheckBox_6)
        self.verticalLayout_25.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.pushButton_46 = QtWidgets.QPushButton(self.frame)
        self.pushButton_46.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"")
        self.pushButton_46.setObjectName("pushButton_46")
        self.horizontalLayout_30.addWidget(self.pushButton_46)
        self.saveCheckBox_7 = QtWidgets.QCheckBox(self.frame)
        self.saveCheckBox_7.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.saveCheckBox_7.setChecked(True)
        self.saveCheckBox_7.setObjectName("saveCheckBox_7")
        self.horizontalLayout_30.addWidget(self.saveCheckBox_7)
        self.verticalLayout_25.addLayout(self.horizontalLayout_30)
        self.verticalLayout_4.addLayout(self.verticalLayout_25)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.camMButton = QtWidgets.QPushButton(self.frame)
        self.camMButton.setStyleSheet("QPushButton {\n"
"    font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"    border-radius: 9px;\n"
"    background: rgba(153, 195, 205, 0.5);\n"
"    color: rgb(218, 218, 218);\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(153, 195, 205, 0.7); /* Change background on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgba(153, 195, 205, 0.9); /* Change background on press */\n"
"}\n"
"")
        self.camMButton.setObjectName("camMButton")
        self.horizontalLayout_12.addWidget(self.camMButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Exposure_offBox = QtWidgets.QCheckBox(self.frame)
        self.Exposure_offBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.Exposure_offBox.setChecked(False)
        self.Exposure_offBox.setTristate(False)
        self.Exposure_offBox.setObjectName("Exposure_offBox")
        self.horizontalLayout_4.addWidget(self.Exposure_offBox)
        self.Exposure_onceBox = QtWidgets.QCheckBox(self.frame)
        self.Exposure_onceBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.Exposure_onceBox.setChecked(False)
        self.Exposure_onceBox.setObjectName("Exposure_onceBox")
        self.horizontalLayout_4.addWidget(self.Exposure_onceBox)
        self.Exposure_continueBox = QtWidgets.QCheckBox(self.frame)
        self.Exposure_continueBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.Exposure_continueBox.setChecked(True)
        self.Exposure_continueBox.setObjectName("Exposure_continueBox")
        self.horizontalLayout_4.addWidget(self.Exposure_continueBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.GainSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.GainSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.GainSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.GainSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.GainSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.GainSpinBox.setMinimum(0.2)
        self.GainSpinBox.setMaximum(24.0)
        self.GainSpinBox.setSingleStep(0.2)
        self.GainSpinBox.setProperty("value", 4.8)
        self.GainSpinBox.setObjectName("GainSpinBox")
        self.horizontalLayout_5.addWidget(self.GainSpinBox)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.GammaSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.GammaSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.GammaSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.GammaSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.GammaSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.GammaSpinBox.setMinimum(0.5)
        self.GammaSpinBox.setMaximum(2.5)
        self.GammaSpinBox.setSingleStep(0.5)
        self.GammaSpinBox.setProperty("value", 0.95)
        self.GammaSpinBox.setObjectName("GammaSpinBox")
        self.horizontalLayout_5.addWidget(self.GammaSpinBox)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.IntensitySpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.IntensitySpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.IntensitySpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.IntensitySpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.IntensitySpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.IntensitySpinBox.setMinimum(10.0)
        self.IntensitySpinBox.setMaximum(89.0)
        self.IntensitySpinBox.setSingleStep(1.0)
        self.IntensitySpinBox.setProperty("value", 48.0)
        self.IntensitySpinBox.setObjectName("IntensitySpinBox")
        self.horizontalLayout_5.addWidget(self.IntensitySpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.OpenCamButton = QtWidgets.QPushButton(self.frame)
        self.OpenCamButton.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QPushButton:checked{\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(153, 195, 205, 0.7); /* Change background on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"")
        self.OpenCamButton.setObjectName("OpenCamButton")
        self.verticalLayout_4.addWidget(self.OpenCamButton)
        self.ReControl = QtWidgets.QPushButton(self.frame)
        self.ReControl.setStyleSheet("QPushButton\n"
"\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(153, 195, 205, 0.5);\n"
"    ;\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(153, 195, 205, 0.7); /* Change background on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.ReControl.setObjectName("ReControl")
        self.verticalLayout_4.addWidget(self.ReControl)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.resultWidget = QtWidgets.QListWidget(self.frame)
        self.resultWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(12, 28, 77, 0);\n"
"border: 1px solid rgba(200, 200, 200,100);\n"
"border-bottom: 0px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.resultWidget.setObjectName("resultWidget")
        self.verticalLayout_7.addWidget(self.resultWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.label_speed = QtWidgets.QLabel(self.frame)
        self.label_speed.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 15px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_speed.setObjectName("label_speed")
        self.verticalLayout_4.addWidget(self.label_speed)
        self.horizontalLayout_7.addWidget(self.frame)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(-1, -1, 7, -1)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setMinimumSize(QtCore.QSize(0, 35))
        self.label_26.setMaximumSize(QtCore.QSize(185, 16777215))
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_29.addWidget(self.label_26)
        self.verticalLayout_5.addLayout(self.horizontalLayout_29)
        self.label_pic = QtWidgets.QLabel(self.widget)
        self.label_pic.setMinimumSize(QtCore.QSize(0, 0))
        self.label_pic.setStyleSheet("\n"
"QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"    background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(144, 246, 0, 34), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"")
        self.label_pic.setObjectName("label_pic")
        self.verticalLayout_5.addWidget(self.label_pic)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.runVideoButton = QtWidgets.QPushButton(self.widget)
        self.runVideoButton.setMinimumSize(QtCore.QSize(40, 40))
        self.runVideoButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.runVideoButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/运行.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/暂停.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.runVideoButton.setIcon(icon3)
        self.runVideoButton.setIconSize(QtCore.QSize(30, 30))
        self.runVideoButton.setCheckable(True)
        self.runVideoButton.setObjectName("runVideoButton")
        self.horizontalLayout_28.addWidget(self.runVideoButton)
        self.videoSlider = QtWidgets.QSlider(self.widget)
        self.videoSlider.setStyleSheet("QSlider{\n"
"border-color: #bcbcbc;\n"
"color:#d9d9d9;\n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     border-image: url(:/img/icon/圆.png);\n"
"     width:15px;\n"
"     margin: -7px -7px -7px -7px;                  \n"
"} \n"
"QSlider::add-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::sub-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.videoSlider.setMaximum(100)
        self.videoSlider.setProperty("value", 0)
        self.videoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.videoSlider.setObjectName("videoSlider")
        self.horizontalLayout_28.addWidget(self.videoSlider)
        self.stopVideoButton = QtWidgets.QPushButton(self.widget)
        self.stopVideoButton.setMinimumSize(QtCore.QSize(40, 40))
        self.stopVideoButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.stopVideoButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icon/终止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopVideoButton.setIcon(icon4)
        self.stopVideoButton.setIconSize(QtCore.QSize(30, 30))
        self.stopVideoButton.setObjectName("stopVideoButton")
        self.horizontalLayout_28.addWidget(self.stopVideoButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_28)
        self.verticalLayout_5.setStretch(1, 8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 7)
        self.horizontalLayout_10.addWidget(self.widget)
        OpenWeedGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OpenWeedGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuModel_select = QtWidgets.QMenu(self.menuSetting)
        self.menuModel_select.setObjectName("menuModel_select")
        self.menuYOLOv5 = QtWidgets.QMenu(self.menuModel_select)
        self.menuYOLOv5.setObjectName("menuYOLOv5")
        self.menuCam_set = QtWidgets.QMenu(self.menuSetting)
        self.menuCam_set.setObjectName("menuCam_set")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        OpenWeedGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OpenWeedGUI)
        self.statusbar.setObjectName("statusbar")
        OpenWeedGUI.setStatusBar(self.statusbar)
        self.actionOpen_image_file = QtWidgets.QAction(OpenWeedGUI)
        self.actionOpen_image_file.setObjectName("actionOpen_image_file")
        self.actionOpen_video_file = QtWidgets.QAction(OpenWeedGUI)
        self.actionOpen_video_file.setObjectName("actionOpen_video_file")
        self.actionClose = QtWidgets.QAction(OpenWeedGUI)
        self.actionClose.setObjectName("actionClose")
        self.actionCut = QtWidgets.QAction(OpenWeedGUI)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(OpenWeedGUI)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy_path = QtWidgets.QAction(OpenWeedGUI)
        self.actionCopy_path.setObjectName("actionCopy_path")
        self.actionPath_set = QtWidgets.QAction(OpenWeedGUI)
        self.actionPath_set.setObjectName("actionPath_set")
        self.actionYOLOv3 = QtWidgets.QAction(OpenWeedGUI)
        self.actionYOLOv3.setObjectName("actionYOLOv3")
        self.actionYOLOv4 = QtWidgets.QAction(OpenWeedGUI)
        self.actionYOLOv4.setObjectName("actionYOLOv4")
        self.actionbestS = QtWidgets.QAction(OpenWeedGUI)
        self.actionbestS.setObjectName("actionbestS")
        self.actionbestL = QtWidgets.QAction(OpenWeedGUI)
        self.actionbestL.setObjectName("actionbestL")
        self.actionbestM = QtWidgets.QAction(OpenWeedGUI)
        self.actionbestM.setObjectName("actionbestM")
        self.actionbestN = QtWidgets.QAction(OpenWeedGUI)
        self.actionbestN.setObjectName("actionbestN")
        self.actionbestL_2 = QtWidgets.QAction(OpenWeedGUI)
        self.actionbestL_2.setObjectName("actionbestL_2")
        self.actionSet_ROI = QtWidgets.QAction(OpenWeedGUI)
        self.actionSet_ROI.setObjectName("actionSet_ROI")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_image_file)
        self.menuFile.addAction(self.actionOpen_video_file)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCopy_path)
        self.menuYOLOv5.addAction(self.actionbestS)
        self.menuYOLOv5.addAction(self.actionbestL)
        self.menuYOLOv5.addAction(self.actionbestM)
        self.menuYOLOv5.addAction(self.actionbestN)
        self.menuYOLOv5.addAction(self.actionbestL_2)
        self.menuModel_select.addAction(self.actionYOLOv3)
        self.menuModel_select.addAction(self.actionYOLOv4)
        self.menuModel_select.addAction(self.menuYOLOv5.menuAction())
        self.menuCam_set.addAction(self.actionSet_ROI)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.menuCam_set.menuAction())
        self.menuSetting.addAction(self.actionPath_set)
        self.menuSetting.addAction(self.menuModel_select.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(OpenWeedGUI)
        QtCore.QMetaObject.connectSlotsByName(OpenWeedGUI)

    def retranslateUi(self, OpenWeedGUI):
        _translate = QtCore.QCoreApplication.translate
        OpenWeedGUI.setWindowTitle(_translate("OpenWeedGUI", "MainWindow"))
        self.label_10.setText(_translate("OpenWeedGUI", "Input"))
        self.fileButton.setToolTip(_translate("OpenWeedGUI", "Image File"))
        self.OpenVideoButton.setToolTip(_translate("OpenWeedGUI", "Video file"))
        self.cameraButton.setToolTip(_translate("OpenWeedGUI", "Open camera"))
        self.label_3.setText(_translate("OpenWeedGUI", "Model "))
        self.comboBox_2.setItemText(0, _translate("OpenWeedGUI", "yolov5"))
        self.comboBox_2.setItemText(1, _translate("OpenWeedGUI", "yolov3"))
        self.comboBox_2.setItemText(2, _translate("OpenWeedGUI", "yolov8"))
        self.comboBox_2.setItemText(3, _translate("OpenWeedGUI", "yolox"))
        self.comboBox_2.setItemText(4, _translate("OpenWeedGUI", "yolor"))
        self.comboBox_2.setItemText(5, _translate("OpenWeedGUI", "yolov4"))
        self.comboBox_2.setItemText(6, _translate("OpenWeedGUI", "Scaled-yolov4"))
        self.comboBox_pt.setItemText(0, _translate("OpenWeedGUI", "bestN.pt"))
        self.comboBox_pt.setItemText(1, _translate("OpenWeedGUI", "bestS.pt"))
        self.comboBox_pt.setItemText(2, _translate("OpenWeedGUI", "bestM.pt"))
        self.comboBox_pt.setItemText(3, _translate("OpenWeedGUI", "bestL.pt"))
        self.comboBox_pt.setItemText(4, _translate("OpenWeedGUI", "bestX.pt"))
        self.comboBox_pt.setItemText(5, _translate("OpenWeedGUI", "bestN.engine"))
        self.comboBox_pt.setItemText(6, _translate("OpenWeedGUI", "bestS.engine"))
        self.comboBox_pt.setItemText(7, _translate("OpenWeedGUI", "bestM.engine"))
        self.comboBox_pt.setItemText(8, _translate("OpenWeedGUI", "bestL.engine"))
        self.label.setText(_translate("OpenWeedGUI", "Confidence Setting"))
        self.save_check.setText(_translate("OpenWeedGUI", "Save"))
        self.detect_check.setText(_translate("OpenWeedGUI", "Detection"))
        self.clearButton.setText(_translate("OpenWeedGUI", "Clear frame"))
        self.label_2.setText(_translate("OpenWeedGUI", "Save Interval (s):"))
        self.label_25.setText(_translate("OpenWeedGUI", "Saving Resolution :"))
        self.comboBox_4.setItemText(0, _translate("OpenWeedGUI", "640*640"))
        self.comboBox_4.setItemText(1, _translate("OpenWeedGUI", "512*512"))
        self.comboBox_4.setItemText(2, _translate("OpenWeedGUI", "1920*1080"))
        self.pushButton_45.setText(_translate("OpenWeedGUI", "Define"))
        self.label_27.setText(_translate("OpenWeedGUI", "Saving Path"))
        self.setImPathButton.setText(_translate("OpenWeedGUI", "Image path"))
        self.saveCheckBox_6.setText(_translate("OpenWeedGUI", "Auto"))
        self.pushButton_46.setText(_translate("OpenWeedGUI", "Jeson path"))
        self.saveCheckBox_7.setText(_translate("OpenWeedGUI", "Auto"))
        self.label_9.setText(_translate("OpenWeedGUI", "Camera Setting"))
        self.camMButton.setText(_translate("OpenWeedGUI", "More"))
        self.label_4.setText(_translate("OpenWeedGUI", "Exposure Auto:"))
        self.Exposure_offBox.setText(_translate("OpenWeedGUI", "Off"))
        self.Exposure_onceBox.setText(_translate("OpenWeedGUI", "Once"))
        self.Exposure_continueBox.setText(_translate("OpenWeedGUI", "Continues"))
        self.label_5.setText(_translate("OpenWeedGUI", "Gain:"))
        self.label_6.setText(_translate("OpenWeedGUI", "Gamma:"))
        self.label_7.setText(_translate("OpenWeedGUI", "Intensity:"))
        self.OpenCamButton.setText(_translate("OpenWeedGUI", "Open Camera"))
        self.ReControl.setText(_translate("OpenWeedGUI", "Relay Control"))
        self.label_11.setText(_translate("OpenWeedGUI", "Results"))
        self.label_speed.setText(_translate("OpenWeedGUI", "Current Speed:"))
        self.label_26.setText(_translate("OpenWeedGUI", "OpenWeed Interface"))
        self.label_pic.setText(_translate("OpenWeedGUI", "Frame"))
        self.menuFile.setTitle(_translate("OpenWeedGUI", "File"))
        self.menuEdit.setTitle(_translate("OpenWeedGUI", "Edit"))
        self.menuSetting.setTitle(_translate("OpenWeedGUI", "Setting"))
        self.menuModel_select.setTitle(_translate("OpenWeedGUI", "Model select"))
        self.menuYOLOv5.setTitle(_translate("OpenWeedGUI", "YOLOv5"))
        self.menuCam_set.setTitle(_translate("OpenWeedGUI", "Cam set"))
        self.menuHelp.setTitle(_translate("OpenWeedGUI", "Help"))
        self.actionOpen_image_file.setText(_translate("OpenWeedGUI", "Open image file"))
        self.actionOpen_video_file.setText(_translate("OpenWeedGUI", "Open video file"))
        self.actionClose.setText(_translate("OpenWeedGUI", "Close"))
        self.actionCut.setText(_translate("OpenWeedGUI", "Cut"))
        self.actionCopy.setText(_translate("OpenWeedGUI", "Copy"))
        self.actionCopy_path.setText(_translate("OpenWeedGUI", "Copy path"))
        self.actionPath_set.setText(_translate("OpenWeedGUI", "Path set"))
        self.actionYOLOv3.setText(_translate("OpenWeedGUI", "YOLOv3"))
        self.actionYOLOv4.setText(_translate("OpenWeedGUI", "YOLOv4"))
        self.actionbestS.setText(_translate("OpenWeedGUI", "bestS"))
        self.actionbestL.setText(_translate("OpenWeedGUI", "bestX"))
        self.actionbestM.setText(_translate("OpenWeedGUI", "bestM"))
        self.actionbestN.setText(_translate("OpenWeedGUI", "bestN"))
        self.actionbestL_2.setText(_translate("OpenWeedGUI", "bestL"))
        self.actionSet_ROI.setText(_translate("OpenWeedGUI", "Set ROI"))
import WeedRC_rc
import apprcc_rc
import figInAPP_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenWeedGUI = QtWidgets.QMainWindow()
    ui = Ui_OpenWeedGUI()
    ui.setupUi(OpenWeedGUI)
    OpenWeedGUI.show()
    sys.exit(app.exec_())
