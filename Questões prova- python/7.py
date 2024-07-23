#Escreva um programa em python que leia um lista de 20 inteiros, calcule e 
#imprima: 
#a. A moda dos elementos na lista (elemento mais freqüente). 
#b. A mediana dos elementos no array (elemento central) 
#c. A média. 
a=[]
soma=0
for i in range(21):
    n=int(input("Digite uma valor para a lista: "))
    a.append(n)
    soma+=n

        #calculo da moda    
x=a[0]
for j in range(0, len(a)):
    if a[j]==a[j-1]:
        x=a[j]
        #calculo da mediana 
        for k in range(i+1, len(a)):
            if a[i]>a[j]:
                a[i], a[j] = a[j], a[i]
                
soma+=a[i]
media= soma/20
moda=x
mediana=a[9]
print("a moda dos números é: ", moda)
print("a média dos números é: ", media)
print("a mediana dos números é: ", mediana)


