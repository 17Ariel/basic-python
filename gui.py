from tkinter import *
from tkinter import ttk


app=Tk()

def clickMsg():
    print('hello')
ttk.Entry(app).grid()
ttk.Button(app,text="Click Me",command=clickMsg).grid()
ttk.Label(app,text="0").grid
app.mainloop()

