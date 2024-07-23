#Escreva um programa que cria uma lista de duas dimensões utilizando List 
#Comprehsion e imprima a diagonal principal desta lista.
a =[[int(input(f"digite um número:")) for j in range (3)] for i in range (3)]
dp=[]
for i in range (3):
    for j in range (3):
        if i==j:
            d=a[i][j]
            dp.append(d)
print( f"a diagonal principal é: {dp}")