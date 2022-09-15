class Computer: 
	def __init__(self, price1, ver1):
		self.price = price1
		self.ver = ver1
		print("Creating instance of Computer Class")

class Person:
	def __init__(self, name, age, comp1):
		self.name = name
		self.age = age
		self.comp = comp1
		print("Creating instance of Person class")
		print(self.comp.price, self.comp.ver)

		

c1 = Computer(90000, 3.9)
p1 = Person("Harish", 25, c1)     #this is aggregation
print(c1.price, c1.ver)

p2 = Person("Sharma", 100, Computer(800000,"2.5")) #this is compotion, if p2 is deleted so will the object created inside of it
print(p2.name, p2.age, p2.comp.price, p2.comp.ver)