import random
import phases

with open('hangman/palavras.txt', 'r', encoding='utf-8') as arquivo:
    lista_palavras_inicial = arquivo.readlines()
    lista_palavras_final = [palavra for palavra in lista_palavras_inicial if 6 <= len(palavra) <= 11]

sem_chances = False

palavra_escolhida = random.choice(lista_palavras_final).strip()

palavra_vazia = [' ' for numero in palavra_escolhida]

chances = 0

while not sem_chances:
    print('Bem-vindo ao jogo da forca!')
    print(phases.PHASES_IMG[chances])
    print(f'Palavra: {palavra_vazia}')
    palpite = input('Digite uma letra: ')

    if isinstance(palpite, str):
        if palpite in palavra_escolhida:
            for i in range(len(palavra_escolhida)):
                if palpite == palavra_escolhida[i]:
                    palavra_vazia[i] = palpite
        else:
            print('Palpite incorreto!')
            chances += 1
        if ''.join(palavra_vazia) == palavra_escolhida:
            sem_chances = True
            print(f'Você acertou!!!\nA palavra era: {palavra_escolhida}')
        if chances == 6:
            sem_chances = True
            print(f'Sem mais chances!!!\nA palavra era: {palavra_escolhida}')
    else:
        print('Digite apenas letras')
