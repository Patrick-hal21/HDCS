class EmptyQueue():
    def __init__(self):
        self.items = []

    def push(self, item): # will be enque 
        self.items.append(item)

    def deque(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    # def __str__(self):
    #     return str(self.items)

myQueue = EmptyQueue()

#  a.
myQueue.push(2)
myQueue.push(4)
myQueue.push(3)
myQueue.push(7)

print()

print(*(f"{item} <-" for item in myQueue.items))

print()

# b. show in two-cell standard notation
print("Front :", myQueue.items[0], "| Back :", myQueue.items[-1])

print()

# c. show the result after     deque -> deque -> front

myQueue.deque()
myQueue.deque()

print("After dequeuing twice: Front is -> ", myQueue.items[0])
