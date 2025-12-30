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
			pass
		elif user_input == "3":
			pass
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



	
obj = chatbook()


