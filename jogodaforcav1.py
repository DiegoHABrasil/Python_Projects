from encodings import utf_8


# -*- coding:utf_8 -*-

import random

from numpy import append, concatenate

board = ['''

+----+
|    |
     |
     |
     |
     |
     |
===========''', '''

+----+
|    |
O    |
     |
     |
     |
     |
===========

''', '''

+----+
|    |
O    |
|    |
     |
     |
     |
===========

''', '''

+----+
|    |
O    |
|\   |
     |
     |
     |
===========

''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
     |
===========

''', '''

 +---+
 |   |
 O   |
/|\  |
  \  |
     |
     |
===========

''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
     |
===========

''']

class Hangman:
    # Método construtor
    def __init__(self,word,letter,answer,counter):
        print("Começo do jogo!")
        self.word = word        # Variável para armazenar a palavra sorteada, inalterável (deve ser usada como index)
        self.letter = letter
        self.answer = answer    # Variável para armazenar os acertos e as letras escondidas do jogo (usada para printar status)
        self.counter = counter

        # Método para adivinhar a letra
    def guess(self,letter):
        i = 0
        sw = str(self.word)
        if sw.find(letter) == -1:
            self.counter += 1
            print("Errou!")
        else:
            for i in range(len(self.answer)):
                if self.word[i] == letter:
                    self.answer[i] = letter
                i += 1
            print("Acertou!")
        
    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.counter > 6:
            return False
        else: return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if list(self.word) == self.answer:
            return True
        else: return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        self.answer = list(self.word)
        for x in range(len(self.answer)):
            self.answer[x] = "_"
        return self.answer
        
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
            print(board[self.counter])
            print(str(self.answer))
            

def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


def main():
    game = Hangman(rand_word(),"","",0)
    game.hide_word()

    while game.hangman_over():
        if game.hangman_won():
            print("Parabéns! Você venceu!") 
            break
        game.guess(input("Digite uma letra: "))
        if game.counter == 6:
            print("\nGame over! Você perdeu.")
            print("\nA palavra era: "+game.word)
            break
            
        game.print_game_status()

    print("\n Foi bom jogar com você! Agora vá estudar!\n")

if __name__ == "__main__":
    main()
