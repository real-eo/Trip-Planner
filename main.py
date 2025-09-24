from PyQt5 import QtWidgets

import planner
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Create the application

    program = planner.Planner()

    app.exec_()  # Start the event loop

