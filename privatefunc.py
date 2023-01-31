class A:

	def fun(self):
		print("Public method")

	def __fun(self):
		print("Private method")

	
	def Help(self):
		self.fun()
		self.__fun()

obj = A()
obj.Help()
