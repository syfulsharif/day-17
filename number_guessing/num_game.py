from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

# Print the logo when the game is initialized
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

computer_number = randint(1, 100)
print(computer_number)

user_chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()


def take_user_guess(life):
    """Takes user input from the user and returns the guess as integer"""
    user_guess = int(input(f"You have {life} attempts remaining to guess the number."))
    return user_guess


def play_game():
    """Plays the number guessing game as long as the correct number guessed by the user and user has attempts left"""
    if user_chosen_level == "easy":
        user_life = EASY_LEVEL
    elif user_chosen_level == "hard":
        user_life = HARD_LEVEL
    else:
        print("Invalid Input by player!")
    user_guess_num = take_user_guess(user_life)

    # if user_guess_num == computer_number:
    #     print(f"You got it! The answer was {computer_number}.")

    while user_life > 0 and user_guess_num != computer_number:
        if user_guess_num > computer_number:
            print("Too High! Guess Again!")
            user_life = user_life - 1
            if user_life != 0:
                user_guess_num = take_user_guess(user_life)

        elif user_guess_num < computer_number:
            print("Too Low! Guess Again!")
            user_life = user_life - 1
            if user_life != 0:
                user_guess_num = take_user_guess(user_life)

    if user_life == 0:
        print("You used all your chances, You lose!")

    if user_guess_num == computer_number:
        print(f"You got it! The answer is {computer_number}.")


play_game()
