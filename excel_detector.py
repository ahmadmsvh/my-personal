import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile


class ExcelDetector:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x500')
        self.lable = Label(self.root, text='result:')
        self.lable.pack()
        self.textbox = Text(self.root, height=10, width=100)
        self.textbox.pack(padx=30, pady=10)
        self.numbers_list = []

        self.detbtn = Button(self.root, text='Detect',
                         width=20, command=lambda: self.startDetecting())
        self.detbtn.pack(pady=30)

        self.upbtn = Button(self.root, text='Upload File',
                       width=20, command=lambda: self.upload_file())
        self.upbtn.pack(pady=2)


        self.root.mainloop()

    def upload_file(self):
        self.upbtn = Button(self.root, text='Upload File',
                         width=20, command=lambda: self.upload_file())
        self.upbtn.pack(pady=2)

        file = filedialog.askopenfilename()
        data = pd.read_excel(file)
        self.numbers_list.extend(data['شماره کارت'])


    def startDetecting(self):
        number_set = set(self.numbers_list)
        result = []

        for number in number_set:
            result.append([number, self.numbers_list.count(number)])

        df = pd.DataFrame(result, columns=['شماره کارت', 'تکرار'],
                          index=range(1, len(number_set) + 1))

        df = df.sort_values(by='تکرار', ascending=False)
        # df.to_excel(f'{directory}/result/result.xlsx', index=False, header=False)
        self.textbox.insert('1.0', f'{df}')
        return df


if __name__ == '__main__':
    detector = ExcelDetector()