#Em uma certificação são feitos 5 exames (I, II, III, IV e V). Escreva um 
#programa que leia as notas destes exames e imprima a classificação do aluno, 
#sabendo que a média é 7.0. 

ex1= (float(int(input("Nota do aluno:"))))
ex2= (float(int(input("Nota do aluno:"))))
ex3= (float(int(input("Nota do aluno:"))))
ex4= (float(int(input("Nota do aluno:"))))
ex5= (float(int(input("Nota do aluno:"))))

soma= (ex1+ex2+ex3+ex4+ex5)
media=(soma/5)
if media>=7.0:
        print("classificação A, você passou em todos os exames com média de:", media)
elif ex1 >= 7.0 and ex2 >= 7.0 and ex4 >= 7.0 and (ex3 < 7.0 or ex5 < 7.0):
        print("classificação B, passou no exame 1, 2 e 4, mas não em 3 ou 5 com média de:", media)
elif ex1 >= 7.0 and ex2 >= 7.0 and (ex3 >= 7.0 and ex4 >= 7.0) and ex5 < 7.0:
        print("classificação C, passou no exame 1, 2, 3 e 4, mas não em 5 com média de:", media)
else:
        print("Reprovado")
    
   


