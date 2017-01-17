from Tkinter import*
t=Tk()
'''
E1 = variable 1
E2 = variable 2
E3 = Result
'''
def add():
    #Function to add
    try:
        E3.delete(0, END)   #Deletes the value present in result column
        m=int(E1.get())     #Takes variable 1 as input
        n=int(E2.get())     #Takes variable 2 as input
        sum=m+n
        E3.delete(0,END)
        E3.insert(10,sum)   #Puts addition in result Entry
    except:                 #Excpets error if entered values are not integers
        E3.insert(10,"ValueError")

def sub():
    #Same here
    try:
        E3.delete(0, END)
        m=int(E1.get())
        n=int(E2.get())
        diff=m-n
        E3.delete(0,END)
        E3.insert(10,diff)
    except:
        E3.insert(10,"ValueError")

def mul():
    try:
        E3.delete(0, END)
        m=int(E1.get())
        n=int(E2.get())
        prod=m*n
        E3.delete(0,END)
        E3.insert(10,prod)
    except:
        E3.insert(10,"ValueError")

def div():
    try:
        E3.delete(0, END)
        m=int(E1.get())
        n=int(E2.get())
        division=m/n
        E3.delete(0,END)
        E3.insert(10,division)
    except ValueError:
        E3.insert(10,"ValueError")
    except ZeroDivisionError:
        E3.insert(10,"Can't Divide")

UpperFrame=Frame(t)                 #Defining frame, it is useful when you
                                    # want some fields to be present in specified locaions
UpperFrame.pack()
MiddleFrame=Frame(t)
MiddleFrame.pack()                  #Window is divided into 2 invisible frames Upperframe and MiddleFrame
t.geometry("500x200")               #Specifying Window height
label1=Label(t,text="Variable 1",fg="blue")   #fg=foreground colour, basically font colour
label1.pack(side=LEFT)
E1=Entry(t,width=20)
E1.pack(side=LEFT,padx=10,pady=10)

E2=Entry(t,width=20)
E2.pack(side=RIGHT,padx=10,pady=10)   #padx, pady is the boundaru or the minimum distance to the nearest object
label2=Label(t,text="Variable 2",fg="blue")
label2.pack(side=RIGHT)
button1=Button(UpperFrame,text="Addition",command=add,fg="red")  #All for buttons command= the function it calls, note no () after function
button1.pack(fill=X,pady=2)
button2=Button(UpperFrame,text="Subtraction",command=sub,fg="blue")
button2.pack(fill=X,pady=2)
button3=Button(UpperFrame,text="Multiplication",command=mul,fg="purple")
button3.pack(fill=X,pady=2)
button4=Button(UpperFrame,text="Division",command=div,fg="green")
button4.pack(fill=X,pady=2)
E3=Entry(MiddleFrame,width=20)
E3.pack(side=LEFT,fill=X,padx=10,pady=10)
E3.insert(10,"Result")
t.mainloop()