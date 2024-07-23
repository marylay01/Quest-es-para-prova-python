#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% 
#ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 
#2% ao ano, escreva um programa, que imprima o tempo necessário para que a 
#população do país A ultrapasse a população do país B. 
popa= 5000000
popb= 7000000
cont=0
while popa < popb:
    popa= popa + (popa*0.03)
    popb= popb + (popb*0.02)
    cont+=1
print("a população A vai ultrapassar a população B em", cont, "anos")