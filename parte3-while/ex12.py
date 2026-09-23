numeros = []

while True:
    numero = float(input('Digite um número: '))
    if(numero != 0):
        numeros.append(numero)
    else:
        break

print(sum(numeros))
