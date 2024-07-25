#Escreva um programa que leia o índice pluviométrico de cada dia do mês de 
#junho e informe o dia que mais choveu, o dia que menos choveu e as médias 
#pluviométricas de cada uma das duas quinzenas. 
soma1=0
soma2=0
ip = []
for i in range (1,31):
    junho = int (input(f"Digite o índice pluviométrico do dia {i}/06: "))
    if i <= 15:
        soma1+=junho
    else:
        soma2+=junho
    media=soma1/15
    media2=soma2/15 
    ip.append(junho)
    max = ip[0]
    min = ip[0]
    for j in ip:
        if j > max:
            max=j
        elif j < min:
            min=j

for k in range(len(ip)):
    if ip[k] == max:
        print(f"A data {k+1}/06 teve o maior indice de chuva.")
        break 
for l in range(len(ip)):
    if ip[l] == min:
        print(f"A data {l+1}/06 teve o menor indice de chuva.")
        break 
       
print(f"A média pluviométrica dos dias 1 a 15/06  é {media}.")
print(f"A média pluviométrica dos dias 16 a 30/06 é {media2}")