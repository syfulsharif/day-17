# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
lowered_name = name1.lower() + name2.lower()


# Checking for True
count_for_true = 0

num_of_t = lowered_name.count("t")
count_for_true += num_of_t
num_of_r = lowered_name.count("r")
count_for_true += num_of_r
num_of_u = lowered_name.count("u")
count_for_true += num_of_u
num_of_e = lowered_name.count("e")
count_for_true += num_of_e

# Checking for Love
count_for_love = 0

num_of_l = lowered_name.count("l")
count_for_love += num_of_l
num_of_o = lowered_name.count("o")
count_for_love += num_of_o
num_of_v = lowered_name.count("v")
count_for_love += num_of_v
num_of_e = lowered_name.count("e")
count_for_love += num_of_e


love_score = str(count_for_true) + str(count_for_love)
# print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
