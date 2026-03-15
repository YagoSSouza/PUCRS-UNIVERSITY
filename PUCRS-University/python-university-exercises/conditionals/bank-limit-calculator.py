saldo = float(input("Valor do saldo: "))
if saldo<500:
  print("Não há limite")
elif saldo>=500 and  saldo<1000: 
  limite = saldo*0.08
  print(f"Seu limite é de 8%: R${limite:.2f}" )
else:
  limite = saldo*0.15
  print(f"Seu limite é de 15%: R${limite:.2f}" )