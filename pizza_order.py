# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_price = 0
s_price = 15
m_price = 20
l_price = 25


pepp_price_s = 2
pepp_price_l = 3
extra_cheese_price = 1


if size.lower() == "s":
    total_price = s_price

    if add_pepperoni.lower() == "y":
        total_price += pepp_price_s

    if extra_cheese.lower() == "y":
        total_price += extra_cheese_price


elif size.lower() == "m":
    total_price = m_price

    if add_pepperoni.lower() == "y":
        total_price += pepp_price_l

    if extra_cheese.lower() == "y":
        total_price += extra_cheese_price


elif size.lower() == "l":
    total_price = l_price

    if add_pepperoni.lower() == "y":
        total_price += pepp_price_l

    if extra_cheese.lower() == "y":
        total_price += extra_cheese_price


else:
    print("You haven't entered the pizza size correctly, try again!")


print(f"Your final bill is: ${total_price}.")
