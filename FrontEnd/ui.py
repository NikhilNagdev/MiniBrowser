
from tkinter import *

from FrontEnd.test import BrowseImage

def buttonEventHandler(self):
    browe = BrowseImage(e1.get())
    print(browe.getURL())



root = Tk()
root.title("Image browser")
f = Frame(root, width=800, height=600)
f.pack()
e1 = Entry(f, font=('Arial', 18))

l1 = Label(f, text="Username: ", borderwidth=2, relief="solid", width=35, height=10, font=('Arial', 14))
l2 = Label(f, text="Username: ", borderwidth=2, relief="solid", width=35, height=10, font=('Arial', 14))
l3 = Label(f, text="Username: ", borderwidth=2, relief="solid", width=35, height=10, font=('Arial', 14))
l4 = Label(f, text="Username: ", borderwidth=2, relief="solid", width=35, height=10, font=('Arial', 14))
e1.place(x=0, y=5, width=690, height=25)
l1.place(x=0, y=100)
l2.place(x=400, y=100)
l3.place(x=0, y=340)
l4.place(x=400, y=340)
b = Button(f, text="Search", width=12, height=1)
b.place(x=700, y=5)
b.bind('<Button>', buttonEventHandler)
root.mainloop()
