from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSignal, QPoint
from drawing_label import DrawingLabel

class ROI_Window(QMainWindow):
    size_signal = pyqtSignal(tuple)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Setting ROI')
        # Access properties of the main window
        self.label_roi = DrawingLabel(self)
        #DrawingLabel
        self.label_roi.resize(parent.label_pic.width(), parent.label_pic.height())
        self.label_roi.setStyleSheet("QLabel{background:white;}")
        self.resize(parent.label_pic.width(),parent.label_pic.height()+240)
        #label_roi.move(0, 0)
        self.coordinate_label = QLabel("Coordinates:")
        self.coordinate_label.setMaximumHeight(20)
        self.size_label = QLabel("Size:")
        self.size_label.setMaximumHeight(20)
        self.set_button = QPushButton("set")
        self.set_button.clicked.connect(self.send_size)
        self.reset_button = QPushButton("reset")
        self.reset_button.clicked.connect(self.reset_label)
        self.size_input = QLineEdit()
        self.size_input.setPlaceholderText("Enter rectangle size (e.g., '100x50')")
        self.place_button = QPushButton("Place")
        self.place_button.clicked.connect(self.place_rectangle)

        layout = QVBoxLayout()
        layout.addWidget(self.label_roi)
        layout.addWidget(self.coordinate_label)
        layout.addWidget(self.size_label)
        layout.addWidget(self.set_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.size_input)
        layout.addWidget(self.place_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update_labels(self, start_pos, end_pos):
        x = min(start_pos.x(), end_pos.x())
        y = min(start_pos.y(), end_pos.y())
        width = abs(start_pos.x() - end_pos.x())
        height = abs(start_pos.y() - end_pos.y())
        self.coordinate_label.setText("Coordinates: ({}, {})".format(x, y))
        self.size_label.setText("Size: {} x {}".format(width, height))
        #self.coordinate_label.setText("Coordinates: ({}, {})".format(x, y))
        #self.size_label.setText("Size: {} x {}".format(width, height))


    def place_rectangle(self):
        size_input = self.size_input.text().strip()
        if self.label_roi.start_pos and size_input:
            width, height = size_input.split('x')
            width = int(width.strip())
            height = int(height.strip())
            x = self.label_roi.start_pos.x()
            y = self.label_roi.start_pos.y()
            end_pos = QPoint(x + width, y + height)
            self.label_roi.end_pos = end_pos
            self.update_labels(self.label_roi.start_pos, self.label_roi.end_pos)
            self.label_roi.update()

    def send_size(self):
        if self.label_roi.start_pos and self.label_roi.end_pos:
            x = min(self.label_roi.start_pos.x(), self.label_roi.end_pos.x())
            y = min(self.label_roi.start_pos.y(), self.label_roi.end_pos.y())
            width = abs(self.label_roi.start_pos.x() - self.label_roi.end_pos.x())
            height = abs(self.label_roi.start_pos.y() - self.label_roi.end_pos.y())
            size_data = (x, y, width,height)
            #print(size_data)
            self.size_signal.emit(size_data)
    def reset_label(self):
        self.parent.resize(717, 669)
