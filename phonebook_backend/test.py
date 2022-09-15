class Computer:
    brand = "HP"
    def __init__(self, price1, ver1):
        self.price = price1
        self.ver = ver1

    def buy(self):
        print("Buying computer")

    def exchange(self):
        print("Exchanging Computer")

    def getPrice(self):
        print(self.__price)


def display(l):
    for i in l:
        print(i.price, i.ver, i.brand)

c1 = Computer(90000, "3.5")
c2 = Computer(80000, '3.4')
c3 = Computer(70000, '3.3')
c4 = Computer(60000, '3.2')

l = [c1, c2, c3, c4]

display(l)

