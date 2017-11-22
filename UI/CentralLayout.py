from PyQt5.QtWidgets import QVBoxLayout, QTextEdit, QWidget


from .LineTextEdit import LineTextWidget


class CentralLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.text_box = LineTextWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.text_box)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setStyleSheet("padding: 0px;")

    def load_lines(self, lines):
        self.text_box.number_bar.edit.clear()
        self.text_box.number_bar.edit.setText("".join(lines))