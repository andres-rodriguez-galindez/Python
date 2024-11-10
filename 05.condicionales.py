#Comparando las variables o instrucciones valida si es verdadero o falso. Con eso se define si continua o termina la instruccion.
    #intrucción
        #Condicion
            #intruccion
    #Si no cumple la condicion
        #intruccion

#datos por teclado - input
tiempo = input("¿Como esta el clima hoy? (lluvia, sol o tormenta) ")

if tiempo=="lluvia":
    print("Se te recomienda usar sombrilla para la ", tiempo)
elif tiempo=="sol":
    print("llevate una gorra")
elif tiempo=="tormenta":
    print("No salga de casa")
else:
    print("Respuesta incorrecta")