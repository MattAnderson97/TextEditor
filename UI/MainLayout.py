from PyQt5.QtWidgets import QHBoxLayout, QWidget

from .CentralLayout import CentralLayout
from .SideBar import SideBar


class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.central_layout = CentralLayout()
        self.side_bar = SideBar()

        layout = QHBoxLayout()
        # layout.addWidget(self.side_bar)
        layout.addWidget(self.central_layout)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)