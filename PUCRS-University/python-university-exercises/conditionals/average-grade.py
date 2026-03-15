n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))

if n1>=n2 and n1>=n3:
  media = (n1*5 + n2*2.5 + n3*2.5 / 10 )
elif n2>=n1 and n2>=n3:
  media = (n2*5 + n1*2.5 + n3*2.5 / 10)
elif n3>=n1 and n3>=n2:
  media = (n3*5 + n1*2.5 + n2*2.5 / 10)
print("A nota média é: ", media)