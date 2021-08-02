import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from UIresources.app_window import Ui_app_window
from DataManager import DataManger

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True)  # enables high dpi scaling since I use a 4k monitor
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True)  # use high dpi icons


class AppWindow(qtw.QWidget, Ui_app_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filepath_browse_button.clicked.connect(self.set_filepath)
        self.submit_button.clicked.connect(self.on_submit)
        self.handler = DataManger()

# TODO - implement proper input validation for all form fields
    def set_filepath(self):
        import os
        default_path = os.path.join(os.path.expanduser('~'), 'Documents')
        filepath = qtw.QFileDialog.getOpenFileName(self, 'Load File', default_path, 'Comma Separated Values (*.csv)')
        print(filepath[0])
        self.filepath_field.setText(filepath[0])

    def on_submit(self):
        if self.filepath_field.text() == '' or self.data_type_dropdown.currentIndex() == -1 \
                or self.email_field.text() == '' or self.password_field.text() == '':
            qtw.QMessageBox.warning(self, 'All Fields Required',
                                    'Please make sure you have filled in every field before submitting!.')

        self.handler.set_filepath(self.filepath_field.text())
        self.handler.set_datatype(self.data_type_dropdown.currentText())
        self.handler.set_auth(self.email_field.text(), self.password_field.text())
        self.handler.set_payloads()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    view = AppWindow()
    view.show()
    sys.exit(app.exec_())
