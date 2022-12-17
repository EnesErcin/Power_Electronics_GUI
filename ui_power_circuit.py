# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_circuit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonBJT = QPushButton(self.centralwidget)
        self.pushButtonBJT.setObjectName(u"pushButtonBJT")
        self.pushButtonBJT.setGeometry(QRect(30, 90, 93, 61))
        self.pushButton_Thyristor = QPushButton(self.centralwidget)
        self.pushButton_Thyristor.setObjectName(u"pushButton_Thyristor")
        self.pushButton_Thyristor.setGeometry(QRect(30, 420, 93, 61))
        self.pushButton_Diode = QPushButton(self.centralwidget)
        self.pushButton_Diode.setObjectName(u"pushButton_Diode")
        self.pushButton_Diode.setGeometry(QRect(30, 310, 93, 61))
        self.pushButton_MOSFET = QPushButton(self.centralwidget)
        self.pushButton_MOSFET.setObjectName(u"pushButton_MOSFET")
        self.pushButton_MOSFET.setGeometry(QRect(30, 200, 93, 61))
        self.graphicsView_graph = QGraphicsView(self.centralwidget)
        self.graphicsView_graph.setObjectName(u"graphicsView_graph")
        self.graphicsView_graph.setGeometry(QRect(290, 20, 721, 551))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.graphicsView_graph.setFont(font)
        self.graphicsView_graph.setFrameShape(QFrame.StyledPanel)
        self.graphicsView_graph.setFrameShadow(QFrame.Plain)
        self.graphicsView_graph.setLineWidth(5)
        self.graphicsView_graph.setMidLineWidth(0)
        self.comboBox_BJT = QComboBox(self.centralwidget)
        self.comboBox_BJT.setObjectName(u"comboBox_BJT")
        self.comboBox_BJT.setGeometry(QRect(150, 110, 121, 22))
        self.comboBox_MOSFET = QComboBox(self.centralwidget)
        self.comboBox_MOSFET.setObjectName(u"comboBox_MOSFET")
        self.comboBox_MOSFET.setGeometry(QRect(150, 220, 121, 22))
        self.comboBox_Diode = QComboBox(self.centralwidget)
        self.comboBox_Diode.setObjectName(u"comboBox_Diode")
        self.comboBox_Diode.setGeometry(QRect(150, 330, 121, 22))
        self.comboBox_Thyristor = QComboBox(self.centralwidget)
        self.comboBox_Thyristor.setObjectName(u"comboBox_Thyristor")
        self.comboBox_Thyristor.setGeometry(QRect(150, 440, 121, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Power Circuit GUI", None))
        self.pushButtonBJT.setText(QCoreApplication.translate("MainWindow", u"BJT", None))
        self.pushButton_Thyristor.setText(QCoreApplication.translate("MainWindow", u"Thyristor", None))
        self.pushButton_Diode.setText(QCoreApplication.translate("MainWindow", u"Diode", None))
        self.pushButton_MOSFET.setText(QCoreApplication.translate("MainWindow", u"MOSFET", None))
    # retranslateUi

