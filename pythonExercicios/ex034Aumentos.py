sal = float(input('Qual o salário do Funcionario R$ '))
if sal <= 1250:
    novosal = sal + (sal * 0.15)
else:
    novosal = sal + (sal * 0.1)
print('Quem ganhava R$ {} agora vai ganhar R$ {} agora'.format(sal, novosal))
