#DLINKED LIST BASED
class StackADT2:
    def __init__(self,min=1):
        self.top = 0
        self.capacity=2*min
        self.items = []
        if min <= 0:
            raise ValueError('Minimum value should atleast b 1')
    
    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top == self.capacity:
            return True
        else:
            return False
    def push(self, item): 
        if StackADT2.isFull(self):
            raise ValueError('Stack is full')
        else:
            self.items.append(item)
            self.top +=1

    def pop(self):
        if StackADT2.isEmpty(self):
            raise ValueError('Stack is empty')
        else:
            
            self.top -= 1
            return self.items.pop()
    
    def size(self):
        return self.top