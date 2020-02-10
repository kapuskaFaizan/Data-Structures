#using linked list
class QueueADT:
    def __init__(self,min=1):
        if min <= 0:
            raise ValueError('queue shoud atleast have one member')
        self.capacity= min * 2
        self.items = []
        
    def isFull(self):
        if len(self.items) == self.capacity:
            return True
        else :
            return False
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def enQueue(self,item):
        if QueueADT.isFull(self):
            raise ValueError('Queue is full')
        self.items.append(item)
    
    def deQueue(self):
        if QueueADT.isEmpty(self):
            raise ValueError('queue is empty')
       
        return self.items.pop()
    
    def peek(self):
        queue = self.items[-1]
        return queue
    
    def size(self):
        return len(self.items)

class vehicle_model:
    
    def __init__(self,vin,model_name,year):
        self.vin = vin
        self.model_name = model_name
        self.year = year
    def __add__(self, other):
        x = self.year + other
        return '(%s,%s,%d)' % (self.vin,self.model_name,x)
    
    def __repr__(self):
        return '(%s, %s ,%d)' % (self.vin, self.model_name, self.year)
       
v = vehicle_model(1,'audi',2010)
v1= vehicle_model(2,'bmw',2010)
v2= vehicle_model(3,'mercedes',2010)
v3= vehicle_model(4,'jaguar',2010)


def addYear(x):
    l = []
    x.enQueue(v)
    y = QueueADT(2)
    for i in x.items:
        l.append(i)

    for i in l:
        i += 1
        y.enQueue(i)
    return y