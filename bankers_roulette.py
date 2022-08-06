# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Calculate the number of people
number_of_people = len(names)

# Randomise the index of array of the people and then putting the random index to the names array
random_person = random.randint(0, (number_of_people-1))

print(f"{names[random_person]} is going to buy the meal today!")
# print(names)
# print(number_of_people)
