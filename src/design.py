from PyQt4 import QtCore, QtGui, QtTest
from PyQt4.QtGui import *
from datetime import datetime
import pygame
from pygame import *
import threading 
import converter, modules

sequence = []

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Infor(object):
	def set_img(info, img):
    		info.img = img
	def set_temp(info, temp):
		info.temp = temp

class Ui_MainWindow(object):
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 640)
	self.showMaximized()

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
	self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 400, 131, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
	self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 400, 131, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 200, 1000, 70))

	self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(600, 60, 20, 600))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

	self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 500, 400, 100))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
	
	self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label"))
	self.label_3.hide()
	self.label_3.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        MainWindow.setMenuBar(self.menubar)        
	self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
	
	self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuArquivo"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionCarry_a_routine = QtGui.QAction(MainWindow)
        self.actionCarry_a_routine.setObjectName(_fromUtf8("actionCarry_a_routine"))
       
	self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCarry_a_routine)

        self.menubar.addAction(self.menuFile.menuAction())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
	QtCore.QObject.connect(self.actionCarry_a_routine, QtCore.SIGNAL(_fromUtf8("triggered()")), self.carryRoutine)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	f = open('../routine/default.txt','r')

    	self.lines = f.read().splitlines()
	
	
    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Iniciar", None))	
	
	self.pushButton_2.setText(_translate("MainWindow", "Iniciar", None))
	self.pushButton_2.clicked.connect(self.startKey)      
	
	self.label.setText(_translate("MainWindow", "Captura via LeapMotion			    Captura via Teclado", None))
        self.label_3.setText(_translate("MainWindow", "", None))
	
	self.menuFile.setTitle(_translate("MainWindow", "Arquivo", None))
        self.actionCarry_a_routine.setText(_translate("MainWindow", "Carregar uma rotina", None))
	
	
    def carryRoutine(self):
	fileNames = QFileDialog.getOpenFileNames(None, 'Open file', '.','Texto (*.txt)')
	for endfile in fileNames: print endfile
	f = open(str(endfile),'r')
	self.lines = f.read().splitlines()
	f.close()

    def readRoutine(self):
	global sequence
	for line in self.lines: 
		if len(line) != 0 and line[0]!='#':	
			atributo = line.split(';')
			imagem = str(atributo[0])
			temp = int(atributo[1])
			
			l = Infor()
			Infor.set_img(l, imagem)

			#image = mpimg.imread("../images/"+imagem+".png")
			#converter.gray_scale(image,"../images/"+imagem+"EC.png")

			#image = mpimg.imread("../images/"+imagem+".png")
			#converter.pattern(image,"../images/"+imagem+".png")

			Infor.set_temp(l, temp)
			sequence.append(l)

    def startLeap(self):
	self.start()

    def startKey(self):
	self.start()

    def start(self):
	self.readRoutine()
	global sequence
	modules.main(sequence)

