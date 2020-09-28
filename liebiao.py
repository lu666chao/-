from collections import Counter  #引入Counter
lst = eval(input('请输入列表lst:'))
a = dict(Counter(lst))
b = []
print ([key for key,value in a.items()if value > 1 ]) #展示重复元素
b=[key for key in(lst+a) if key not in list1]
print(b)