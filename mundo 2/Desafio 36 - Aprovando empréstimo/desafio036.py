valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = valorCasa / (anos * 12)
minimo = salario * 30 /100
if minimo >= prestacao:
    print(f'Para pagar uma casa de R${valorCasa} em {anos} anos a prestação será de R${prestacao:.2f} por mês.')
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m.')
else: 
    print(f'Para pagar uma casa de R${valorCasa} em {anos} anos a prestação será de R${prestacao:.2f} por mês.')
    print('Empréstimo \033[31mNEGADO\033[m.')
