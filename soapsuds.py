#Importing tkinter module
from tkinter import *

from tkinter.ttk import *
#Initializing window
window = Tk()
#Application title, dimensions, misc
window.title("Soap Suds")
window.geometry('500x300')
#Sets background image
img = PhotoImage(file="soapbg.png")
Label = Label(
    window,
    image=img
)
Label.place(x=0, y=0)
#Holds selection integer for choices
selected = IntVar()

rad1 = Radiobutton(window,text='Soap', value=1, variable=selected)

rad2 = Radiobutton(window,text='Candles', value=2, variable=selected)

rad3 = Radiobutton(window,text='Bath Bombs', value=3, variable=selected)
#Sets up the submit button to retrieve selected number
def clicked():

   print(selected.get())

btn = Button(window, text="Sumbit", command=clicked)
#Sets alignment and spacing on GUI for choices
rad1.grid(column=0, row=0)

rad2.grid(column=1, row=2)

rad3.grid(column=2, row=4)

btn.grid(column=3, row=5)

window.mainloop()