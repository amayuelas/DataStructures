class Queue(object):
    def __init__(self,maxSize, output):
        self.queue = []
        self.maxSize = maxSize
        for i in range(self.maxSize):
            self.queue.append(None)
        self.head = -1
        self.tail = -1
        self.out = output

    def isFull(self):
        return (self.head == (self.tail + 1) % self.maxSize)

    def isEmpty(self):
        return (self.head == -1 and self.tail == -1)

    def enqueue(self,code):
        if (self.isFull()):
            print("The queue is Full")
            self.dequeue()

        if (self.isEmpty()):
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.maxSize

        self.queue[self.tail] = code
        return self.tail

    def dequeue(self):
        code = None
        if(self.isEmpty()):
            print("The queue is Empty")
        elif(self.head == self.tail):
            code = self.queue[self.tail]
            self.head = -1
            self.tail = -1
        else:
            code = self.queue[self.head]
            self.head = (self.head + 1) % self.maxSize
        print(code)

    def clearQ(self):
        while(self.isEmpty() == False):
            self.dequeue()
