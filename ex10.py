import numpy as np
import cv2

class Factory (object):

	"""docstring for factory """

	def __init__(self, arquivo):
		self.texture = cv2.imread(arquivo)

	def build(self):
		return Personagem(self)




class Personagem(object):

	x = 200
	y = 200

	"""docstring for ClassName"""

	def __init__(self, factory):

		self.ff = factory

	def draw(self,tela):
		qn = self.ff.texture[102:208,71+109*0:179+109*0]

		tela[300:406,400:508] = qn			

def main():
	
	factory = Factory("guerrilha.jpg")


	p1 = factory.build()

	cenario = cv2.imread("deserto.jpg")
	x = 100
	y = 100

	while True:

		tela = cenario[y+0:y+768,x+0:x+1024].copy()

		p1.draw(tela)
		cv2.imshow("janela A", tela)
		
		key = cv2.waitKey(1000)

		if key == 97: 
			if x > 10:
				x = x - 10		
		elif key == 115:
			y = y + 10
		elif key == 119:
			if y > 10:
				y = y - 10
		elif key == 100:
			x = x + 10	



print ("__init__")

main()