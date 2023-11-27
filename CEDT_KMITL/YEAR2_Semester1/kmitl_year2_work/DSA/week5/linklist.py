class Node:
    def __init__(self, data, next = None):
        self.data = data
        
        if next is None:
            self.next = None
        else:
            self.next = next

class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            s_now = self.head
            while s_now.next:
                s_now = s_now.next
            s_now.next = new_node
    
    def node_print(self):
        elements = []
        s_now_node = self.head
        while s_now_node:
            elements.append(s_now_node.data)
            s_now_node = s_now_node.next
        return elements

    def insert_after(self, target_data, data):
        if self.head is None:
            return
        s_now = self.head
        while s_now and s_now.data != target_data:
            s_now = s_now.next
        new_node = Node(data)
        new_node.next = s_now.next
        s_now.next = new_node
        
ll = List()
for i in "ABCDEF":
    ll.append(i)
    
print("\n\n#Activities 3 \nList:", ll.node_print())

ll.insert_after("C", "X")
ll.insert_after("X", "Y")
ll.insert_after("Y", "Z")

print("Insert LL After", ll.node_print())