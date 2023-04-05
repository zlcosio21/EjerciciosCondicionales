#Un proveedor de estéreos ofrece un descuento del 10% sobre el precio sin IVA de algún aparato si este cuesta $200.000 o más. Además, independientemente de esto, ofrece un 5% de descuento si la marca es NOSY. Determinar cuánto pagará, con IVA incluído, un cliente cualquiera por la compra de su estéreo. El IVA es del 16%.


stereo = input("Enter the name stereo: ")
partial_total = int(input("Enter the total partial: "))


if partial_total >= 200000:
  iva = partial_total + (partial_total * 0.06)
  print(f"Total to pay is ${iva} COP")
elif stereo == "SONY":
  iva2 = partial_total + (partial_total * 0.11)
  print(f"Total to pay is ${iva2} COP")
else:
  print(f"There is no discount, the total to pay is ${partial_total} COP")