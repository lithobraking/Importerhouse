import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from UIresources.app_window import Ui_app_window

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)  # enables high dpi scaling since I use a 4k monitor
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)  # use high dpi icons

class AppWindow(qtw.QWidget, Ui_app_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.filepath = None

    # def set_filepath(self):
    #     # stub
    #
    # def set_datatype(self):
    #     # stub
    #
    # def set_email(self):
    #     email = self.email_field.text()
    #
    # def set_password(self):
    #     # stub

if __name__ == '__main__':
    app = qtw.QApplication([])

    view = AppWindow()
    view.show()
    sys.exit(app.exec_())