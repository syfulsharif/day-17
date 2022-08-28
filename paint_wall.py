# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    cans_needed = ceil((height * width) / cover)
    return cans_needed


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
cans_needed_to_paint = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You'll need {cans_needed_to_paint} cans of paint.")
