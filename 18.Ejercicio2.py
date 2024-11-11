#Ejercicio: Calculo de precio total de una compra

#Supongamos que estas trabajando en una pequeña empresa que vende productos y necesitas crear un programa que calcule el precio total de una compra
#Incluyendo el impuesto sobre la venta
#El programa debera solicitar al usuario el nombre del producto, la cantidad y el precio unitario del producto
#Luego calculara el precio total y mostrara un resumen de la compra. 

#nombrepro = str(input("Ingrese el nombre del producto: "))
#precio = int(input("Cual es el valor del producto: "))
#cantidad = int(input("Ingrese la cantidad: "))
#impuesto = 0.19
#operacion = precio * cantidad
#total = operacion * impuesto
#print(f"El produco {nombrepro} debe pagar {total}")

def calcular_precio_total(cantidad, preciounitario):
    #Calcular el precio total de la compra
    precio_total = cantidad * preciounitario
    return precio_total

def main():
    print("Bienvenido a tu tienda")
nombre_producto = input("ingresa el nombre del producto: ")
cantidad = int(input("Ingresa la cantidad comprada: "))
preciounitario = float(input("ingrese el precio unitario: "))

if cantidad <= 0 or preciounitario <=0:
    print("El importe introducido no es correcto")
else:
    precio_total = calcular_precio_total(cantidad,preciounitario)
    impuesto_ventas = precio_total * 0.21
    precio_total_con_impuesto = precio_total + impuesto_ventas

    print("Resumen de la compra: ")
    print(f"Producto: {nombre_producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio Unitario: {preciounitario:.2f} $")
    print(f"Precio total: {precio_total:.2f} $")
    print(f"IVA (9%): {impuesto_ventas:.2f} $")
    print(f"Total con impuestos: {precio_total_con_impuesto:.2f} $")

main()