class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

def infix_to_postfix(infix_expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = Stack()
    postfix = []
    num_operands = 0
    num_operations = 0

    for char in infix_expression:
        if char.isalpha():
            postfix.append(char)
            num_operands += 1
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.stack[-1] != '(':
                postfix.append(stack.pop())
                num_operations += 1
            stack.pop()
        else:
            while (not stack.isEmpty() and stack.stack[-1] != '(' and precedence[char] <= precedence[stack.stack[-1]]):
                postfix.append(stack.pop())
                num_operations += 1
            stack.push(char)

    while not stack.isEmpty():
        postfix.append(stack.pop())
        num_operations += 1

    return ''.join(postfix), num_operations, num_operands

print(infix_to_postfix("a+b*c-d"))
print(infix_to_postfix("a+b*c-(d/e+f)*g"))
print(infix_to_postfix("(a+b)*c/d"))


class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.isEmpty():
            current = self.head
            string = str(current.data)
            while current.next:
                current = current.next
                string += ' -> ' + str(current.data)
            return string
        else:
            return 'List is empty'

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.Node(data)

    def remove(self, data):
        if not self.isEmpty():
            if self.head.data == data:
                self.head = self.head.next
            else:
                current = self.head
                while current.next and current.next.data != data:
                    current = current.next
                if current.next:
                    current.next = current.next.next

    def add(self, data):
        if not self.head or data <= self.head.data:
            self.head = self.Node(data, self.head)
        else:
            current = self.head
            while current.next and data > current.next.data:
                current = current.next
            new_node = self.Node(data, current.next)
            current.next = new_node

L1 = LinkedList()
L1.add(5)
print(L1)
L1.add(9)
print(L1)
L1.add(7)
print(L1)
L1.add(3)
print(L1)
L1.add(11)
print(L1)


from collections import Counter

class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.isEmpty():
            current = self.head
            string = str(current.data)
            while current.next:
                current = current.next
                string += ' -> ' + str(current.data)
            return string
        else:
            return 'List is empty'

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.Node(data)

    def remove(self, data):
        if not self.isEmpty():
            if self.head.data == data:
                self.head = self.head.next
            else:
                current = self.head
                while current.next and current.next.data != data:
                    current = current.next
                if current.next:
                    current.next = current.next.next

    def add(self, data):
        if not self.head or data <= self.head.data:
            self.head = self.Node(data, self.head)
        else:
            current = self.head
            while current.next and data > current.next.data:
                current = current.next
            new_node = self.Node(data, current.next)
            current.next = new_node

def calculate_statistics(numbers):
    L1 = LinkedList()
    for number in numbers:
        L1.add(number)

    print("LinkedList data:", L1)

    mean = sum(numbers) / len(numbers)
    print("Mean =", mean)

    counter = Counter(numbers)
    max_count = max(list(counter.values()))
    mode_val = [num for num, freq in counter.items() if freq == max_count]
    if len(mode_val) == len(numbers):
        print("No mode found")
    else:
        print("Mode =", ', '.join(map(str, mode_val)))

    numbers.sort()
    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers)//2]
        median2 = numbers[len(numbers)//2 - 1]
        median = (median1 + median2)/2
    else:
        median = numbers[len(numbers)//2]
    print("Median =", median)

numbers1 = [7, 9, 3, 2, 1, 2, 3, 4, 8, 9, 3, 15]
calculate_statistics(numbers1)

numbers2 = [7, 6, 74, 44, 6, 37, 55, 35, 3, 31, 3, 10]
calculate_statistics(numbers2)

