import random
keys = [2019660101,2019660102,2019660103,2019660104,2019660105,2019660106,2019660107,2019660108,2019660109,2019660110,2019660111,2019660112,2019660113,2019660114,2019660115,2019660116,2019660117,2019660119,2019660120,2019660121,2019660122,2019660123,2019660124,2019660125,2019660126,2019660127,2019660128]
values = ['周嘉铖','钱珑超','徐展','尤桉哲','钱涛','黄舒怡','胡志辉','吴昭耀','陈萌萌','郑巧悦','陈艳','梁明皓','蒋俊超','徐颖','倪宏涛','潘梦倩','王中阳','毛贞强','张嫒','朱速航','陈涛','陆元超','叶振雄','奚申杰','叶梦婷','徐丽丽','潘艳']
mydict= dict(zip(keys,values))
i = 1
list1 = []
list2 = []
while i < 4:
    a = random.choice(list(mydict))
    list1.append(a)
    list2.append(mydict.get(a))
    i+=1
print(list1,list2)