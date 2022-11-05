class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        # print("User is being created....")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("0001", "Sharif")
user_2 = User("0002", "Angela")

user_1.follow(user_2)


print(user_2.followers)
print(user_1.following)