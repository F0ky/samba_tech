par = []
impar = []

for i in range(8): # Inserindo valores dentro dos vetores.
    n = int(input("Insira um número: "))
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)

for c in range(len(par)): # Ordenando os valores peres em ordem decressente.
    for x in range(1, len(par) - c):
        if par[x] > par[x - 1]:
            par[x], par[x - 1] = par[x - 1], par[x]

for c in range(len(impar)): # Ordenando os valores ímpares em ordem crescente.
    for x in range(1, len(impar) - c):
        if impar[x] < impar[x - 1]:
            impar[x], impar[x - 1] = impar[x - 1], impar[x]

num = par + impar # Concatenando os dois vetores para exibir o resultado.
print(num)
