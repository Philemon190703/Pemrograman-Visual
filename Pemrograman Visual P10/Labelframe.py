from tkinter import *

root = Tk()

LabelFrame = LabelFrame(root, text="This is a Labelframe")
LabelFrame.pack(fill="both", expand="yes")

left = Label(LabelFrame, text="Inside the Labelframe")
left.pack()

root.mainloop()