import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Choose a letter: \n")
guess = guess.lower()
print(guess)


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
i = 0
while i < len(chosen_word):
    if chosen_word[i] == guess:
        print("Right")
    else:
        print("Wrong")
    i += 1
