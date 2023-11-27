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

    # ผสมสองส่วนของ string ด้วยการกรีดไพ่
    result = ''
    while not q1.is_empty() and not q2.is_empty():
        result += q1.dequeue()
        result += q2.dequeue()

    # เพิ่มตัวอักษรที่เหลือใน queue (ถ้ามี)
    while not q1.is_empty():
        result += q1.dequeue()
    while not q2.is_empty():
        result += q2.dequeue()

    return result

# ทดสอบฟังก์ชัน shuffle_string
print(shuffle_string('ABCDEFGH'))  # Output: AEBFCGDH
