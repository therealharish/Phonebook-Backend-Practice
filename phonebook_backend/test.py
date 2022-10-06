class Queue:
    def __init__(self, maxsize):
        self.__maxsize = maxsize
        self.__q = [None] * maxsize
        self.__front = 0
        self.__rear = -1

    def enqueue(self, ele):
        if self.is_full():
            print("Queue is Full")
            return
        self.__rear += 1
        self.__q[self.__rear] = ele

    def is_full(self):
        return self.__rear == (self.__maxsize - 1)

    def is_empty(self):
        return self.__rear == -1

    def show(self):
        print(self.__q)


q = Queue(5)
for i in range(6):
    q.enqueue(i)
    q.show()
