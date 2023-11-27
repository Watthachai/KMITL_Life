def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# กำหนดให้ตัวแปร data มีค่าเป็น list ของตัวเลข 1-1,000,000
import random
dat = list(range(1,1000001))

# รับ input เป็นตัวเลข 1 ตัว
target = int(input("Enter a number to search: "))

# ค้นหาตำแหน่งของตัวเลขใน dat
index = binary_search(dat, target)
if index != -1:
    print(f"The number {target} is found at index {index}")
else:
    print(f"The number {target} is not found in the list")
