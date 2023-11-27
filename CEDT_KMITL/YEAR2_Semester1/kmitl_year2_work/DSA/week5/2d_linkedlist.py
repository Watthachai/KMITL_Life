"""#LAB : 04"""

print("\n\nLAB : 4")


class tempStack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:   
            self.items = list
        self.size = len(self.items)
        
    def isEmpty(self):
        return self.items == []
    
    
    def left_push(self, item):
        self.items.insert(0, item)
        self.size += 1
    
    def left_pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop(0)

    def right_push(self, item):
        self.items.append(item)
        self.size += 1
    
    def right_pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop()


ts = tempStack()

print("################ 1 #################")

# Push_left
for i in "ABCD":
    ts.left_push(i)
    print(ts.items)
    
# Pop_left
while not ts.isEmpty():
    for i in ts.items:
        print(i, end="")
    print(' Remove :', ts.left_pop()) 

print("\n################ 2 #################")

#Push_right
for i in "ABCD":
    ts.right_push(i)
    print(ts.items)

#Pop_right
while not ts.isEmpty():
    for i in ts.items:
        print(i, end='')
    print(' Remove :', ts.right_pop())
    
print("\n################ 3 #################")

# Push_left
for i in "ABCD":
    ts.left_push(i)
    print(ts.items)

#Pop_right
while not ts.isEmpty():
    for i in ts.items:
        print(i, end='')
    print(' Remove :',ts.right_pop())
    
print("\n################ 4 #################")

#Push_right
for i in "ABCD":
    ts.right_push(i)
    print(ts.items)

# Pop_left
while not ts.isEmpty():
    for i in ts.items:
        print(i, end='')
    print(' Remove :', ts.left_pop()) 


print("\n\n ###################### 2D Linklist #####################")
class Node:
    #Node for 2D LinkedList
    def __init__(self):
        self.head = None
        
    def Append_primary(self, pri_data):
        new_node = primaryNode(pri_data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def Delete_primary(self, pri_data):
        current_node = self.head
        prevoius_node = None
        while current_node != None:
            if current_node.data == pri_data:
                if prevoius_node == None:
                    self.head = current_node.next
                else:
                    prevoius_node.next = current_node.next
                break
            prevoius_node = current_node
            current_node = current_node.next
    
    def Append_secondary(self, pri_data, sec_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == pri_data:
                current_node.sec_list.append(sec_data)
                break
            current_node = current_node.next
        
    def Delete_secondary(self, pri_data, sec_data):
        current_node = self.head
        previous_node = None
        while current_node != None:
            if current_node.data == pri_data:
                current_node.sec_list.remove(sec_data)
                break
            previous_node = current_node
            current_node = current_node.next
    
    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, ': ', current_node.sec_list)
            current_node = current_node.next
class primaryNode:
    def __init__(self, pri_data):
        self.data = pri_data
        self.sec_list = []
        self.next = None

class secondNode:
    def __init__(self, sec_data):
        self.data = sec_data
        

ll = Node()

ll.Append_primary('A')
ll.Append_primary('B')
ll.Append_primary('C')

ll.Append_secondary('A', 'A1')
ll.Append_secondary('A', 'A2')
ll.Append_secondary('B', 'B1')
ll.Append_secondary('B', 'B2')
ll.Append_secondary('C', 'C1')
ll.Append_secondary('C', 'C2')
ll.Delete_primary('B')


ll.print_list()