class Computer: 
	def __init__(self, price1, ver1):
		self.price = price1
		self.ver = ver1
		print("Creating instance of Computer Class")

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("Creating instanc of Person class")

c1 = Computer(90000, 3.9)
p1 = Person("Harish", 25)