filename = 'demo.py'
  
with open(filename,'r',encoding='utf-8') as fp:
     lines = fp.readlines()          #读取所有行
  
  
maxLength = max(map(len,lines)) #获取最长的行的长度
print(maxLength)
  #遍历所有行
for index,line in enumerate(lines):
     newLine = line.rstrip()            #删除每行右侧的空白字符
     newLine = newLine + ' ' * (maxLength - len(newLine))   #在每行右侧填充空格
     newLine = newLine + '#' + str(index + 1) + '\n'            #在每行右侧增加行号
    lines[index] = newLine                                     #把新组装的行放到列表中

#把新组装的列中写入到demo_new.py文件中
with open('demo_new.py','w',encoding='UTF-8') as fp:
     fp.writelines(lines)
