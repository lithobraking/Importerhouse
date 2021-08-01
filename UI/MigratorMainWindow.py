import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from UIresources.app_window import Ui_app_window

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)  # enables high dpi scaling since I use a 4k monitor
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)  # use high dpi icons

class AppWindow(qtw.QWidget, Ui_app_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filepath_browse_button.clicked.connect(self.set_filepath)

    # TODO - add logic that stores data entered in fields for use
    def set_filepath(self):
        import os
        default_path = os.path.join(os.path.expanduser('~'), 'Documents')
        filepath = qtw.QFileDialog.getOpenFileName(self, 'Load File', default_path, 'Comma Separated Values (*.csv)')
        print(filepath[0])
        self.filepath_field.setText(filepath[0])

    # def set_datatype(self):
    #     TODO - implement datatype setter
    #
    # def set_email(self):
    #     TODO - implement email address setter
    #
    # def set_password(self):
    #     TODO - implement password setter

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    view = AppWindow()
    view.show()
    sys.exit(app.exec_())