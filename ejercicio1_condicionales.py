#En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compren. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco pero menos de diez se les otorga un 20% de descuento; y si son diez o más se les da un 40%. El precio de cada computadora es de $1.000.000

num_computadoras = int(input("Ingrese el numero de computadoras a comprar: "))

if num_computadoras < 5:
  descuento = 0.90
elif num_computadoras >= 5 and num_computadoras < 10:
  descuento = 0.80
elif num_computadoras  >= 10:
  descuento = 0.60

total = num_computadoras * 1000000 * descuento

print(f"Total a pagar: ${total:,} COP")
