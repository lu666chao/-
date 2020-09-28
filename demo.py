len_max = 0
text1t = []
space = ''
new_list = []
file = open('C:\\Users\lyc\AppData\Roaming\JetBrains\PyCharmCE2020.1\scratches\demo.py','r')
file_txt = file.readlines()
file.close()
text_list = len(file_txt)
for text in file_txt:
    text_str = len(text)
    if text_str > len_max:
        len_max = text_str
    if text[-1] == '\n':
        text_list.append(text[:-1])
    else:
        text_list.append(text)
for new_text in text_list:
    while True:
        if len(new_text)+len(space) == len_max:
            new_list.append(new_text+space+'#')
            space = ''
            break
        else:
            space += ' '

demo_file = open('C:\\Users\lyc\AppData\Roaming\JetBrains\PyCharmCE2020.1\scratches\demo_new.py', 'w')
for i in range(1,text_list):
    demo_file.write(new_list[i-1]+str(i)+'\n')
demo_file.close()