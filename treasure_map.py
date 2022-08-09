# 🚨 Don't change the code below 👇
from hashlib import new
from turtle import pos


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# Checking if the user input is valid

if int(position) < 34 and int(position) > 10:
    colum = int(position[1]) - 1
    row = int(position[0]) - 1
    map[colum][row] = "X"
else:
    print("Please enter a valid position less than 34 and more than 10")


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
