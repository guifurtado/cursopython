import numpy as np
import cv2
import math as m



y = 300 
x = 400
tela = np.zeros((600,800,3), np.uint8)
cv2.circle(tela, (x,y), 20, (255,0,0), -1)


while True:
	x = 0
	for i in range(500):

		tela = np.zeros((600,800,3), np.uint8)

		# x = x + 1
		# y = int(  iy + m.sin(i*3.141592/180)*50 )

		cv2.circle(tela,(x,y), 20, (255,0,0), -1)
		cv2.imshow("tela", tela)
		key = cv2.waitKey(20)
		print(key)

		if key == 97: 
			x = x - 10  
		elif key == 115:
			y = y + 10
		elif key == 119:
			y = y - 10
		elif key == 100:
			x = x + 10	



