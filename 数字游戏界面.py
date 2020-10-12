from tkinter import *
import random

root=Tk()

guess_num,max_n,min_n,a=0,1024,1,0


def init():
    global guess_num,max_n,min_n,a
    guess_num=0
    max_n = 1024
    min_n = 1
    a = random.randint(min_n, max_n)
    print("待猜测的数字为"+str(a))
    label_str.set("请输入你所猜的数字，数字为"+str(min_n)+"到"+str(max_n)+"之间的整数")

def guess():
    global guess_num,max_n,min_n,a             #global定义全局变量
    try:
        val=int(entry.get())
        print(val)
    except Exception as e:
        label_str.set("您的输入有误，请输入一个" + str(min_n) + "到" + str(max_n) + "之间的整数")
        print(e)
        return
    guess_num += 1
    if val>1024 or val<1:
        label_str.set("您的输入有误，请输入一个"+str(min_n)+"到"+str(max_n)+"之间的整数")
    elif val==a:
        label_str.set("恭喜您已猜中，您用了"+str(guess_num)+"次机会")
        button1["state"] = "disabled"
        button3["state"] = "active"
    elif val>a and guess_num<10:
        max_n=val
        label_str.set("请输入一个大于等于"+str(min_n)+"小于"+str(val)+"的数")
    elif val<a and guess_num<10:
        min_n=val
        label_str.set("请输入一个大于"+str(val)+"小于等于"+str(max_n)+"的数")
    else:
        label_str.set("您已经猜10次未中，请重新开始游戏")
        button1["state"]="disabled"
        button3["state"] = "active"

def retry():
    init()
    button1["state"] = "active"
    button3["state"] = "disabled"


def close():
    root.destroy()

root.title("猜数字游戏")
root.geometry("400x100+150+150")
label_str = StringVar()
label_str.set("请输入你所猜的数字，数字为"+str(min_n)+"到"+str(max_n)+"之间的整数")
label=Label(root,textvariable=label_str)
entry=Entry(root,width=30,fg="red")
entry.place(relx=0.1,rely=0.5)               #按钮的参数，定义不同的按钮位置
button1=Button(root,text="猜",command=guess)
button1.place(relx=0.65,rely=0.45)
button2=Button(root,text="关闭",command=close)
button2.place(relx=0.75,rely=0.45)
button3=Button(root,text="重新开始",command=retry)
button3.place(relx=0.85,rely=0.45)
button3["state"]="disabled"
label.pack()

init()

root.mainloop()