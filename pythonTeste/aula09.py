frase = 'Curso em Vídeo Python'
print(frase[3:13])  # da terceira letra a décima segunda
print(frase[:13])  # do começo a décima segunda
print(frase[1:15:2])  # da primeira letra a décima quinta pulando de 2 em 2
print(frase.count('o'))  # vai contar quantas vezes tem a letra o minúscula
print(frase.upper().count('O'))  # contando a quantidade de o jogada para a letra Maiúscula
print(len(frase.strip()))  # contando o tamanho da frase, strip remove os espaços
print(frase.replace('Python', 'Android'))  # tracando palavras
frase = frase.replace('Python', 'Android')  # salvando modificação
print('Curso' in frase)  # Verifica se a palavra está na frase
print(frase.find('Vídeo'))  # diz qual posição está a frase
dividido = frase.split()  # dividindo frase
print(dividido[0][3])  # imprimindo a frase 0 e a terceira letra


