from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = "They can conquer who believe they can."


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('POOJA', 'Ms.', 21, 5.7)

friend_one = Spy('Kritika', 'Ms.', 21, 4.9)
friend_two = Spy('RAJAT', 'Mr.', 20, 5)
friend_three = Spy('Shikha', 'Ms.', 19,3.39, )
friend_four = Spy('Aman', 'Mr.',22,4.29 )


friends = [friend_one, friend_two,friend_three,friend_four]


