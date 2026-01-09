class BankAccount:
	def __init__(self, account_no, owner_name, balance):
		self.account_no = account_no
		self.owner_name = owner_name
		self.balance = balance

	def deposit(self, balance):
		self.balance += balance
		print("Balance added successfully: ", balance)

	def withdraw(self, balance):
		if balance <= self.balance:
			self.balance -= balance
			print("Money debited: ",balance)
		else:
			print("Insuffcient balance", balance)
	
	def chk_bal(self):
		print("The available balance is ", self.balance)

b1 = BankAccount(123, "sk", 10_000)

b1.deposit(2000)
b1.withdraw(1000)
b1.chk_bal()


		