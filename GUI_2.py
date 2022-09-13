from tkinter import *
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Excel Detector')

        self.lable = Label(self.root, text='your message')
        self.textbox = Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = IntVar()

        self.check = Checkbutton(self.root, text='show message', variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = Button(self.root, text='show message', command=self.showMessage)
        self.button.pack()
        self.root.mainloop()

    def showMessage(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', END))
        else:
            messagebox.showinfo(title='message', message=self.textbox.get('1.0', END))

    def shortcut(self, event):
        print(event)
        print(event.keycode)
        if event.keycode == 36:
            self.showMessage()

gui = MyGUI()