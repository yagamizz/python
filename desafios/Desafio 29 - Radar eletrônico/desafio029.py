v = int(input('Quantos KMs/h? '))
multa = (v - 80) * 7
if v > 80:
    print(f'Você foi multado! A multa vai custar R$7.00 por cada KM ultrapassado acima do limite, ou seja: R${multa:.2f}')
