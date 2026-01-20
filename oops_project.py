class chatbook:
	def __init__(self): # constructor || special method/ magic method/dunder method 
		self.username = ''
		self.password = ''
		self.loggedin = False
		self.menu()

	def menu(self):
		user_input = input("""welcome to chatbook!! How would you like to proceed?
					 1. Press 1 to signup
					 2. press 2 to signin
					 3. Press 3 to write a post
					 4. Press 4 to message a friend
					 5. Press any other key to exit
					 Enter your choice: """)
		
		if user_input == "1":
			self.signup()
		elif user_input == "2":
			self.signin()
		elif user_input == "3":
			self.write_post()
		elif user_input == "4":
			self.sendmsg()
		else:
			exit()


	def signup(self):
		email = input("Enter your email here: ")
		password = input("Enter your password here: ")
		self.username = email
		self.password = password
		print("signup successfull!!")
		print("\n")
		self.menu()


	def signin(self):
		if self.username == '' and self.password == '':
			print("Please signup first by pressing 1 in the main menu")
		else:
			uname = input("Enter your username: ")
			pwd = input("Enter your password: ")
			if self.username == uname and self.password == pwd:
				self.loggedin = True
				print("Signin sucessfull!!")
			else:
				print("Inavlid credentials, please try again")
		print("\n")
		self.menu()

	def write_post(self):
		if self.loggedin == True:
			post = input("Write your post here: ")
			print(f"Your post has been published! ->{post}")
		else:
			print("Please signin first to write any post")
		print("\n")
		self.menu()

	def sendmsg(self):
		if self.loggedin == True:
			post = input("Write your message here: ")
			frd = input(f"Whom to send message: {post}")
			print(f"Your message has been sent to {frd} ->{post}")
		else:
			print("Please signin first to send any message")
		print("\n")
		self.menu()

	
obj = chatbook()


