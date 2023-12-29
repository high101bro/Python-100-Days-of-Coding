

class User: #PascalCase naming convenition: ex: ThisIsAClass
    # Giving User an attribute
    def __init__(self, user_id, username):
        print(f"Creating a new user.")  # The __init__ is ran everytime the class is called
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Giving User a method
    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1.id = '001'
# user_1.username = 'Dan'
# print(user_1.username)

user_1 = User("001","Dan")
user_2 = User("002","Lisa")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)











