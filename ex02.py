n1 = int( input ("nota 1: "))
n2 = int( input ("nota 2: "))
while n1>=0 and n2>=0:
	
	media = (n1+n2)/2

	if media < 5:
		print ("Reprovado")
	elif media < 7:
		print ("Final")
	else:
		print ("Aprovado")	
		
	n1 = int( input ("nota 1: "))
	n2 = int( input ("nota 2: "))	