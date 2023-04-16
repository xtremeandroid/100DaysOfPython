class User:

    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user_object):
        user_object.followers += 1
        self.following += 1


user_1 = User(1, "Ayush")
user_2 = User(2, "Prajwal")

user_1.follow(user_2)
print(user_2.followers)
print(user_1.following)