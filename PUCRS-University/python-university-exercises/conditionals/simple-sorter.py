# Solicita três valores ao usuário
v1 = int(input("Insira o primeiro valor "))
v2 = int(input("Insira o segundo valor "))
v3 = int(input("Insira o terceiro valor "))

# Assume inicialmente que o maior valor é v1
maior = v1
# Verifica se v2 é maior que o atual maior
if v2 > maior : maior = v2
  
# Verifica se v3 é maior que o atual maior
if v3 > maior : maior = v3

# Assume inicialmente que o menor valor é v1
menor = v1
# Verifica se v2 é menor que o atual menor
if v2 < menor : menor = v2
  
# Verifica se v3 é menor que o atual menor
if v3 < menor : menor = v3

# Calcula o valor do meio usando a soma total menos o maior e o menor
meio = v1 + v2 + v3 - maior - menor

# Exibe os valores em ordem crescente
print("Ordem Crescente: ", menor, meio, maior)
# Exibe os valores em ordem decrescente
print("Ordem Decrescente: ", maior, meio, menor)
