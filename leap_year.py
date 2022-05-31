# 🚨 Don't change the code below 👇
from queue import PriorityQueue


year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# print(year)
# My Solution logic is not correct
# if (year % 4 == 0 and year % 100 and year % 400):
#     print("Leap year.")
# else:
#     print("Not leap year.")


# Correct Solution

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
