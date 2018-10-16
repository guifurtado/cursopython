continuar = "s"
while continuar == "s":

	print("Digite o primeiro número: ")
	n1 = int(input())
	print("Digite o segundo número: ")
	n2 = int(input())

	print("Qual o símbolo da operação você deseja fazer?")
	operacao = input()

	if(operacao == "+"):
		res = (n1 + n2)
		
	elif(operacao == "-"):
		res = (n1 - n2)

	elif(operacao == "x"):
		res = (n1 * n2)
		
	print(res)

	print("Deseja efetuar outra operação?(s/n)")
	continuar = input()
