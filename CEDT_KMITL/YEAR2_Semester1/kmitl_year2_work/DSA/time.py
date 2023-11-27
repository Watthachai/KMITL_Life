import time

# โปรแกรมที่ 1
st = time.time()
for i in range(1000000):
    x = i**2
en = time.time()
elapsed_time1 = en - st
print('Execution time of program 1:', elapsed_time1, 'seconds')

# โปรแกรมที่ 2
st = time.time()
for i in range(1000000):
    x = i**3
en = time.time()
elapsed_time2 = en - st
print('Execution time of program 2:', elapsed_time2, 'seconds')
