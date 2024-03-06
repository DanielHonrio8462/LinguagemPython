dias = int(input('Quantos dias alugados? '))
kmr = float(input('Quantos Km rodados? '))
pagar = dias*60 + kmr*0.15
print('O tatal a pagar de aluguel é R$ {:.2f}'.format(pagar))
