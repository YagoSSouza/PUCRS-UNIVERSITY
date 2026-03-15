nota = float(input("Digite a nota: "))
if nota > 10 or nota < 0 :
  print("Valor inválido")
elif nota >= 9 and nota <= 10 :
  print("Conceito A")
elif nota >= 7 and nota < 8.9 :
  print("Conceito B")
elif nota >= 5 and nota < 6.9 :
  print("Conceito C")
elif nota >= 3 and nota < 4.9 :
  print("Conceito D")
elif nota <= 3 and nota >= 0 :
  print("Conceito E")