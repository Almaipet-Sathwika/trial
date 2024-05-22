from tkinter import *
import math as m
root=Tk()
root.title('Calculator')
#root.geometry("250x330")
root.maxsize(250,330)
root.minsize(250,330)
frame=Frame(master=root,bg='lavender',padx=10)
frame.pack()
#entry bar 
entry=Entry(master=frame,relief=SUNKEN,width=30,borderwidth=3)
entry.grid(row=0,column=0,columnspan=4,pady=10,ipady=3,ipadx=5,padx=10)

#display in frame
def click(n):
    entry.insert(END,n)

def equal():
    try:
        r=str(eval(entry.get()))
        entry.delete(0,END)
        entry.insert(0,r)
    except:
        entry.delete(0,END)
        entry.insert(0,'Error')
        #help
        

def all_clear():
    entry.delete(0,END)

def back():
    pass
#need help here



#buttons-b
b1=Button(master=frame,text='1',padx=10,pady=10,width=4,command=lambda: click('1'))
b1.grid(row=2,column=0)

b2=Button(master=frame,text='2',padx=10,pady=10,width=4,command=lambda: click('2'))
b2.grid(row=2,column=1)

b3=Button(master=frame,text='3',padx=10,pady=10,width=4,command=lambda: click('3'))
b3.grid(row=2,column=2)

b4=Button(master=frame,text='4',padx=10,pady=10,width=4,command=lambda: click('4'))
b4.grid(row=3,column=0)

b5=Button(master=frame,text='5',padx=10,pady=10,width=4,command=lambda: click('5'))
b5.grid(row=3,column=1)

b6=Button(master=frame,text='6',padx=10,pady=10,width=4,command=lambda: click('6'))
b6.grid(row=3,column=2)

b7=Button(master=frame,text='7',padx=10,pady=10,width=4,command=lambda: click('7'))
b7.grid(row=4,column=0)

b8=Button(master=frame,text='8',padx=10,pady=10,width=4,command=lambda: click('8'))
b8.grid(row=4,column=1)

b9=Button(master=frame,text='9',padx=10,pady=10,width=4,command=lambda: click('9'))
b9.grid(row=4,column=2)

b0=Button(master=frame,text='0',padx=10,pady=10,width=4,command=lambda: click('0'))
b0.grid(row=5,column=1)

#operators
plus_button=Button(master=frame,text='+',padx=10,pady=10,width=4,command=lambda: click('+'))
plus_button.grid(row=4,column=3)

minus_button=Button(master=frame,text='-',padx=10,pady=10,width=4,command=lambda: click('-'))
minus_button.grid(row=3,column=3)

mul_button=Button(master=frame,text='x',padx=10,pady=10,width=4,command=lambda: click('*'))
mul_button.grid(row=2,column=3)

div_button=Button(master=frame,text='/',padx=10,pady=10,width=4,command=lambda: click('/'))
div_button.grid(row=1,column=3)

per_button=Button(master=frame,text='%',padx=10,pady=10,width=4,command=lambda: click('%'))
per_button.grid(row=1,column=2)

equ_button=Button(master=frame,text='=',padx=10,pady=10,width=4,command=lambda: click('='))
equ_button.grid(row=5,column=3)

par1_button=Button(master=frame,text='(',padx=10,pady=10,width=4,command=lambda: click('('))
par1_button.grid(row=5,column=0)

par2_button=Button(master=frame,text=')',padx=10,pady=10,width=4,command=lambda: click(')'))
par2_button.grid(row=5,column=2)

dot_button=Button(master=frame,text='.',padx=10,pady=10,width=4,comman=lambda: click('.'))
dot_button.grid(row=1,column=1)

#special buttons
ac=Button(master=frame,text='AC',padx=10,pady=10,width=4,command=all_clear)
ac.grid(row=1,column=0)

equ_button=Button(master=frame,text='=',padx=10,pady=10,width=4,command=equal)
equ_button.grid(row=5,column=3)


#sq, sqrt
sqr_b=Button(master=frame,text='Sqrt',padx=10,pady=10,width=4,command=lambda: click('**1/2'))
sqr_b.grid(row=6,column=0)

sq_b=Button(master=frame,text='Sq',padx=10,pady=10,width=4,command=lambda: click('**2'))
sq_b.grid(row=6,column=1)

cbr_b=Button(master=frame,text='cbrt',padx=10,pady=10,width=4,command=lambda: click('**1/3'))
cbr_b.grid(row=6,column=2)

cb_b=Button(master=frame,text='cb',padx=10,pady=10,width=4,command=lambda: click('**3'))
cb_b.grid(row=6,column=3)

root.mainloop()
