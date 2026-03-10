def menu():
	menu=input("""


		Cafeteria AromaCampus
		1.Cafe con leche
		2.Cafe americano
		3.Cafe descafeinado""")
	match menu:
		case 1:
			print("Bienvenido el cafe con leche tiene un valor de 1500")
		case 2:
			print("Bienvenido el cafe ameriano tiene un valor de 3000")
		case 3:
			print("Bienvenido el cafe descafeinado tiene un valor de 5000")