import csv
import tkinter as tk
from tkinter import messagebox
from matplotlib import animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from datetime import datetime as dt

def GUI():
    print('Start')


def openCSV():
    global file_writer
    try:
        with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Data Analytics\AGV Data.csv', mode='a', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    except IOError:
        with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Data Analytics\AGV Data.csv', mode='w+', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow("Alpha")
            file_writer.writerow("Beta")

        print('The file could not be opened')


    #for i in range(len(df)):
     #    print(df[i])

def click():
    global enteredText1
    enteredText1= entryUserName.get()
    entryUserName.delete(0,len(enteredText1))

    global enteredText2
    enteredText2= entryInputPassword.get()
    entryInputPassword.delete(0,len(enteredText2))

    qt = [enteredText1,enteredText2]

    try:
        with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Data Analytics\AGV Data.csv', mode='a', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(qt)
    except IOError:
        print("NO")

    return messagebox.showinfo(title = 'Submission', message = 'AGV Number: ' + enteredText1 +'\n'*2 + 'AGV Issue: ' + enteredText2)

def dashTextLabels():
    frameAGVNumber = tk.Frame(master=window, width=10, height=10, borderwidth=5, relief=tk.SUNKEN)
    frameAGVNumber.grid(row=0, column=1,pady=2)

    frameAGVIssue = tk.Frame(master=window, width=10, height=10, borderwidth=5, relief=tk.SUNKEN)
    frameAGVIssue.grid(row=1, column=1,pady=2)

    frameDate = tk.Frame(master=window, width=10, height=10, borderwidth=3, relief=tk.RIDGE)
    frameDate.grid(row=7, column=1, columnspan=2)

    labelAGVNumber = tk.Label(master=frameAGVNumber,
                         text='AGV number',
                         fg='black',
                         bg='white', width=25,
                         height=1,
                         font=('Arial', 9))
    labelAGVNumber.pack()

    labelAGVIssue = tk.Label(master=frameAGVIssue,
                      text='Describe AGV issue',
                      fg='black',
                      bg='white', width=25,
                      height=1,
                      font=('Arial', 9))
    labelAGVIssue.pack()

    labelDate = tk.Label(master=frameDate,
                         text= f"{dt.now():%a %b %d, %Y}",
                         fg='black',
                         bg='white', width=15,
                         height=1,
                         font=('Arial', 9))
    labelDate.pack()

def dashInputLabels():
    frameAGVNumber = tk.Frame(master=window, width=10, height=10, relief=tk.GROOVE,borderwidth=5)
    frameAGVNumber.grid(row=0, column=2, padx=5,pady=2)

    frameAGVIssue = tk.Frame(master=window, width=10, height=10, relief=tk.GROOVE,borderwidth=5)
    frameAGVIssue.grid(row=1, column=2,padx=5,pady=2)

    global entryUserName
    entryUserName= tk.Entry(master=frameAGVNumber, width=25, bg='white')
    entryUserName.pack()

    global entryInputPassword
    entryInputPassword= tk.Entry(master=frameAGVIssue, width = 25, bg='white')
    entryInputPassword.pack()

def dashButtons():
    frameSubmit = tk.Frame(master=window, width=10, height=10,borderwidth=2,bg='green')
    frameSubmit.grid(row=3, column=1,columnspan=2)

    button = tk.Button(master=frameSubmit, text='Submit', width=5, command=click, font=('Arial', 9))
    button.pack()

def main():
    global window
    window = tk.Tk()
    window.configure(bg='light gray')
    window.title("AGV Recording")
    window.geometry('380x300')
    window.columnconfigure([0,1,2,3,4,5,6],minsize=10,weight=0)
    window.rowconfigure([0,1,2,3,4,5,6],minsize=10,weight=0)

    #above functions
    dashTextLabels()
    dashInputLabels()
    dashButtons()

    window.mainloop()

if __name__ == "__main__":
    main()
    print('All done!')