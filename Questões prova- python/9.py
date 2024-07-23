#Escreva um programa que recebe um CPF e verifica se ele é válido ou inválido.
cpf= input("Digite p cpf:")
primeiro_digito=0
segundo_digit0=0
soma=0 
soma2=0
 
 #calculando primeiro cpf 
for cont in range (10,1,-1):
    numero=cpf[10-cont]
    soma+=int(numero)*cont

if soma %11<2:
    primeiro_digito=0
else:
    primeiro_digito=11-(soma%11)

#calculando o segundo digito 
for cont in range (11,1,-1):
    numero=cpf[11-cont]
    soma2+=int(numero)*cont

if soma2%11<2:
    segundo_digit0=0
else:
    segundo_digit0=11-(soma2%11)

#verificando se o cpf é válido
if cpf[-2]==str(primeiro_digito) and cpf[-1]==str(segundo_digit0):
    print("CPF válido")
else:
    print("CPF inválido")


