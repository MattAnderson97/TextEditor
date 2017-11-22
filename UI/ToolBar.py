from PyQt5.QtWidgets import QToolBar, QComboBox, QLabel
from PyQt5.QtCore import Qt

import matplotlib.font_manager


class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()
        # create font size combobox
        self.size_combo_box = QComboBox()
        # add size numbers to combobox
        self.size_combo_box.addItems(["8","9","10","11","12","14","16","18","24","30","36","48","60","72","96"])

        self.font_combo_box = QComboBox()
        # get system fonts
        flist = matplotlib.font_manager.get_fontconfig_fonts()
        # get list of font names
        names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
        # put into new list without duplicates
        fonts = []
        for name in names:
            if not name in fonts:
                fonts.append(name)
        # sort alphabetically
        fonts.sort()
        # add to combo box
        self.font_combo_box.addItems(fonts)

        # select language
        self.language_combo_box = QComboBox()
        self.language_combo_box.addItem("None")
        self.language_combo_box.addItem("Python")

        # add widgets to toolbar
        self.addWidget(QLabel("Font size: "))
        self.addWidget(self.size_combo_box)
        self.addWidget(QLabel("  Font family: "))
        self.addWidget(self.font_combo_box)
        self.addWidget(QLabel("  Language: "))
        self.addWidget(self.language_combo_box)