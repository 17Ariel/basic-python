from tkinter import *


app=Tk()
labelTxt=StringVar()
labelTxt=Label(app,text='Enter a text here',font=('bold',16),foreground='#333',pady=20)
labelTxt.grid(row=0,column=0)
inputField=StringVar()
inputField=Entry(app,font=('bold',16),foreground='#333')
inputField.grid(row=0,column=1)
btnsubmit
app.title('Simple Gui')
app.geometry("500x400")
app.mainloop()