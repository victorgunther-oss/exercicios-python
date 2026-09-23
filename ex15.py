positivos = []

while True:
    numero = float(input('Digite um número: '))
    if(numero > 0):
        positivos.append(numero)
    elif(numero == 0):
        break

print(f'Foram digitados {len(positivos)} números positivos.')