import math
ca = float(input('Digite o cateto adjacente do triângulo: '))
co = float(input('Digite o cateto oposto do triângulo: '))
print('A Hipotenusa desse triângulo é {}.'.format(math.hypot(ca, co)))
