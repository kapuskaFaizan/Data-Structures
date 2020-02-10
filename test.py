from queue_using_linkedList_1 import QueueADT,addYear
from queue_using_rawArray_2 import QueueADT2
from stack_arrayBased_1 import StackADT,countMake

from stack_DLinkedList_2 import StackADT2
from D_LinkedList import DLinkedList,vehicle_model,toarray

    
v = vehicle_model(1,'audi',2010)
v1= vehicle_model(2,'bmw',2010)
v2= vehicle_model(3,'mercedes',2010)
v3= vehicle_model(4,'jaguar',2010)

print('solution for d')

print('addYear')

x = QueueADT(2)
x.enQueue(v)
x.enQueue(v1)
print('queue data before adding year',x.items)
y = addYear(x) 
print('queue data after adding year',y.items)   

print(60 *'#')

print('countMake')

s = StackADT()
s.push(v)
s.push(v1)
print('items is stack',s.items) 
c = countMake(s,'bmw')

print('items after coutMake with bmw',c.items)

print(60*'#')

print('solution of c')

s = StackADT()
s.push(v)
s.push(v1)

print('values in stack', s.items)

print('peek value for stack', s.peek())

q = QueueADT(2)
q.enQueue(v)
q.enQueue(v1)
q.enQueue(v2)
print('values in queue',q.items)
print('peek value of queue',q.peek())

print(' solution for b')

dll = DLinkedList()
dll.addFirst(v2)
dll.addLast(v3)

print('items in DLL')

dll.printNextLine(dll.front)

x = toarray(dll,3)

print('DLL in array form', x)

print('solution for a')

print('items in DLinkedList')

dll.printNextLine(dll.front)

print('data model passed is v3')

m = dll.sublist(v3)

print('data in sublist',m)

print('data in dll')
dll.printNextLine(dll.front)

print('no_dublicate entry')
print('output will be an error , dont freak out')

dll.no_dublicate(v3)