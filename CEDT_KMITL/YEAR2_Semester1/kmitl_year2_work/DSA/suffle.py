#
# เขียนฟังก์ชั่น Shuffle string 2 ชุดให้กลายเป็นชุดเดียว เช่น
# input = "abc","def"
# output = "adbecf"
# โดยใช้ queue 2 ชุด ช่วยในการสลับตัวอักษร
#

from queue import Queue


def shuffle(string1, string2):
    q1 = Queue(maxsize=50)
    for s in string1:
        q1.put(s)

    q2 = Queue(maxsize=50)
    for s in string2:
        q2.put(s)

    ret = ""

    if len(string1) >= len(string2):
        for i in range(len(string1)):
            if not q1.empty() and not q2.empty():
                ret += q1.get() + q2.get()
            else:
                ret += q1.get()
    else:
        for i in range(len(string2)):
            if not q2.empty() and not q1.empty():
                ret += q1.get() + q2.get()
            else:
                ret += q2.get()

    return ret


st1 = "abcdefghhhhhhhhhhhhh"
st2 = "ABCDEFGasssssssssssssssdasdw"
print(shuffle(st1, st2))  # aAbBcCdDeEfFgG