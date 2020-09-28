import math
import numpy
i = 0
j = 0
n = 0
m = 0
list1 = []
a = int(input("请输入矩形个数："))   #矩形个数越多结果越准确
if a < 5:                   #5个起步太少了不精确
    print("请重新输入")
else:
    b = math.pi//a
    for i in range(0,2*math.pi,b):
        list1.append(abs(math.sin(i)))
    while j <= len(list1):
        n+=int(list1(j))
        j+=1
    m = n*2*math.pi
    print(m)



