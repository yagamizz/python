d = int(input ('quantos dias alugados? '))
km = float(input ('quantos KMs rodados? '))
vt = (d * 60) + (km * 0.15)
print(f'o total a pagar é R${vt:.2f}')
