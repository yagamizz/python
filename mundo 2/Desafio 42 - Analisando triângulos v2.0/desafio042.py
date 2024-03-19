l1 = int(input('Primeiro segmento: '))
l2 = int(input('Segundo segmento: '))
l3 = int(input('Terceiro segmento: '))
if l1 == l2 == l3 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
elif l1 != l2 != l3 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
