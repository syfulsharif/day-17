print("Welcome to the rollercoaster!")
# Take input from the visitor
height = int(input("Please tell me your height in centimeter: "))

if height > 120:
    age = int(input("Tell me about your age: "))
    if age < 12:
        print("For your age, the base ticket price is $5")
        ticket = 5
    elif age >= 12 and age <= 18:
        print("For your age, the base ticket price is $7")
        ticket = 7
    elif age > 18:
        print("For your age, the base ticket price is $12")
        ticket = 12
    photos = input("Would like to take photos for $3 extra? y/n ")
    if photos == "y":
        ticket += 3
        print(f"You have to pay total {ticket} for the ticket.")
    else:
        print(f"You have to pay total {ticket} for the ticket.")
else:
    print("Sorry, you have to grow taller before you can ride.")
