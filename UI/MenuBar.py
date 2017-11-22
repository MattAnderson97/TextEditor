from PyQt5.QtWidgets import QMenuBar, QMenu


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        self.file_menu = QMenu("File")
        self.open_file = self.file_menu.addAction("Open File")
        self.save_file = self.file_menu.addAction("Save File")

        self.addMenu(self.file_menu)