#Escreva um programa que cria uma lista de duas dimensões utilizando List 
#Comprehsion e imprima a diagonal principal desta lista.
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dp = [lista[i][i] for i in range(len(lista))]
print(dp)