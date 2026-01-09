class Book:
	def __init__(self, tittle, author):
		self.tittle = tittle
		self.author = author
		self.reviews = []

	def add_review(self, review):
		self.reviews.append(review)
		print("Review added successfully!: " ,review)

	def count_reviews(self):
		return len(self.reviews)

	def all_review(self):
		print("Reviews:")
		for review in self.reviews:
			print("_", review)

b1 = Book("atomic habit","james")
# b2 = Book("we were never meant to be.","krishna", "3star")
# b3 = Book("alone","rk", "2star")
# b4 = Book("panchayat","mels", "5star")

b1.add_review("very useful book")
b1.add_review("i liked it")
b1.add_review("i know about this book ")


print("Total reviews: ", b1.count_reviews())
b1.all_review()





		