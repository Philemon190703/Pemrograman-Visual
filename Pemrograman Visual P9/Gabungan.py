from tkinter import *

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
menubar = Menu(root)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# Checkbuttons
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(root, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()

# User Name Entry
user_frame = Frame(root)
user_frame.pack(fill=X, padx=10, pady=5)
L1 = Label(user_frame, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(user_frame, bd=5)
E1.pack(side=LEFT)

# Frame
button_frame = Frame(root)
button_frame.pack(padx=10, pady=5)
redbutton = Button(button_frame, text="Red", fg="red")
redbutton.pack(side=LEFT)
greenbutton = Button(button_frame, text="Brown", fg="brown")
greenbutton.pack(side=LEFT)
bluebutton = Button(button_frame, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)
blackbutton = Button(button_frame, text="Black", fg="black")
blackbutton.pack(side=LEFT)

# Label
var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
var.set("Hey!? How are you doing?")
label.pack(padx=10, pady=5)

# Listbox
Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack(padx=10, pady=5)

# Menu Button
mb = Menubutton(root, text="condiments", relief=RAISED)
mb.pack(padx=10, pady=5)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

# Radiobuttons
radio_frame = Frame(root)
radio_frame.pack(padx=10, pady=5, anchor=W)
var = IntVar()
R1 = Radiobutton(radio_frame, text="Option 1", variable=var, value=1, command=sel)
R1.pack(anchor=W)
R2 = Radiobutton(radio_frame, text="Option 2", variable=var, value=2, command=sel)
R2.pack(anchor=W)
R3 = Radiobutton(radio_frame, text="Option 3", variable=var, value=3, command=sel)
R3.pack(anchor=W)

root.mainloop()