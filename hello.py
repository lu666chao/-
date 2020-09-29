import re
from collections import Counter

with open("Walden.txt","r",encoding="utf-8") as fd:
    texts = fd.read()                 #将文件内容全部变成字符串
    count = Counter(re.split(r"\W+",texts)) #单词分隔
print(count)
    