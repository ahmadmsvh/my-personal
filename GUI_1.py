from tkinter import *

root = Tk()

root.geometry("800x500")
root.title("My First GUI")

lable = Label(root, text='hello world!', font=('Arial', 18))
lable.pack(padx=50, pady=50)

textbox = Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=30)

button = Entry(root)
button.pack()

my_btn = Button(root, text='Click Me!', font=('Arial', 14))
my_btn.pack()

buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=2)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = Button(buttonframe, text='one')
btn1.grid(row=0, column=0, sticky=W+E)

btn2 = Button(buttonframe, text='two')
btn2.grid(row=1, column=1, sticky=W+E)

btn3 = Button(buttonframe, text='three')
btn3.grid(row=2, column=2, sticky=W+E)

# another_button = Button(root, text='placed btn')
# another_button.place(x=200, y=200, height=100, width=150)

buttonframe.pack(fill='x', padx=20)


root.mainloop()