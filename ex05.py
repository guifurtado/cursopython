



def quebra (line):
	size = len(line)
	vetor = []
	buffer = ""
	i = 0
	# quebra
	while i < size:

		lido = line[i]

		if lido == ",":

			vetor.append(buffer)
			buffer = ""

		else:

			buffer = buffer + lido	

		i = i + 1
	if buffer != "":
		vetor.append(buffer)

	return vetor				





#ler, se encontrar vírgula, jogar para uma variável
lin = []
desc= []

for n in range(5):

	line = input()
	if n == 0:
		continue;

	vetor = quebra(line)

	#print(vetor[2],vetor[4])

	lin.append (vetor[2])
	desc.append(vetor[4])

print(lin[2],desc[2])









