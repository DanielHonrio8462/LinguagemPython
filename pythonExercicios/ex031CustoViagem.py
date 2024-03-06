distância = float(input('Qual a distância da sua Viagem? '))
print('Você está preste a começar uma Viagem de {:.1f}Km.'.format(distância))
if distância <= 200:
    passagem = distância * 0.5
else:
    passagem = distância * 0.45
print('E o preço da sua Pasagem vai ser de R$ {:.2f}'.format(passagem))
