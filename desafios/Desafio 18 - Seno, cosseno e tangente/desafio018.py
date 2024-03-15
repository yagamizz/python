import math
angulo_inteiro = int(input('digite o ângulo: '))
angulo_em_radiano = math.radians(angulo_inteiro)
cos_value = math.cos(angulo_em_radiano)
sin_value = math.sin(angulo_em_radiano)
tan_value = math.tan(angulo_em_radiano)
print(f'COSSENO: {cos_value}')
print(f'SENO: {sin_value}')
print(f'TANGENTE: {tan_value}')
