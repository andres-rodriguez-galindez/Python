#Sacar facturación media de tres empresas
total = 3 + 4 + 5
media = total / 3

print("La facturación media es de:", media)

total = 7 + 10 + 20
media = total / 3

print("La facturación media es de:", media)

def facturacion_media(empresa1, emnpresa2, empresa3):
     total = empresa1 + emnpresa2 + empresa3
     media = total / 3
     return media

resultado = facturacion_media(4,8,12)

print(resultado)
