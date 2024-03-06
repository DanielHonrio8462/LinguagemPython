import random
from time import sleep
computador = random.randint(0, 5)  # Maquina pensando em um número entre 0 e 5
print('-=-' * 19)
print('  Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei '))  # jogador
print('PROCESSANDO...')
sleep(3)
if jogador==computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))


