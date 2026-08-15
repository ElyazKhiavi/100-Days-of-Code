import uuid

class User:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('Sarah')
user_2 = User('Mona')

user_1.follow(user_2)

print(user_1.name,user_1.id, user_1.follower,user_1.following)
print(user_2.name,user_2.id, user_2.follower,user_2.following)