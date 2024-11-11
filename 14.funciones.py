def saludo (): #palabra recervada def
    print("Hola Amigo")
saludo()

def saludo(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

saludo("Rosario", "Rodriguez")
#saludo("Fernando", "Rodriguez")

def suma(numero1, numero2):
    total = numero1 + numero2
    print(f"La suma es:  {numero1} + {numero2} = {total}")
suma(1,3)
