from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QStatusBar, QErrorMessage

from FileManager import FileManager
from .MainLayout import MainLayout
from .MenuBar import MenuBar
from .ToolBar import ToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # get components of window
        self.menu_bar = MenuBar()
        self.toolbar = ToolBar()
        self.main_layout = MainLayout()
        self.status_bar = QStatusBar()

        # set menu bar, toolbars and status bar
        self.setMenuBar(self.menu_bar)
        self.addToolBar(self.toolbar)
        self.setStatusBar(self.status_bar)

        # set central widget
        self.setCentralWidget(self.main_layout)

        self.setContentsMargins(0, 0, 0, 0)

        # event connections
        # menu bar events
        self.menu_bar.open_file.triggered.connect(self.load_file)
        self.menu_bar.save_file.triggered.connect(self.save_file)

        # toolbar events
        self.toolbar.size_combo_box.currentIndexChanged.connect(self.change_font_size)
        self.toolbar.font_combo_box.currentIndexChanged.connect(self.change_font_family)
        self.toolbar.language_combo_box.currentIndexChanged.connect(self.change_language)

    def load_file(self):
        filename = QFileDialog.getExistingDirectory(self, 'Open File or directory')[0]
        response = FileManager.open_file(filename)
        success, exception = response.was_successful()
        if success:
            self.main_layout.central_layout.load_lines(response.get_lines())
            # self.main_layout.side_bar.show_directory(filename)
            self.status_bar.showMessage("Opened file: {}".format(filename))
        else:
            self.status_bar.showMessage(exception)

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')[0]
        text = self.main_layout.central_layout.text_box.toPlainText()
        FileManager.save_file(filename, text)

    def change_font_size(self):
        font_size = self.toolbar.size_combo_box.currentText()
        self.main_layout.central_layout.text_box.set_font_size(font_size)

    def change_font_family(self):
        font_family = self.toolbar.font_combo_box.currentText()
        self.main_layout.central_layout.text_box.set_font_family(font_family)

    def change_language(self):
        language = self.toolbar.language_combo_box.currentText()
        if language == "Python":
            self.main_layout.central_layout.text_box.set_highlighter(self.main_layout.central_layout.text_box.Syntax.python)
