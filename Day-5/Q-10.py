class User:
	def __init__(self, username):
		self.username = username

	def send_message(self, chatroom, text):
		chatroom.send_message(self, text)

	def join_chatroom(self, chatroom):
		chatroom.add_user(self)
	
	def leave_chatroom(self, chatroom):
		chatroom.remove_user(self)

	
class send_message:
	def __init__(self, sender, text):
		self.sender = sender
		self.text = text

	def display(self):
		print(f"{self.sender.username}: {self.text}")

