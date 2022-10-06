
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
        return self.__rear < self.__front

    def show(self):
        print(self.__q)

    def dequeue(self):
        if self.is_empty():
            self.__rear = -1
            self.__front = 0
            return None
        ele = self.__q[self.__front]
        self.__front += 1
        return ele
    
intQueue = Queue(3)
intQueue.enqueue(3)
intQueue.enqueue(5)
intQueue.enqueue(8)

charQueue = Queue(5)
charQueue.enqueue('a')
charQueue.enqueue('b')
charQueue.enqueue('c')
charQueue.enqueue('d')
charQueue.enqueue('e')

def solve(intQueue, charQueue):
    newQueue = Queue(8)
    while (not intQueue.is_empty() or not charQueue.is_empty()):
        if (not intQueue.is_empty()):
            newQueue.enqueue(intQueue.dequeue())
        if (not charQueue.is_empty()):
            newQueue.enqueue(charQueue.dequeue())
    
    while(not intQueue.is_empty()):
        newQueue.enqueue(intQueue.dequeue())
    
    while(not charQueue.is_empty()):
        newQueue.enqueue(charQueue.dequeue())
    
    return newQueue

ansQueue = solve(intQueue, charQueue)
ansQueue.show()
