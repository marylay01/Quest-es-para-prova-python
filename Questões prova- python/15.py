# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
km=float(int(input ("Digite os quilômetros rodados:")))
dias= int(input("Digite a quantidade de dias:"))

valorK= (km*0.20)
valorD= (dias*90)

total= (valorK+valorD)
print("O total a pagar pelo serviço é:", total) 