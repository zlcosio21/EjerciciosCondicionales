#Recibir como entrada dos números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste, y si es el segundo es mayor que el primero que los sume.


num1 = int(input("Enter a number: "))
num2 = int(input("Enter other number: "))


if num1 == num2:
  multiply = (num1 * num2)
  print(f"The result is {multiply}")
elif num1 > num2:
  subtract = (num1 - num2) 
  print(f"The result is {subtract}")
elif num1 < num2:
  add = (num1 + num2)
  print(f"The result is {add}")