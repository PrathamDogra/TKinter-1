from Tkinter import *
t=Tk()
#declaring the variables
value=0
switch_val=StringVar()
switch_val.set(str(value))
button_text=StringVar()
button_colour=StringVar()
button_text.set("Start")
delay=400
count=False
def switch():
    #the function that gets executed when the button is pressed
    global count,button_text
    count=not count  #Stops to count if counting and vice-versa
    button_text.set("Start" if not count else"Stop")

def update():
    #function to update the values or keep the counter going
    global value,switch_val,button_text,delay,count
    if count:
        value+=1
        switch_val.set(str(value))

    t.after(delay,update)
label=Label(t,textvariable=switch_val,bg="blue",fg="white")  #bg=background colour
label.pack(fill=X)  #fill=X will fill it in X direction no matter how long you pull it
button=Button(t,textvariable=button_text,command=switch,fg="red")
button.pack(fill=X)
t.after(10,update)   # The counter starts
t.mainloop()