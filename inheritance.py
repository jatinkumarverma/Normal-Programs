class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name



# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName())
