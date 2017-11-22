from PyQt5.QtWidgets import QApplication

import sys

from FileManager import FileManager
from UI.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    window.raise_()
    app.exec_()
    # file_path = input("please enter a text file to open: ")
    # response = FileManager.open_file(file_path)
    # success,exception = response.was_successful()
    # if success:
    #     lines = response.get_lines()
    #     for line in lines:
    #         print(line.replace("\n", ""))
    # else:
    #     print("Error: {}".format(exception))


if __name__ == "__main__":
    main()
