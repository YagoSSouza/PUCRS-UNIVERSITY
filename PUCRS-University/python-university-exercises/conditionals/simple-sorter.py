v1 = int(input("Insira o primeiro valor "))
v2 = int(input("Insira o segundo valor "))
v3 = int(input("Insira o terceiro valor "))

maior = v1
if v2 > maior : maior = v2
if v3 > maior : maior = v3

menor = v1
if v2 < menor : menor = v2
if v3 < menor : menor = v3

meio = v1 + v2 + v3 - maior - menor
print("Ordem Crescente: ", menor, meio, maior)
print("Ordem Decrescente: ", maior, meio, menor)