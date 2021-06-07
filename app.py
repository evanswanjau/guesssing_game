"""
Guessing Game
"""
import random

# get random value
def get_random_value():
    random_value = random.randint(0, 10)

    return random_value

# input value
def get_input_value():
    """
    Get input value and return int
    """
    guess = int(input("Enter a number: "))

    return guess


# compare the random number and input
def check_guess(response="Fail"):
    """
    Function that equates a random number 
    to an input and returns a response
    """
    guess = get_input_value()
    random_value = get_random_value()

    if guess != random_value:
        present_data(guess, random_value, response)
        check_guess(response)
    else:
        response = 'Success'
        present_data(guess, random_value, response)
        
    return response

# present data
def present_data(guess, random_value, response):
    print('--------')
    print(response)
    print('--------')
    print('Value: ' , random_value)
    print('Guess: ' , guess)

# execute program
check_guess()