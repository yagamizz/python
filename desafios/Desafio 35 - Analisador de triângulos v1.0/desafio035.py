print('=' * 30)
print('ANALISADOR DE TRIÂNGULO')
print('=' * 30)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else: 
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
