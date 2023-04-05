#En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compren. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco pero menos de diez se les otorga un 20% de descuento; y si son diez o más se les da un 40%. El precio de cada computadora es de $1.000.000


computer_number = int(input("enter the number of cumputers to buy: "))


if computer_number < 5:
  discount = 0.1
elif computer_number >= 5 and computer_number < 10:
  discount = 0.2
if computer_number  >= 10:
  discount = 0.4


total = computer_number * 1000000 - (computer_number * 1000000 * discount)


print(f"Total to pay: ${total} COP")