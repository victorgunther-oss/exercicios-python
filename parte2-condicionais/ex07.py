numero1 = float(input("Digite seu primeiro numero: "))
numero2 = float(input("Digite seu segundo numero: "))

if (numero1 > numero2):
    print(f'{numero1} é maior que {numero2}')
elif (numero2 > numero1):
    print(f'{numero2} é maior que {numero1}')
else:
    print(f'{numero1} é igual a {numero2}')