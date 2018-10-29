import sqlite3

#name = input()
#idade = input()

db = sqlite3.connect("projeto.db")
c1 = db.cursor()

c1.execute("select * from users")
for item in c1.fetchall():
	print(item)
c1.close()

#db.commit()

