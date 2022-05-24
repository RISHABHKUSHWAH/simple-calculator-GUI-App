from tkinter import Tk,PhotoImage,Entry,StringVar,Frame,Button,LEFT,X

root = Tk()
root.geometry("400x550")
photo = PhotoImage(file="icons8-calculator-48.png")
root.iconphoto(False, photo)

# root.iconbitmap(r'C:\Users\kushwah\Desktop\python_demo\tkinter\Dtafalonso-Android-Lollipop-Calculator.ico')
root.title("Simple Calculator")


def click(event):
    global entvalue
    text = event.widget.cget("text")
    try:
        if text == "=":
            if entvalue.get().isdigit():
                value = int(entvalue.get())
            else:
                value = eval(ent.get())
            entvalue.set(value)
            ent.update()
        elif text == "C":
            entvalue.set("")
            ent.update()
        else:
            entvalue.set(entvalue.get() + text)
            ent.update()
   # handles zerodivision exception
    except ZeroDivisionError:
        #print("Can't divide by zero") 
        entvalue.set("Can't divide by 0")
        ent.update()
entvalue = StringVar()
entvalue.set("")
ent = Entry(root, textvariable=entvalue, font="Calibri 40 bold")
ent.pack(fill=X, padx=10, pady=10, ipadx=10)
# Frame one
f = Frame(root, bg='grey')
b = Button(f, text='9', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='8', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='7', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='*', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

# Frame second
f = Frame(root, bg='grey')
b = Button(f, text='6', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='5', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='4', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='/', padx=21, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

# Frame third
f = Frame(root, bg='grey')
b = Button(f, text='3', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='2', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='1', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='+', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()

# Frame fourth
f = Frame(root, bg='grey')
b = Button(f, text='C', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='0', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='=', padx=20, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = Button(f, text='-', padx=23, pady=20, font="Calibri 25 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()
