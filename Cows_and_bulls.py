import random

number = list(str(random.randint(1000, 9999)))
print(number)
y = list(input('Welcome to the Cows and Bulls game!\nEnter a number: '))
cow = 0
bull = 0
guesses = 1
while True:
    try:
        for k in range(4):
            if int(number[k]) == int(y[k]):
                cow += 1
            else:
                bull += 1
        if cow == 4:
            print('You got 4 cows, you guessed it after {} times'.format(guesses))
            guesses = 0
            break
        else:
            print('You got {} cows, {} bulls'.format(cow, bull))
            cow = 0
            bull = 0
            guesses += 1
            y = list(input('Enter a number: '))
    except (ValueError, IndexError):
        y = list(input('Wrong input, try again!\nEnter a number: '))



