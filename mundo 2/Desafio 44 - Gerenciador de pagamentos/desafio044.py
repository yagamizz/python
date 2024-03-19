print('========= LOJINHA DO JOHNNY =========')
compras = float(input('Valor gasto em compras: R$'))
print('FORMAS DE PAGAMENTOS')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    desconto = compras - (compras * 0.1)
    print(f'Sua compra de R${compras:.2f} vai custar R${desconto:.2f} no final.')
elif escolha == 2:
    desconto = compras - (compras * 0.05)
    print(f'Sua compra de R${compras:.2f} vai custar R${desconto:.2f} no final.')
elif escolha == 3:
    parcela = compras / 2
    print(f'Sua compra de R${compras:.2f} terá duas parcelas de R${parcela:.2f}')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas: '))
    juros_parcela = compras / parcelas
    juros_parcela1 = juros_parcela + (juros_parcela * 0.2)
    juros_total = compras + (compras * 0.2)
    print(f'Sua compra será parcelada em {parcelas}x de R${juros_parcela1:.2f} com JUROS.')
    print(f'Sua compra de R${compras:.2f} vai custar R${juros_total:.2f} no final.')
else:
    print('Entrada inválida, tente novamente.')
