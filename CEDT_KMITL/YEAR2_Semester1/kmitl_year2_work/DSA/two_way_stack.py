# ให้นักศึกษาสร้าง class ที่มีการทำงานเป็น 2 way stack ที่สามารถ push/pop ได้จาก 2 ทิศทาง พร้อมทั้งสร้าง method
# push_left() push ข้อมูลทางซ้าย
# push_right() push ข้อมูลทางขวา
# pop_left() pop ข้อมูลทางซ้าย
# pop_right() pop ข้อมูลทางขวา
# isEmpty() สำหรับตรวจสอบว่า stack ว่างหรือไม่
# stackdat() สำหรับแสดง list ที่เก็บข้อมูล
# พร้อมทั้งทดสอบการใช้งานเช่น


class twoWayStack:

    def __init__(self):
        self.dat = []
        
    def isEmpty(self):
        if len(self.dat) == 0:
            return True
        else: 
            return False

    def push_left(self, data):
            return self.dat.insert(0, data)
        
    def push_right(self, data):
            return self.dat.append(data)

    def pop_left(self):
        return self.dat.pop(0)

    def pop_right(self):
        return self.dat.pop()

    def stackdat(self):
        return self.dat

stk = twoWayStack()
stk.push_left(2)
stk.push_right(5)
stk.push_left(4)
stk.push_right(10)
print(stk.stackdat())  # [4, 2, 5, 10]
print(stk.pop_right())  # 10
print(stk.pop_left())  # 4
print(stk.pop_right())  # 5
print(stk.pop_right())  # 2
print(stk.stackdat())  # []
