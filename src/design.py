from PyQt4 import QtCore, QtGui, QtTest
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer
import time, string, os
import threading
from datetime import datetime
import keyboard

tempcap = 0.5
	
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

	self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 500, 600))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
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
	
	self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 1150, 200))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label"))
	self.label_4.hide()

	self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 650, 1000, 25))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
    	self.progressBar.hide()

	self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(350, 600, 500, 15))
        self.progressBar_2.setObjectName(_fromUtf8("progressBar"))
	self.progressBar_2.setFormat(_fromUtf8(""))
    	self.progressBar_2.hide()


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
	
	self.pushButton_2.setText(_translate("MainWindow", "Iniciar", None))
	self.pushButton_2.clicked.connect(self.startKey)      
	
	self.label.setText(_translate("MainWindow", "Captura via LeapMotion			    Captura via Teclado", None))
        self.label_3.setText(_translate("MainWindow", "", None))
	
	self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.actionCarregar_uma_programa.setText(_translate("MainWindow", "Carregar um programa", None))

    def contImg(self):
	i = 0
	for linha in self.lines:
		i = i + 1
	return i
	
    def start(self):

	self.qtdimg = self.contImg()
	self.line.hide()
	self.pushButton.hide()
	self.pushButton_2.hide()
	
	self.progressBar.show()	
        self.progressBar_2.show()	
        
    	self.readRoutine()
	
    def carrega(self):
	fileNames = QFileDialog.getOpenFileNames(None, 'Open file', '.','Texto (*.txt)')
	for endfile in fileNames: print endfile
	f = open(str(endfile),'r')
	self.lines = f.read().splitlines()

	f.close()

    def readRoutine(self):
	self.sequencia = []
	for linha in self.lines: 
		if len(linha) != 0 and linha[0]!='#':	
			atributo = linha.split(';')
			imagem = str(atributo[0])
			temp = int(atributo[1])
			
			l = Infor()
			Infor.set_img(l, imagem)
			Infor.set_temp(l, temp)
			self.sequencia.append(l)
	self.PrintScreen()


    def calculaSalto(self):
	
	return float(100.0/len(self.sequencia))
	
    def PrintScreen(self):
    	pos = 0.0
	self.label.hide()
	self.pushButton.hide()
	
	tamsalto = 0.0
	tamsalto = self.calculaSalto()
	
	for item in self.sequencia: #PERCORRE TODA A SAQUENCIA DE COMANDOS ARMAZENADA
		self.progressBar.setProperty("value", pos)
		pos += tamsalto
		self.label_2.show()
		self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":../images/"+item.img+".JPG\"/></p></body></html>", None))	

		cursor = float(25.0/item.temp)
		c = 0		
		while c <= 100:
			c += cursor
			self.progressBar_2.setProperty("value", c)
 			QtTest.QTest.qWait(250)

    def startLeap(self):

	self.start()

    def startKey(self):

	self.thingOne = ThreadOne()
    	self.thingOne.start()
	self.start()

class ThreadOne(threading.Thread):
    
    def run(self):
	
	arq = open('../routine/log.txt','a')
	now = datetime.now()
	nowS = str(now)
	date = str(nowS[0:19])

	arq.write("NOVA ROTINA -- "+str(date)+"\n\n")
	dt = 0

	while 1==1:
		arq = open('../routine/log.txt','a')
    		arq.write(str(dt)+";")

		if keyboard.is_pressed('space'):
			arq.write("100 ;")
		else :
			arq.write(" 0 ;")

		if keyboard.is_pressed('7'):
			arq.write(" 100 ;")
		else :
			arq.write(" 0 ;")

		if keyboard.is_pressed('8'):
			arq.write(" 100 ;")
		else :
			arq.write(" 0 ;")

		if keyboard.is_pressed('9'):
			arq.write(" 100 ;")
		else :
			arq.write(" 0 ;")

		if keyboard.is_pressed('0'):
			arq.write(" 100;\n")
		else :
			arq.write(" 0;\n")
 
		dt+=0.1
		global tempcap
		time.sleep(tempcap)#DEIXAR DE FACIL ACESSO PARA ALTERAR SE NECESSARIO

