#arraybase
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



class StackADT:
    
    def __init__(self,mini=1 ):
        if mini <= 0:
            raise ValueError(' minimum should be atleast 1')
        self.capacity = mini*2
        self.items = []
    
    def isEmpty(self):
        if len(self.items) ==0:
            return True
        else:
            return False

    def push(self, item): 
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isFull(self):
        if StackADT.size(self) == self.capacity:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)

    def peek(self):
        stack = self.items[-1]
        return stack

s = StackADT()
s.push(v)
s.push(v1)

def countMake(s,make):
    ns = StackADT()
    l = []
    for i in s.items:
        l.append(i)
    final_list = [i for i in l if i.model_name == make]
    for i in final_list:
        ns.push(i)
    return ns