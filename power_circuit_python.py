# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alper/OneDrive/Masaüstü/python/elk107gui/power_circuit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonBJT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBJT.setGeometry(QtCore.QRect(30, 90, 93, 61))
        self.pushButtonBJT.setObjectName("pushButtonBJT")
        self.pushButton_Thyristor = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Thyristor.setGeometry(QtCore.QRect(30, 420, 93, 61))
        self.pushButton_Thyristor.setObjectName("pushButton_Thyristor")
        self.pushButton_Diode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Diode.setGeometry(QtCore.QRect(30, 310, 93, 61))
        self.pushButton_Diode.setObjectName("pushButton_Diode")
        self.pushButton_MOSFET = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MOSFET.setGeometry(QtCore.QRect(30, 200, 93, 61))
        self.pushButton_MOSFET.setObjectName("pushButton_MOSFET")
        self.graphicsView_graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_graph.setGeometry(QtCore.QRect(290, 20, 721, 551))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.graphicsView_graph.setFont(font)
        self.graphicsView_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphicsView_graph.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView_graph.setLineWidth(5)
        self.graphicsView_graph.setMidLineWidth(0)
        self.graphicsView_graph.setObjectName("graphicsView_graph")
        combobox_liste = ['Graph','Circuit','Info','References']
        self.comboBox_BJT = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_BJT.setGeometry(QtCore.QRect(150, 110, 121, 22))
        self.comboBox_BJT.setObjectName("comboBox_BJT")
        self.comboBox_BJT.addItems(combobox_liste)
        self.comboBox_MOSFET = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_MOSFET.setGeometry(QtCore.QRect(150, 220, 121, 22))
        self.comboBox_MOSFET.setObjectName("comboBox_MOSFET")
        self.comboBox_MOSFET.addItems(combobox_liste)
        self.comboBox_Diode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Diode.setGeometry(QtCore.QRect(150, 330, 121, 22))
        self.comboBox_Diode.setObjectName("comboBox_Diode")
        self.comboBox_Diode.addItems(combobox_liste)
        self.comboBox_Thyristor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Thyristor.setGeometry(QtCore.QRect(150, 440, 121, 22))
        self.comboBox_Thyristor.setObjectName("comboBox_Thyristor")
        self.comboBox_Thyristor.addItems(combobox_liste)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Power Circuit GUI"))
        self.pushButtonBJT.setText(_translate("MainWindow", "BJT"))
        self.pushButton_Thyristor.setText(_translate("MainWindow", "Thyristor"))
        self.pushButton_Diode.setText(_translate("MainWindow", "Diode"))
        self.pushButton_MOSFET.setText(_translate("MainWindow", "MOSFET"))

