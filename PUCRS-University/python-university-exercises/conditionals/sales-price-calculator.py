# Solicita ao usuário o preço do produto
preco = float(input("Digite o preço do produto: "))
# Verifica se o preço é inválido (negativo)
if preco < 0 :
  print("Preço inválido")
else:
  # Se o preço estiver entre 10 e 30, adiciona 50% de lucro
  if preco < 10 : venda = preco + preco * 0.7

  # Se o preço estiver entre 10 e 30, adiciona 50% de lucro
  elif preco < 30 : venda = preco + preco * 0.5
    
  # Se o preço estiver entre 30 e 50, adiciona 40% de lucro
  elif preco < 50 : venda = preco + preco * 0.4
    
  # Se o preço for 50 ou mais, adiciona 30% de lucro
  else:
    venda = preco + preco * 0.3

  # Exibe o preço final de venda
  print("Preço de venda: ", venda)
