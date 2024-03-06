velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}!'.format(multa))
else:
    print('A sua Velocidade de {:.1f}Km/h está no limite permitido'.format(velocidade))
    print('Tenha um bom dia! Dirija com segurança!')
