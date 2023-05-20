from random import randint
from palavras import *
from funcoes import *

# Menu de tema:
titulo()
print(f' [ 1 ] --> {vermelho}BTS{reset}'
      f'\n [ 2 ] --> {vermelho}Animais{reset}'
      f'\n [ 3 ] --> {vermelho}Países{reset}')

tema = int(input(f'\n{lilas}[𝙴𝚜𝚌𝚘𝚕𝚑𝚊 𝚞𝚖 𝚍𝚘𝚜 𝚝𝚎𝚖𝚊𝚜]--> {reset}'))

# Palavra definida com base no tema:
if tema == 1:
    num = randint(0, len(bts) - 1)
    palavra = ' '.join(bts[num]).split()
elif tema == 2:
    num = randint(0, len(animais) - 1)
    palavra = ' '.join(animais[num]).split()
elif tema == 3:
    num = randint(0, len(paises) - 1)
    palavra = ' '.join(paises[num]).split()

# Número de letras presentes na palavra
num = len(palavra)

# Cria uma lista do tamanho da lista da palavra
numletras = []
for c in range(num):
    numletras.append('_')

# Erros
erros = 0

# Interface
titulo()
forca()

# Lista com as letras descartadas
letras_usadas = []

# Jogo
while True:

    print(f'𝐋𝐞𝐭𝐫𝐚𝐬 𝐝𝐞𝐬𝐜𝐨𝐛𝐞𝐫𝐭𝐚𝐬: {verde + " ".join(numletras) + reset}')
    print(f'𝐋𝐞𝐭𝐫𝐚𝐬 𝐝𝐞𝐬𝐜𝐚𝐫𝐭𝐚𝐝𝐚𝐬: {vermelho + " ".join(letras_usadas) + reset}')

    letra = input(f'{lilas}[𝒟𝒾𝑔𝒾𝓉𝑒 𝓊𝓂𝒶 𝓁𝑒𝓉𝓇𝒶]-->{reset}  ')

    titulo()

    if letra not in char or letra in letras_usadas:
        forcas(erros)

    else:
        # Se a letra estiver presente na palavra
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    numletras.pop(i)
                    numletras.insert(i, letra)

            # Desenho da forca
            forcas(erros)

            # Caso a lista numletras seja igual a lista palavras, o usuário vence
            if numletras == palavra:
                vitoria()
                print(f'A palavra era {lilas + "".join(palavra)}')
                break

        # Caso não esteja
        else:
            erros = erros + 1
            letras_usadas.append(letra)
            # Desenho do personagem na forca quando o usuário erra
            forcas(erros)
            # se erros for igual a 6, o usuário perde
            if erros == 6:
                erro6()
                print(f'A palavra era {lilas + "".join(palavra)}')
                break
