# Solicita ao usuário o valor do saldo da conta
saldo = float(input("Valor do saldo: "))
# Verifica se o saldo é menor que 500
if saldo<500:
  # Nesse caso, não há limite disponível
  print("Não há limite")
  
# Verifica se o saldo está entre 500 e 999.99
elif saldo>=500 and  saldo<1000: 
  # Calcula 8% do saldo como limite
  limite = saldo*0.08
  print(f"Seu limite é de 8%: R${limite:.2f}" )

# Caso o saldo seja 1000 ou mais
else:
  # Calcula 15% do saldo como limite
  limite = saldo*0.15
  print(f"Seu limite é de 15%: R${limite:.2f}" )
