alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
mensagem=input("Digite a mensagem:") 
chave=int(input("Digite a chave:"))
mc= ""

for letra in mensagem:
    inicio=0
    fim=len(alfabeto)-1
    meio=(inicio+fim)//2
    while inicio<=fim and alfabeto(meio)!=letra:
        if letra<alfabeto[meio]:
            fim=meio-1
        else: 
            inicio=meio+1
        meio=(inicio+fim)//2
    if alfabeto[meio]==letra:
        codigo = meio+chave
        if codigo>25:
            codigo=codigo-26
        mc==alfabeto[codigo]
print("Mensagem criptografada", mc)