# tenho que fazer um programa que gera uma lista dos números primos 
# existentes entre 1 e um número inteiro informado pelo usuário.

num=int(input("Digite um número:"))
lista=[]

for i in range (1, num):
    for j in range (2, i):
        if i%j==0:
            break
    else: 
        lista.append(i)
print(lista)