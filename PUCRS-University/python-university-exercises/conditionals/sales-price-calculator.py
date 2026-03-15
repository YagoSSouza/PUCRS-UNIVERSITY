preco = float(input("Digite o preço do produto: "))
if preco < 0 :
  print("Preço inválido")
else:
  if preco < 10 : venda = preco + preco * 0.7
  if preco > 10 and preco < 30 : venda = preco + preco * 0.5
  if preco > 30 and preco < 50 : venda = preco + preco * 0.4
  if preco >= 50 : venda = preco + preco * 0.3
  print("Preço de venda: ", venda)