from pygame import MyWidget
from PySide6 import QtCore, QtWidgets, QtGui
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())