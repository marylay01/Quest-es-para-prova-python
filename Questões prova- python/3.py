#Escreva um progama que calcule o imposto de renda a partir de um salário de um funcionário a partir de da tabela
#O programa deverá ao fim imprimir o valor do imposto devido, o salário bruto e o salário com desconto. O programa ainda deverá  se repe r até que o 
#usuário deseje encerra-lo.
while True:
   salário=float(input("Digite aqui o seu salário bruto:"))
   
   if salário>=1.500:
      SL= salário*0.95
      imp= salário*0.05
   elif 1.500 < salário <=3.000:
      SL= salário*0.92
      imp = salário*0.08
   elif 3.000<salário<=10.000:
     SL=salário*0.85
     imp = salário*0.15
   else: 
     SL=salário*0.85
     imp = salário*0.15
   print("seu salário bruto é de:", salário, ", seu salário líquido é de:", SL, "e seu imposto fica de:",imp)
   
   pergunta=input("você deseja continuar (sim ou não)")
   if pergunta=="nâo":
        break

      



   