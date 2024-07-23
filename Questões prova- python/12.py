# Faça um algoritmo que leia o saldo 
# do crédito de um cliente e calcule o valor do crédito de acordo com a tabela 

saldo=float(input("Digite seu saldo aqui:"))
credito= 0
for i in range (5):
    if 0<saldo<=200:
        c1=credito+saldo   #não teve nenhum crédito
    elif 201<saldo<=400:
        c2= (saldo*0.2) 
        credito+=c2
    elif  401<=saldo<=600:
        c3=(saldo*0.6)  
        credito+=c3
    else: 
        c4= (saldo*0.4)
        credito+=c4
print("O seu saldo médio foi de:", saldo, "e o seu crédito foi de",credito)
