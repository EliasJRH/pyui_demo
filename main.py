from ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
    def slot1(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        self.ui.label.setText(fname[0])

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()