print("Bem vindo a consulta de anagramas. Favor inserir abaixo as palavras a serem consultadas.")
palavra1 = str(input("Informe a primeira palavra: "))
palavra2 = str(input("Informe a segunda palavra: "))

def anagrama(palavra1, palavra2):
    lista1 = list(palavra1)  # Separando as letras contidas na palavra.
    lista2 = list(palavra2)

    lista1.sort()  # Organizando as letras em ordem alfabetica.
    lista2.sort()

    pos = 0
    igual = True

    while pos < len(palavra1) and igual:
        if lista1[pos] == lista2[pos]:  # Caso as letras na posição "pos" forem iguais, ele pulará para a próxima.
            pos = pos + 1
        else:
            igual = False # Caso as letras forem diferentes, o loop é encerrado e retorna "False".
    return igual

print(anagrama(palavra1, palavra2))
