from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QLabel

class DrawingLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.start_pos = None
        self.end_pos = None
        self.ROI_Window = parent
        self.dragging = False

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.start_pos and self.end_pos and self.is_inside_rectangle(event.pos()):
                self.dragging = True
            else:
                self.start_pos = event.pos()
                self.end_pos = None
                self.dragging = False
                self.update_labels()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.dragging:
                self.move_rectangle(event.pos())
            else:
                self.end_pos = event.pos()
                self.update_labels()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.dragging:
                self.move_rectangle(event.pos())
                self.dragging = False
            else:
                self.end_pos = event.pos()
                self.update()
                self.print_rectangle_info()
                self.ROI_Window.update_labels(self.start_pos, self.end_pos)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.start_pos and self.end_pos:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2))
            painter.drawRect(QRect(self.start_pos, self.end_pos))

    def print_rectangle_info(self):
        if self.start_pos and self.end_pos:
            x = min(self.start_pos.x(), self.end_pos.x())
            y = min(self.start_pos.y(), self.end_pos.y())
            width = abs(self.start_pos.x() - self.end_pos.x())
            height = abs(self.start_pos.y() - self.end_pos.y())
            print("Rectangle position: ({}, {})".format(x, y))
            print("Rectangle size: {} x {}".format(width, height))

    def is_inside_rectangle(self, point):
        if self.start_pos and self.end_pos:
            x = min(self.start_pos.x(), self.end_pos.x())
            y = min(self.start_pos.y(), self.end_pos.y())
            width = abs(self.start_pos.x() - self.end_pos.x())
            height = abs(self.start_pos.y() - self.end_pos.y())
            rect = QRect(x, y, width, height)
            return rect.contains(point)
        return False

    def move_rectangle(self, new_pos):
        if self.start_pos and self.end_pos:
            width = abs(self.start_pos.x() - self.end_pos.x())
            height = abs(self.start_pos.y() - self.end_pos.y())
            x = new_pos.x() - width // 2
            y = new_pos.y() - height // 2
            self.start_pos = QPoint(x, y)
            self.end_pos = QPoint(x + width, y + height)
            self.update_labels()
            self.update()

    def update_labels(self):
        if self.start_pos and self.end_pos:
            x = min(self.start_pos.x(), self.end_pos.x())
            y = min(self.start_pos.y(), self.end_pos.y())
            width = abs(self.start_pos.x() - self.end_pos.x())
            height = abs(self.start_pos.y() - self.end_pos.y())
            self.ROI_Window.update_labels(QPoint(x, y), QPoint(x + width, y + height))