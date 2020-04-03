from pdfminer.pdfinterp import *
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

def read_pdf(pdf):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 獲取所有行
    lines = str(content).split("\n")
    lines = [i for i in lines if i]
    # 去除空格沒字串的地方
    print(lines)
    return lines


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.find_dir_btn = QtWidgets.QPushButton(self)
        self.find_dir_btn.setText('Choose  PDF ')
        self.find_dir_btn.setGeometry(QtCore.QRect(140, 220, 200, 80))
        self.find_dir_btn.move(64, 32)
        self.find_dir_btn.clicked.connect(self.open_pdf)

    def get_address_and_type(self):
        file_address, file_type = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "Your query", "PDF Files (*.pdf);;TXT Files (*.txt)")
        print(file_address, file_type)
        return file_address, file_type

    def open_pdf(self):
        file_address, file_type = self.get_address_and_type()
        if file_type == 'PDF Files (*.pdf)':
            my_pdf = open(file_address, "rb")
            read_pdf(my_pdf)
            my_pdf.close()

    def open_txt(self):
        file_address, file_type = self.get_address_and_type()
        if file_type == 'TXT Files (*.txt)':
            my_txt = open(file_address, 'r').read()
            for i in my_txt:
                print(i)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setGeometry(50, 50, 320, 200)
    window.setWindowTitle("Find Pdf")
    window.show()
    sys.exit(app.exec_())
