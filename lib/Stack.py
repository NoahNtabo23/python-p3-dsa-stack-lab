class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(0)

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self,limit=100):
        return len(self.items)>self.limit

    def search(self, target):
        pass
