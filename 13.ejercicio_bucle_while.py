#Adivine el número
#Función Randon
import random

print("!Bienvenido al juego de adivina el número")
print("!Trata de adivinar entre el 1 al 100")

numero_secreto = random.randint(0,100)

adivinado = False

while not adivinado:
    numero_usuario = int(input("Ingresa un numero:  "))

    if (numero_usuario == numero_secreto):
        print("Felicidades haz acetado")
        adivinado= True
    elif numero_usuario < numero_secreto:
        print("El número secreto es mas alto")
    else:
        print("El número secreto es mas bajo")
