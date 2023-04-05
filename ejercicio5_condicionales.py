#Recibir como entrada tres números diferentes e imprimir el número mayor de los tres.


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))


if num1 > num2 and num1 > num3:
  print(f"The largest number is {num1}")
elif num2 > num1 and num2 > num3:
  print(f"The largest number is {num2}")
elif num3 > num1 and num3 > num2:
  print(f"The largest number is {num3}")