#Escreva um programa que leia o índice pluviométrico de cada dia do mês de 
#junho e informe o dia que mais choveu, o dia que menos choveu e as médias 
#pluviométricas de cada uma das duas quinzenas. 
dias = 30
pluvio = []
for i in range(dias):
    pluvio.append(float(input(f"Digite a pluviosidade do dia {i + 1} de junho: ")))
max_pluvio = pluvio[0]
min_pluvio = pluvio[0]
dia_mais_chuvoso = 1
dia_menos_chuvoso = 1

for i in range(1, dias):
    if pluvio[i] > max_pluvio:
        max_pluvio = pluvio[i]
        dia_mais_chuvoso = i + 1
    if pluvio[i] < min_pluvio:
        min_pluvio = pluvio[i]
        dia_menos_chuvoso = i + 1

quinzena1 = 0
quinzena2 = 0

for i in range(15):
  quinzena1 += pluvio[i]

for i in range(15, dias):
   quinzena2 += pluvio[i]

media_primeira_quinzena = quinzena1/ 15
media_segunda_quinzena =   quinzena2/ 15

# Exibindo os resultados
print(f"O dia que mais choveu foi o dia {dia_mais_chuvoso} com {max_pluvio}mm")
print(f"O dia que menos choveu foi o dia {dia_menos_chuvoso} com {min_pluvio}mm")
print(f"Média pluviométrica da primeira quinzena: {media_primeira_quinzena:.2f}mm")
print(f"Média pluviométrica da segunda quinzena: {media_segunda_quinzena:.2f}mm")