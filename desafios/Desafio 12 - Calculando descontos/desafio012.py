valor = float(input('digite o preço do produto: R$'))
desconto = valor - (valor * 5 / 100)
print(f'com um desconto de 5%, o valor do produto que era de R${valor} passa a ser de R${desconto:.2f}!')
