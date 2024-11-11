#Tabla de multiplicar donde pasaremos el número de la tabla por teclado
#numero = int(input("Ingrese numero uno: "))
#numero2 = int(input("ingrese numero dos: "))
#for multiplicar in range(0,12):
#resultado = numero * numero2
#print(f"{numero} x {numero2} = {resultado}")

def tabla_multiplicar(tabla,limite):
    for i in range(0,limite):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")
tabla = int(input("Que tabla quieres saber. "))
tabla_multiplicar(tabla,11)


def table_multi(table,limit):
    for i in range(0,limit):
        result = table * i
    print(f"{table} x {i} = {result}")
table = int(input("Que tabla quieres multiplicar: "))
table_multi(table,11)
