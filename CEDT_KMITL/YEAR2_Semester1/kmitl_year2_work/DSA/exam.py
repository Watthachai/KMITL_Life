"""
Program 1:
ให้นักศึกษาเขียนโปรแกรม สร้าง Class Queue และรับ input เป็น string แล้วทำการสลับตำแหน่งตัวอักษร
แบบกรีดไพ่ โดยใช้ Queue
ตัวอย่าง
Input: ABCDEFGH
Output : AEBFCGDH
"""
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

def shuffle_string(s):
    q1 = Queue()
    q2 = Queue()

    # แบ่ง string เป็นสองส่วน
    for i in range(len(s)):
        if i < len(s) / 2:
            q1.enqueue(s[i])
        else:
            q2.enqueue(s[i])

    # ผสมสองส่วนของ string
    result = ''
    while not q1.is_empty() and not q2.is_empty():
        result += q1.dequeue()
        result += q2.dequeue()

    # เพิ่มตัวอักษรที่เหลือใน queue
    while not q1.is_empty():
        result += q1.dequeue()
    while not q2.is_empty():
        result += q2.dequeue()

    return result
str_input = input("Input string: ")
print(shuffle_string(str_input))

"""
Program 2:
ให้นักศึกษาเขียนโปรแกรม สร้าง Class Stack และรับ input เป็น expression ทางคณิตศาสตร์ แล้วทำการตรวจสอบ expression ว่ามีการเติมวงเล็บถูกต้องหรือไม่โดยใช้ Stack
ตัวอย่าง
Input : (1+(2-3))
Output : True
ตัวอย่าง
Input : 1+(2*3)-4)
Output : False
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def is_balanced(expression):
    s = Stack()
    for char in expression: 
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()

str_input = input("Input expression: ")
print(is_balanced(str_input)) 



"""
Program 3:
เขียนโปรแกรมรับ input เป็น string และ keyword แล้วหาตำแหน่งของ Keyword ใน string ถ้าไม่พบให้ แสดงผล -1 โดยไม่ใช้ฟังก์ชัน find
Input string : hello world
Input Keyword: world
Output : 6
Input string : hello world
Input Keyword: word
Output: -1 
"""
def find_keyword(string, keyword):
    len_string = len(string) 
    len_keyword = len(keyword)

    for i in range(len_string - len_keyword + 1):
        if string[i:i+len_keyword] == keyword: 
            return i 

    return -1

input_string = input("Input string: ")
input_keyword = input("Input keyword: ")
result = find_keyword(f'{input_string}', f'{input_keyword}')
print(result)

