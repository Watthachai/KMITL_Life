def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# กำหนดให้ตัวแปร data เป็นค่า list ของค่าสุ่ม
import random
rnddat = [random.randint(1,1000) for i in range(0,1000000)]

# เรียงลำดับตัวเลขใน rnddat จากน้อยไปมาก
sorted_rnddat = bubble_sort(rnddat)
