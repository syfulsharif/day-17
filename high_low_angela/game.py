# Importing Required Dependency Files
import os
from art import logo, vs
from game_data import data
from random import choice


def format_data(account):
    """Format the data to display"""
    return f'{account["name"]}, a {account["description"]}, from {account["country"]}.'


def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Display Art
print(logo)
score = 0

game_on = True

account_b = choice(data)
while game_on:

    # Generate Random Account from the data
    account_a = account_b
    account_b = choice(data)

    # Making Position at account B the next account at position A
    while account_a == account_b:
        account_b = choice(data)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # print(account_a)
    # print(account_b)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask users for a guess
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(user_input, a_follower_count, b_follower_count)

    # Clear the screen
    os.system("clear")
    print(logo)

    # Give User feedback
    if is_correct:
        score += 1
        print(f"You are right. Current Score is {score}")

    else:
        game_on = False
        print(f"Sorry, You got it wrong. Final Score is {score}")
