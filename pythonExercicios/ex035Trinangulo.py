print('-=-' * 8)
print(' Análisando Triángulo')
print('-=-' * 8)
seg1 = int(input("Primeiro Segmento: "))
seg2 = int(input("Segundo Segmento: "))
seg3 = int(input("Terceiro Segmento: "))
if (seg1 + seg2) > seg3 and (seg1 + seg3) > seg2 and (seg2 + seg3) > seg1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
