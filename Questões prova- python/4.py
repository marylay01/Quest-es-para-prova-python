alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mensagem = input("Digite a mensagem a ser criptografada: ")
chave = int(input("Digite a chave de criptografia: "))
criptografia = []

for letra in mensagem:
    if letra in alfabeto: # Verifica se o caractere está no alfabeto
        for j in range(len(alfabeto)):
            if alfabeto[j] == letra:
                index = j
        if index >= 23:
            novo_index = (index + chave) - 25  # Desloca 3 posições no alfabeto, usando módulo para "circular"
        else: novo_index = (index + chave) 
        criptografia.append(alfabeto[novo_index])
    else:
        criptografia.append(letra)  # Mantém caracteres que não estão no alfabeto, como espaços

criptografado = ''.join(criptografia)
print("Mensagem criptografada:", criptografado)