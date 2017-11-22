from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QGraphicsPixmapItem, QPushButton, QWidget
from PyQt5.QtCore import Qt
from pathlib import Path

import os


class SideBar(QWidget):
    class ControlBar(QWidget):
        def __init__(self):
            super().__init__()
            self.toggle_button = QPushButton("<")
            self.toggle_button.setMaximumSize(20, 20)

            self.layout = QHBoxLayout()
            self.layout.addWidget(self.toggle_button, Qt.AlignRight)
            self.layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
            self.layout.setContentsMargins(0, 0, 0, 0)

            self.setLayout(self.layout)

    def __init__(self):
        super().__init__()
        self.control_bar = SideBar.ControlBar()
        self.setFixedWidth(300)

        self.visible = True
        self.open_directory = None
        self.labels = []

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.control_bar)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.layout)
        self.setContentsMargins(0,0,0,0)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.control_bar.toggle_button.clicked.connect(self.toggle)

    def toggle(self):
        if self.visible:
            self.setFixedWidth(0)
            self.control_bar.toggle_button.setText(">")
            self.visible = False
        else:
            self.setFixedWidth(300)
            self.control_bar.toggle_button.setText("<")
            self.visible = True

    def show_directory(self, path):
        self.labels.clear()
        self.open_directory = path
        if os.path.isfile(path):
            label = QLabel(os.path.basename(path))
            self.labels.append(label)
        else:
            dir_label = QLabel(os.path.basename(path))
            self.labels.append(dir_label)

            rootdir = Path(path)
            file_list = [f for f in rootdir.glob('**\\*')]
            for file in file_list:
                label = QLabel(os.path.basename(path))
                self.labels.append(label)

        for label in self.labels:
            self.layout.addWidget(label)

    def close_directory(self):
        for label in self.labels:
            self.layout.removeWidget(label)
        self.labels.clear()
