class Ponto(object):
	x = 0
	y = 0

	def __str__(self):
		return (str(self.x) + "," + str(self.y)) 
		
	def soma(self,ponto_B):
		res = Ponto()
		res.x = self.x + ponto_B.x
		res.y = self.y + ponto_B.y

		return res

	def __init__(self, A = 0, B = 0):
		self.x = A
		self.y = B	

	def __mul__(self,ponto_B):
		raise BaseException ("nao implementa")	
		
p1 = Ponto(10,20)
p2 = Ponto(30,40)

try:
	p3 = p1 * p2
except BaseException as E:
	print("Vc fez merda",E)
	exit(1)
print(p3)
print(p1)