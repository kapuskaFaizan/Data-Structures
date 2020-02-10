#vehicle_model
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
   
#assignment1 (A)
class DLinkedList: 
    class Node: 
        def __init__(self, data): 
            self.data = data 
            self.next = None
            self.prev = None
    def __init__(self): 
        self.front = None
        self.rear = None
        self.int_length =0
        
    def addFirst(self, new_data): 
        new_node = DLinkedList.Node(new_data) 
        new_node.next = self.front 
        if self.front is not None: 
            self.front.prev = new_node 
            
        self.front = new_node 
        self.int_length +=1
        
    def addLast(self, new_data):
        
        new_node = DLinkedList.Node(new_data) 
        new_node.next = None
  
        if self.front is None: 
            new_node.prev = None
            self.front = new_node 
            return 
   
        last = self.front 
        while(last.next is not None): 
            last = last.next
            
        last.next = new_node  
        new_node.prev = last
        self.int_length +=1
  
        return
    
    def printNextLine(self, node): 
  
        print("\nTraversal in forward direction")
        while(node is not None): 
            print (node.data) 
            last = node 
            node = node.next
    
    
    def printPrevLine(self,node):
        while(node is not None): 
            last = node 
            node = node.next
        print("\nTraversal in reverse direction")
        while(last is not None): 
            print(" % d" %(last.data),) 
            last = last.prev 
    
    def deleteFirst(self, dele):  
        if self.front is None or dele is None: 
            raise ValueError('list is empty')
          
        if self.front == dele: 
            self.front = dele.next

        if dele.next is not None: 
            dele.next.prev = dele.prev 
      
 
        if dele.prev is not None: 
            dele.prev.next = dele.next
        self.int_length -=1
         
    def deleteLast(self):
        if self.front is None:
            raise ValueError('list is empty')
        if self.front.next is None:
            self.front = None
            return
        n = self.front
        while n.next is not None:
            n = n.next
        n.prev.next = None
        self.int_length -=1
    
    def size(self):
        return self.int_length
    
    def deleteAll(self):
        while(self.int_length > 0):
            DLinkedList.deleteFirst(self,self.front)
        return None
    
    def sublist(self, model):
        l = []
        node = self.front
        while(node is not None): 
            l.append(node.data)
            last = node 
            node = node.next
        final_list = [i for i in l if i.model_name == model.model_name]
        return final_list
        
        
    def no_dublicate(self,new_data):
        l = []
        node = self.front
        while(node is not None): 
            l.append(node.data.vin)
            last = node 
            node = node.next
        if new_data.vin in l:
            raise ValueError('vin value already exists')
        else:
            new_node = DLinkedList.Node(new_data) 
            new_node.next = self.front 
            if self.front is not None: 
                self.front.prev = new_node 

            self.front = new_node 
            self.int_length +=1
    
    def addList(self,dll):
        node = dll.front
        if node is None:
            raise ValueError('DLinkedList is empty')
        else:    
            l = []
            while(node is not None): 
                print (node.data)
                l.append(node.data)
                last = node 
                node = node.next
            for i in l:
                new_node = DLinkedList.Node(i) 
                new_node.next = None

                if self.front is None: 
                    new_node.prev = None
                    self.front = new_node 
                    return 

                last = self.front 
                while(last.next is not None): 
                    last = last.next

                last.next = new_node  
                new_node.prev = last

        return 

# (B)
def toarray(dll,filter):
    node = dll.front
    l = []
    if node is None:
        raise ValueError('List is empty')
    else:
        while(node is not None): 
            l.append(node.data)
            last = node 
            node = node.next
    vehicleArray = [i for i in l if i.vin == filter]
    return vehicleArray
#x = toarray(dll,2)