class Turing (object):
	"""docstring for Turing"""

	def calc (self,raw):
		map = {}
		words = raw.split(' ')
		for item in words:
			if item in map:
				map[item] = map[item] + 1
			else:	
				map[item] = 1

		return map		




def main():

	conta_palavras = Turing()
	texto = input()
	map = conta_palavras.calc(texto)


	for key,val in map.items():
		print(key,val)

main()	
