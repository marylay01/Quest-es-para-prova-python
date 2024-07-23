# Construa um algoritmo que, tendo como dados de entrada dois pontos 
#quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles atraves da fórmula 
x1=float(input("Digite um valor:"))
y1=float(input("Digite um valor:"))
x2=float(input("Digite um valor:"))
y2=float(input("Digite um valor:"))

distancia= (((x2-x1)**2) + ((y2-y1)**2))**1/2
print(distancia)
