import random
import re

# Simple hangman game. The player has 8 chances to guess a word in order to win. 
# Otherwise he will be hanged! Typing a non ASCII character, uppercase letter or a 
# letter that was already used does not reduce attempts count.

def menu():
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == 'play':
        print()
        play_game()
    elif play == 'exit':
        pass
    else:
        print('Wrong command\n')
        menu()

def play_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    # words = ['java', 'javascript']
    word = random.choice(words)
    letter_list = ['-' for letter in word]
    chances = 8
    tried_letters = []
    while '-' in letter_list:
        # while True:
        print(''.join(letter_list))
        guess = input('Input a letter: ')
        if guess in word and len(guess) == 1:
            if guess not in letter_list:
                print('\n')
                occurrence_index = [m.start() for m in re.finditer(guess, word)]
                for occurrence in occurrence_index:
                    letter_list[occurrence] = guess
            else:
                print('You already typed this letter\n')
        else:
            if len(guess) != 1:
                print('You should print a single letter\n')
            elif not guess.isalpha() or not guess.islower():
                print('It is not an ASCII lowercase letter\n')
            elif guess in tried_letters:
                print('You already typed this letter\n')
            else:
                chances -= 1
                if chances == 0:
                    print('No such letter in the word\nYou are hanged!\n')
                    menu()
                print('No such letter in the word\n\n')
                tried_letters.append(guess)
            
    print('You guessed the word {}!\nYou survived!\n'.format(''.join(letter_list)))
    menu()

print('H A N G M A N')
menu()
