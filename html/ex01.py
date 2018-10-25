import yaml

fd = open("./schedules.yaml","r")

texto = fd.read()
fd.close()

data = yaml.load(texto)

rooms = {}

for linha in data["schedules"]:

	if "assigned" in linha:
		sala = linha["assigned"]

		if sala in rooms:
			pass
		else:
			rooms[sala] = 1

res = {}

for sala_nome,val in rooms.items():

	out = []

	for linha in data["schedules"]:
		if "assigned" in linha and linha["assigned"] == sala_nome:
			out.append(linha)

	res[sala_nome] = out


texto = "<table class=table>"

for sala_nome,val in res.items():
	texto = texto + "<tr><td>{}</td> <td>{}</td></tr>".format(sala_nome,len(val))
texto += "</table>"


fs = open("./index.html","r")
template = fs.read()
fs.close()


saida = template.replace("YIELD", texto)
print(saida)
