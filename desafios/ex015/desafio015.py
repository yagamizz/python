d = int(input('quantos dias alugados? '))
km = float(input('quantos KMs rodados? '))
vt = (d * 60) + (km * 0.15)
print(f'o valor total a ser pago é de R${vt:.2f}')
