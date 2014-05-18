import sys
from PyQt4 import QtCore, QtGui

from black_rfid_reader import RFIDReader
from keyboard_alike import reader
from pyqt_ui import Ui_MainWindow


class ReadFromUSB(QtCore.QThread):
    def __init__(self, parent):
        super(ReadFromUSB, self).__init__(parent)
        self.parent = parent

    def run(self):
        try:
            self.parent.usb_read_value = self.parent.rfidreader.read().strip()
        except (reader.DeviceException, reader.ReadException) as e:
            self.parent.usb_exception = str(e)
            self.parent.usb_exception_counter += 1


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._set_initial_usb_values()

        self.rfidreader = RFIDReader(0x08ff, 0x0009, 84, 16, should_reset=False)
        self.rfidreader.initialize()

        self._start_reader_thread()

    def _set_initial_usb_values(self):
        self.usb_read_value = None
        self.usb_exception = None
        self.usb_exception_counter = 0

    def _start_reader_thread(self):
        thread = ReadFromUSB(self)
        thread.start()
        thread.finished.connect(self._receive_data)

    def _receive_data(self):
        if not self.usb_read_value:
            print('* Ups, no data')
        else:
            print(self.usb_read_value)
            self.ui.dataList.addItem(self.usb_read_value)
            self._set_initial_usb_values()

        if self.usb_exception_counter >= 3:
            print(self.usb_exception)
            self.rfidreader.disconnect()
            QtGui.QApplication.quit()
        else:
            if self.usb_exception:
                print(self.usb_exception)
                self.usb_exception = None
            self._start_reader_thread()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
