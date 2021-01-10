from random import randint
guesses =1
number = randint(1,100)
guess = int(input('Guess a numberbetween 1 and 100.'))
while guess !=number:
    if guess < number:
        print ('What a lovely day!')
        guess = int(input('Guess again!'))
        guesses = guesses + 1
    elif guess >number:
        print ('Really?')
        guess = int(input('Guess again!'))
        guesses = guesses + 1

        print()
        print ('Congratulation you guessed the number!')
        print('It only took you',guesses,'guesses!')

