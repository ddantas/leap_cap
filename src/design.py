from PyQt4 import QtCore, QtGui, QtTest
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer
import time, string, os



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

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 640)
	self.showMaximized()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
	self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 500, 600))
        self.label_2.setObjectName(_fromUtf8("label_2"))        
	self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 290, 131, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 200, 561, 70))
	
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
	
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 650, 1000, 40))
	
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
	self.horizontalSlider.hide()
        
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
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCarregar_uma_programa = QtGui.QAction(MainWindow)
        self.actionCarregar_uma_programa.setObjectName(_fromUtf8("actionCarregar_uma_programa"))
       
	self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionCarregar_uma_programa)
        self.menubar.addAction(self.menuArquivo.menuAction())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
	QtCore.QObject.connect(self.actionCarregar_uma_programa, QtCore.SIGNAL(_fromUtf8("triggered()")), self.carrega)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	f = open('../routine/default.txt','r')

    	self.lines = f.read().splitlines()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Iniciar", None))
	self.pushButton.clicked.connect(self.start)        
	
	self.label.setText(_translate("MainWindow", "Clique em Iniciar para dar o inicio a captura", None))
        self.label_3.setText(_translate("MainWindow", "", None))
	
	self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.actionCarregar_uma_programa.setText(_translate("MainWindow", "Carregar um programa", None))
	
    def contImg(self):
	i = 0
	for linha in self.lines:
		i = i + 1
	return i

    def start(self):
	

	qtdimg = self.contImg()
	self.horizontalSlider.setMaximum(qtdimg-1)
	self.horizontalSlider.show()
    	self.img()
	    
    def carrega(self):
	fileNames = QFileDialog.getOpenFileNames(None, 'Open file', '.','Texto (*.txt)')
	for endfile in fileNames: print endfile
	f = open(str(endfile),'r')
	#self.lines = f.readlines()
	self.lines = f.read().splitlines()
	#self.qtd = self.qtdImg()

	f.close()

    def img(self):
	pos = 0
	
	for linha in self.lines:
		#if (linha[0] >= 'a' and linha[0] <='z') or (linha[0] >= 1 and linha[0] <= 9):
		if len(linha) == 0 or linha[0]=='#':	
			print "PULA"
		else:
			atributo = linha.split(';')
			imagem = str(atributo[0])
			#print imagem
			temp = int(atributo[1])
			temp = temp * 1000
			#print temp
		
			self.label.hide()
			self.pushButton.hide()
			self.label_3.show()
			self.horizontalSlider.setValue(pos)
			pos = pos+1
			self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":../images/"+imagem+".JPG\"/></p></body></html>", None))
			QtTest.QTest.qWait(temp)

