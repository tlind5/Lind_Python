from tkinter import *
from tkinter.ttk import *
import time

ws = Tk()
ws.title('Progress Bar')
ws.geometry('400x250+1000+300')


def step():
    for i in range(50):
        ws.update_idletasks()
        pb1['value'] += 2

        time.sleep(.2)


pb1 = Progressbar(ws, orient=HORIZONTAL, length=100, mode='determinate')
pb1.pack(expand=True)

Button(ws, text='Start', command=step).pack()

ws.mainloop()