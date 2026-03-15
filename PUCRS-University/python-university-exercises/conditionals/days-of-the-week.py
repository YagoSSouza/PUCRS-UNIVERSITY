# Solicita ao usuário um número entre 1 e 7
dia = int(input("Digite um número (1-7): "))

# Verifica qual dia da semana corresponde ao número digitado
if dia == 1:
  print("Domingo")
elif dia == 2:
  print("Segunda")
elif dia == 3:
  print("Terça")
elif dia == 4:
  print("Quarta")
elif dia == 5:
  print("Quinta")
elif dia == 6:
  print("Sexta")
elif dia == 7:
  print("Sábado")
  
# Caso o número não esteja entre 1 e 7
else:
  print("Erro. Insira um valor no intervalo de 1-7")
