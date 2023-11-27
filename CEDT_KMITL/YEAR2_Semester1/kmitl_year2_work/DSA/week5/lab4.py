class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def insert_after(self, target, data):
        if self.head is None:
            return
        current = self.head
        while current and current.data != target:
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

# สร้าง linked list และเพิ่มข้อมูล ABCDEF
ll = LinkedList()
for char in "ABCDEF":
    ll.insert(char)

print("Original Linked List: ", ll.display())

# แทรกข้อมูล XYZ ระหว่าง C และ D
ll.insert_after("C", "XYZ")

print("Linked List after inserting XYZ: ", ll.display())