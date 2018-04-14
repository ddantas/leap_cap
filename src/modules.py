from PyQt4 import QtTest
from datetime import datetime
import pygame 
from pygame import *
import threading 

import converter

gameDisplay = 0


def keyCapture():
	
	global gameDisplay

	arq = open('../routine/log.txt','a')
	now = datetime.now()
	nowS = str(now)
	date = str(nowS[0:19])
	arq.write("NOVA ROTINA -- "+str(date)+"\n\n")

	dt = 0

	white = (255,255,255)
	black = (0,0,0)

	old_k_delay, old_k_interval = pygame.key.get_repeat()	
	pygame.key.set_repeat (500, 30)
	i = 0
	gameExit = False
	try:
		while not gameExit:
			
			for event in pygame.event.get():	
				arq = open('../routine/log.txt','a')
		    		arq.write(str(dt)+";")
						
				if event.type == pygame.QUIT:
					gameExit = True

				if pygame.key.get_pressed()[pygame.K_SPACE] != 0 :
					arq.write("100 ;")
					pygame.draw.rect(gameDisplay, black, [100,600,20,100])	
				else :
					arq.write(" 0 ;")
					pygame.draw.rect(gameDisplay, white, [100,600,20,99])
		

				if pygame.key.get_pressed()[pygame.K_7] != 0 :
					arq.write(" 100 ;")
					pygame.draw.rect(gameDisplay, black, [130,600,20,100])
			
				else :
					arq.write(" 0 ;")
					pygame.draw.rect(gameDisplay, white, [130,600,20,99])


				if pygame.key.get_pressed()[pygame.K_8] != 0 :
					arq.write(" 100 ;")
					pygame.draw.rect(gameDisplay, black, [160,600,20,100])							
				else :
					arq.write(" 0 ;")
					pygame.draw.rect(gameDisplay, white, [160,600,20,99])							

				if pygame.key.get_pressed()[pygame.K_9] != 0 :
					arq.write(" 100 ;")
					pygame.draw.rect(gameDisplay, black, [190,600,20,100])				
				else :
					arq.write(" 0 ;")
					pygame.draw.rect(gameDisplay, white, [190,600,20,99])							

 
				if pygame.key.get_pressed()[pygame.K_0] != 0 :
					arq.write(" 100;\n")				
					pygame.draw.rect(gameDisplay, black, [220,600,20,100])
				else :
					arq.write(" 0;\n")
					pygame.draw.rect(gameDisplay, white, [220,600,20,99])							

				pygame.display.update()
				
				dt+=0.1

	finally:
		pygame.key.set_repeat (old_k_delay, old_k_interval)
		

def printScreen(sequencia):		
	#global sequencia
	global gameDisplay
	tamMin = 50
	tamMax = 1200

	num_elementos_lista = len(sequencia)
	j = 0
	black = (0,0,0)

	white = (255,255,255)
	jump = (tamMax / num_elementos_lista) 
	porcent = 0
	
	try:
		while(j < num_elementos_lista):
	
			img1 = pygame.image.load("../images/"+sequencia[j].img+".png")
			gameDisplay.blit(img1,(10,30))
	   		pygame.display.update()
		
			img2 = pygame.image.load("../images/"+sequencia[j+1].img+"EC.png")
			gameDisplay.blit(img2,(160,-25))
	   		pygame.display.update()

			img3 = pygame.image.load("../images/"+sequencia[j+2].img+"EC.png")
			gameDisplay.blit(img3,(480,-25))
			pygame.display.update()

	
			img4 = pygame.image.load("../images/"+sequencia[j+3].img+"EC.png")
			gameDisplay.blit(img4,(800,-25))
			pygame.display.update()

			j = j + 1

			c = 0		
			por = 0
			qtdframes = 20
			aux = (300-15)/qtdframes
			while c <= qtdframes:
				pygame.draw.rect(gameDisplay, black, [15,410,por,10])			
				pygame.display.update()				
				por = por + aux
				QtTest.QTest.qWait(100)
				c = c + 1
			
			pygame.draw.rect(gameDisplay, white, [15,410,300,120])	
			pygame.display.update()
			
			pygame.draw.rect(gameDisplay, black, [50,430,porcent,10])
			pygame.display.update()
			
			porcent += jump

	finally:	
		pygame.quit()
	
	   #	sys.exit()

def main(sequencia):
	global gameDisplay
	pygame.init()
	white = (255,255,255)
	black = (0,0,0)
	gameDisplay = pygame.display.set_mode((1600,740))
	gameDisplay.fill(white)
        pygame.display.update()
	
	
	t1 = threadKey()
        t1.start()

	printScreen(sequencia)


class threadKey(threading.Thread):
 
    def run(self):
	#Ui_MainWindow().keyCapture()
	keyCapture()

