class Pessoa(object):
	nome = "Guilherme"
	cpf = "010.073.349-24"

	def __str__(self):
		return("Pessoa: " + self.nome + "," + self.cpf)

class Usuario(Pessoa):
	email = "blabla@uol.com.br"
	password = "******"

	def __str__(self):
		A = Pessoa.__str__(self)
		return(A + " User: " + self.email + ", " + self.password)
		


class Admin(Usuario):
	funcao = ""		

p1 = Pessoa()
p2 = Pessoa()
p3 = Usuario()
vet =[p1, p2, p3]

print(vet[2])


		