#using raw array
class QueueADT2:
    def __init__(self,min):
        self.end = 0
        self.capacity = 2 * min
        self.items = []
        
    def isEmpty(self):
        if self.end == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.end == self.capacity:
            return True
        else:
            return False
    
    def enQueue(self,item):
        if QueueADT2.isFull(self):
            raise ValueError('queue is already full')
        else:
            self.items.append(item)
            self.end += 1
    
    def deQueue(self):
        if QueueADT2.isEmpty(self):
            raise ValueError('queue is empty')
        else:
            self.end -= 1
        return self.items.pop()
    
    def size(self):
        return self.end