nome = 'Daniel'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}

print('Olá! muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))  # style, text, back | 0,1,4,7 | 30 à 37 | 40 à 47

