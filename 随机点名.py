import tkinter
import tkinter.messagebox
import random
import threading
import itertools
import time


def closeWindow():
    root.flag = False
    time.sleep(0.1)  # 延迟0.1秒执行
    root.destroy()


def clickStart():
    t = threading.Thread(target=shuffleUsers)
    t.start()
    btnStart['state'] = 'disabled'
    btnStop['state'] = 'normal'


def clickStop():
    global times
    root.flag = False  # 暂停线程
    time.sleep(0.1)
    times += 1
    tkinter.messagebox.showinfo(title="Congratulations!", message=str(times) + ": " + showLabel['text'])
    btnStart['state'] = 'normal'
    btnStop['state'] = 'disabled'


def shuffleUsers():  # 开始洗牌线程
    root.flag = True
    t = users[:]
    random.shuffle(t)
    t = itertools.cycle(t)
    while root.flag:
        showLabel['text'] = next(t)
        time.sleep(0.1)


root = tkinter.Tk()
root.title("Name Shuffle")
root.geometry("400x400+480+200")
root.resizable(False, False)

root.flag = False  # 线程状态
times = 0
users = ['周嘉铖','钱珑超','徐展','尤桉哲','钱涛','黄舒怡','胡志辉','吴昭耀','陈萌萌','郑巧悦','陈艳','梁明皓','蒋俊超','徐颖','倪宏涛','潘梦倩','王中阳','毛贞强','张嫒','朱速航','陈涛','陆元超','叶振雄','奚申杰','叶梦婷','徐丽丽','潘艳']

btnStart = tkinter.Button(root, text='Start', command=clickStart)
btnStart.place(x=30, y=10, width=80, height=20)

btnStop = tkinter.Button(root, text='Stop', command=clickStop)
btnStop['state'] = 'disabled'
btnStop.place(x=300, y=10, width=80, height=20)

showLabel = tkinter.Label(root, text='')
showLabel['fg'] = 'red'
showLabel.place(x=150, y=180, width=100, height=20)

root.protocol("WM_DELETE_WINDOW", closeWindow)
root.mainloop()