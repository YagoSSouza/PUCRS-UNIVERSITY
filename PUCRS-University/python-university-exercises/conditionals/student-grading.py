# Solicita ao usuário uma nota
nota = float(input("Digite a nota: "))

# Verifica se a nota está fora do intervalo válido
if nota > 10 or nota < 0:
  print("Valor inválido")

# Nota entre 9 e 10 → Conceito A
elif nota >= 9:
  print("Conceito A")

# Nota entre 7 e 8.9 → Conceito B
elif nota >= 7:
  print("Conceito B")

# Nota entre 5 e 6.9 → Conceito C
elif nota >= 5:
  print("Conceito C")

# Nota entre 3 e 4.9 → Conceito D
elif nota >= 3:
  print("Conceito D")

# Nota entre 0 e 2.9 → Conceito E
else:
  print("Conceito E")
