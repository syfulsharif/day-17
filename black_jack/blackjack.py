import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack_card = 11
user_card_1 = random.choice(cards)
# print(user_card_1)
user_card_2 = random.choice(cards)
# print(user_card_2)
user_card_sum = user_card_1 + user_card_2
print(user_card_sum)

computer_card_1 = random.choice(cards)
computer_card_2 = random.choice(cards)
computer_card_sum = computer_card_1 + computer_card_2
print(computer_card_sum)
