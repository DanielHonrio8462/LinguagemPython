nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()  # Dívidindo em blocos
print(n)
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
