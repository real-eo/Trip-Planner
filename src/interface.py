# User interface components and pop-up windows
from PyQt5 import QtWidgets, QtCore, QtGui


# class InterfaceBase:
#     def __init__(self, window:QtWidgets.QMainWindow=None, title:str=None, geometry:QtCore.QRect=None):
#         self.window = window if window else QtWidgets.QMainWindow()
#         self.window.setWindowTitle(title if title else "Trip Planner")
#         self.window.setGeometry(geometry if geometry else QtCore.QRect(100, 100, 800, 600))
#         self.central_widget = QtWidgets.QWidget()

class PlannerInterface:
    def __init__(self):
        pass