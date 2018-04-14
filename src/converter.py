import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb_to_gray(img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img

        for i in range(3):
           grayImage[:,:,i] = Avg

        return grayImage       

#image = mpimg.imread("imagem.png") 

def atributed(img):
	patternImage = np.zeros(img.shape)

        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        patternImage = img

	return patternImage  

def pattern(image, localSave):

	"""
	plt.imshow(image)
	plt.show()
	plt . xticks ([]),  plt . yticks ([]) 
	plt.rcParams['figure.figsize'] = (9,5)
	plt.savefig(localSave,  transparent = True)"""

	N = 10
	x = np.random.rand(N)
	y = np.random.rand(N)
	area = np.pi * (15 * np.random.rand(N))**2
	plt.imshow(image)
	fig = plt.figure(figsize=(18, 18))
	plt.scatter(x, y, s=area, alpha=0.5)
	fig.savefig(localSave, dpi = 100)

def gray_scale(image, localSave):
	grayImage = rgb_to_gray(image)  
	plt.imshow(grayImage)

	#plt.show()
	plt . xticks ([]),  plt . yticks ([]) 
	#plt.rcParams['figure.figsize'] = (9,5)
	plt.savefig(localSave,  transparent = True)

   
