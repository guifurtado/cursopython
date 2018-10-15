ant=1
cur=1
i=0
n = int(input()) - 2
while i<n:

	num = ant+cur
	razao = num/cur
	print(num, razao)

	ant = cur
	cur = num
	i+=1