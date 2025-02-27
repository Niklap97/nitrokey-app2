import sys

from PyQt5 import QtWidgets

import nitrokeyapp.resources_rc  # noqa: F401
from nitrokeyapp.gui import GUI, BackendThread
from nitrokeyapp.qt_utils_mix_in import QtUtilsMixIn


def main():
    # backend thread init
    QtUtilsMixIn.backend_thread = BackendThread()

    app = QtWidgets.QApplication(sys.argv)

    window = GUI(app)  # noqa: F841
    app.exec()


main()
