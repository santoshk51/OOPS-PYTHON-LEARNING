from datetime import datetime

# User class
class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, chatroom, text):
        chatroom.send_message(self, text)

    def join_chatroom(self, chatroom):
        chatroom.add_user(self)

    def leave_chatroom(self, chatroom):
        chatroom.remove_user(self)


# Message class
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.timestamp = datetime.now()

    def display(self):
        print(f"[{self.timestamp.strftime('%H:%M:%S')}] {self.sender.username}: {self.text}")


# ChatRoom class
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.username} joined {self.room_name}")

    def remove_user(self, user):
        self.users.remove(user)
        print(f"{user.username} left {self.room_name}")

    def send_message(self, user, text):
        if user in self.users:
            message = Message(user, text)
            self.messages.append(message)
        else:
            print("User is not in the chatroom")

    def show_chat_history(self):
        print(f"\nChat History of {self.room_name}:")
        for message in self.messages:
            message.display()


# Example usage
chat = ChatRoom("Python Chat")

u1 = User("Santosh")
u2 = User("Amit")

u1.join_chatroom(chat)
u2.join_chatroom(chat)

u1.send_message(chat, "Hello everyone!")
u2.send_message(chat, "Hi Santosh!")

chat.show_chat_history()

u2.leave_chatroom(chat)
