
# Game codes-------------------------------------------------------------------------------------
import random
import time
user_num = int(input('Guess a number between 0-30:   '))
rand_num = random.randint(0,30)
num_variance = user_num - rand_num
user_guesses = 1
price_per_guess = 3

while num_variance != 0:
    user_guesses += 1
    if num_variance < 0:
        print (f'Oh no! Your guess is smaller than the magic number! Try again.')
    elif num_variance > 0:
        print(f'Oh no! Your guess is bigger than the magic number! Try again.')
    else:
        print(f'Not sure what you have entered. Try again with another input in a number format!')
    user_num = int(input('Try another number between 0-30:   '))
    num_variance = user_num - rand_num
print (f'Aha! You have guess the correct magic number {rand_num}!')
time.sleep(1)
print(f'Well... you took {user_guesses} guesses, '
      f'you now owe me £{price_per_guess*user_guesses} at £{price_per_guess} for each guesses.')

