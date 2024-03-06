import math
angulo = float(input('Digite um ângulo qualquer: '))
radi = math.radians(angulo)
print('O Seno de {}° é {}'.format(angulo, math.sin(radi)))
print('O cosseno de {}° é {}'.format(angulo, math.cos(radi)))
print('A tangente de {}° é {}'.format(angulo, math.tan(radi)))
