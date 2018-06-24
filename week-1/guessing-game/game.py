"""A number-guessing game."""

import random
import math

print('Hello, player!')
player_name = input('Enter your name: ')
minimum = int(input("Pick your start number. Pick 1 for default."))
maximum = int(input("Pick your end number. Pick 100 for default."))


def guessing_game(min_r, max_r, max_guess):
    count = 0
    com_num = random.randint(min_r, max_r)

    while count < max_guess:
        try:
            guess_num = int(
                input('Please choose a number between {} and {}:'.format(
                    min_r,
                    max_r
                    )
                )
            )
        except ValueError:
            print('Numbers are cool. Please enter a number.')
            continue
        if guess_num < min_r or guess_num > max_r:
            print('FAILURE... TRY AGAIN...')
            continue
        count += 1
        if guess_num == com_num:
            print('you win! You guessed ' + str(count) + ' times')
            return count
        elif guess_num < com_num:
            print('you guessed too low.')
        else:
            print('you guessed too high.')
    print("Too many guesses!")
    return -1


def score_converter(guess, min_r, max_r):
    converter = math.log(max_r - min_r + 1, 2)
    return converter/guess * 10


best_score = None
game_continue = 'yes'

while game_continue == 'yes':

    guess = guessing_game(minimum, maximum, 5)
    try:
        if guess < best_score and guess != -1:
            best_score = guess
    except TypeError:
        if guess != -1:
            best_score = guess
    game_continue = input('Do you want to play again? (yes/no)').lower()

try:
    score = score_converter(best_score, minimum, maximum)
except TypeError:
    score = None
print('Your lowest number of guesses is: '+str(best_score))
print('Your best score is ' + str(score))
