#Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma 
#pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo 
#com a tabela

kg=float(input("diga-nos seu peso:"))
h=float(input("diga-nos sua altura:"))
IMC= kg / (h)**2

if IMC<18.5:
    print("Você está abaixo do peso! Seu IMC é de:", IMC)

elif 18.6 < IMC < 24.9:
    print("Parabéns, você está em peso ideal! Seu IMC é de:", IMC)
elif 25.0<IMC<29.9:
    print("você está levemente acima do peso! Seu IMC é de:", IMC)
elif 30.0 < IMC<34.9:
    print("Você está com obesidade grau I! Seu IMC é de:", IMC)
elif 35.0<IMC<39.9:
    print("Você está com obesidade grau II(SEVERA)! Seu IMC é de:", IMC)
else:
   print("Você está com obesidade grau IIi(MÓRBIDA)! Seu IMC é de:", IMC)


