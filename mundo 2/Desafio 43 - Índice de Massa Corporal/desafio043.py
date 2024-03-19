peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print(f'seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Abaixo do normal, procure um médico.')
elif imc >= 18.6 and imc <= 24.9:
    print('Parabéns pelo seu peso estar dentro do ideal!')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso, procure um médico.')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau 1, procure um médico.')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau 2, procure um médico.')
else:
    print('Obesidade Grau 3, procure um médico.')
