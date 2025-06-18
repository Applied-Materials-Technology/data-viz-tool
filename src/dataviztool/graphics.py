import pyvista as pv
import pyvistaqt as pvqt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from ex_logger import *
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyVista QT Integration')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout) 

        self.plotter = pvqt.QtInteractor(self)
        layout.addWidget(self.plotter.interactor)

        self.plotter.add_mesh(pv.Sphere())
        self.plotter.show_grid()

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()"""


logger.debug('This is a debug message')