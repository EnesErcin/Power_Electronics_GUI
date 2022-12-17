
from power_circuit_python import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
import ltspice
import numpy as np
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt, QRectF, QPointF, pyqtSignal, QObject
import ltspice_interface

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.WindowEvents()

    def WindowEvents(self):
        self.ui.pushButtonBJT.clicked.connect(self.bjtClicked)
        self.ui.pushButton_MOSFET.clicked.connect(self.mosfetClicked)
        self.ui.pushButton_Diode.clicked.connect(self.diodeClicked)
        self.ui.pushButton_Thyristor.clicked.connect(self.thyClicked)


    def bjtClicked(self):
        if self.ui.comboBox_BJT.currentText() == 'Graph':
            time_ref,vce,vbe,ic_current = ltspice_interface.extract_var("BJT")
            figure = Figure()
            scene = QtWidgets.QGraphicsScene()
            axes = figure.gca()
            axes.set_title('BJT')
            axes.set_xlabel('Vce(V)',loc= 'right')
            axes.set_ylabel("Ic(mA)",loc="top")
            axes.grid(True)

            dim = np.shape(ic_current)[0]
            for i in range (dim):
                axes.plot(vce[i], ic_current[i])

            canvas = FigureCanvas(figure)
            scene.addWidget(canvas)
            self.ui.graphicsView_graph.setScene(scene)
            scene.setSceneRect(35, 40, 541, 411)
            self.ui.graphicsView_graph.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.show()  

        elif self.ui.comboBox_BJT.currentText() == 'Circuit':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\circuit_images''\\BJT.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)

        elif self.ui.comboBox_BJT.currentText() == 'Info':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\BJT_INFO.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)

        else:
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\ref.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)
    
    def mosfetClicked(self):
        if self.ui.comboBox_MOSFET.currentText() == 'Graph':
            time_ref,vds,vgs,id_current     =  ltspice_interface.extract_var("MOSFET")
            figure = Figure()

            scene = QtWidgets.QGraphicsScene()
            axes = figure.gca()
            axes.set_title('MOSFET')
            axes.set_xlabel('Vds(V)',loc= 'right')
            axes.set_ylabel("Id(mA)",loc="top")
            axes.grid(True)

            dim = np.shape(id_current)[0]
            for i in range (dim):
                axes.plot(vds[i], id_current[i])

            canvas = FigureCanvas(figure)
            scene.addWidget(canvas)
            self.ui.graphicsView_graph.setScene(scene)
            scene.setSceneRect(35, 40, 541, 411)
            self.ui.graphicsView_graph.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.show()  

        elif self.ui.comboBox_MOSFET.currentText() == 'Circuit':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\circuit_images'+'\\MOSFET.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)

        elif self.ui.comboBox_MOSFET.currentText() == 'Info':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\MOSFET_INFO.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)           
        else:
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\ref.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)

    def diodeClicked(self):
        if self.ui.comboBox_Diode.currentText() == 'Graph':
            time_ref,vs,vo      =ltspice_interface.extract_var("DIODE")
            figure = Figure()
            scene = QtWidgets.QGraphicsScene()
            axes = figure.gca()
            axes.set_title('Didode')
            axes.set_xlabel('Vs(V)',loc= 'right')
            axes.set_ylabel("Vo(mA)",loc="top")
            axes.grid(True)
            axes.plot(time_ref, vo,vs)
            canvas = FigureCanvas(figure)
            scene.addWidget(canvas)
            self.ui.graphicsView_graph.setScene(scene)
            scene.setSceneRect(35, 40, 541, 411)
            self.ui.graphicsView_graph.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.show()

        elif self.ui.comboBox_Diode.currentText() == 'Circuit': 
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\circuit_images''\\DIODE.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)

        elif self.ui.comboBox_Diode.currentText() == 'Info':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\DIODE_INFO.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)
        else:
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\ref.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)
        
        self.ui.graphicsView_graph.show()
    def thyClicked(self):
        if self.ui.comboBox_Thyristor.currentText() == 'Graph':
            time_ref,vs,vo,delay_angle     = ltspice_interface.extract_var("THYRISTOR")
            figure = Figure()
            scene = QtWidgets.QGraphicsScene()
            axes = figure.gca()
            axes.set_title('THYRISTOR with a delay angle:   {}'.format(delay_angle))
            axes.set_xlabel('Vs(V)',loc= 'right')
            axes.set_ylabel("Vo(mA)",loc="top")
            axes.grid(True)
            axes.plot(time_ref, vo,vs)
            canvas = FigureCanvas(figure)
            scene.addWidget(canvas)
            self.ui.graphicsView_graph.setScene(scene)
            scene.setSceneRect(35, 40, 541, 411)
            self.ui.graphicsView_graph.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.show()
        elif self.ui.comboBox_Thyristor.currentText() == 'Circuit':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\circuit_images'+'\\THYRISTOR.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)
        elif self.ui.comboBox_Thyristor.currentText() == 'Info':
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\THYRISTOR_INFO.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)
        else:
            pix = QPixmap(os.path.dirname(__file__)+'\\Ltspice\\info_images'+'\\ref.png')
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.ui.graphicsView_graph.fitInView(item,Qt.KeepAspectRatio)
            self.ui.graphicsView_graph.setScene(scene)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=myWindow()
    window.show()
    sys.exit(app.exec())