import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox
from matplotlib import animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from datetime import datetime as dt
import sys

def clickEnd():
    #window.destroy()
    #sys.exit(1)
    #exit(1)
    plt.close()

def dateNow():

    today = dt.now()
    todayFormat = today.strftime("%m-%d-%y, %H:%M:%S")
    return todayFormat

#master represents the parent window

def animate(i):
    data = pd.read_csv(r"C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\ExcelDocuments\UpdateCSV.csv")

    global xar,yar
    xar = data['Number']
    yar = data['Value']

    plot1.clear()
    plot1.plot(xar[len(xar)-45:len(xar)], yar[len(yar)-45:len(yar)])
    #return xar,yar

def plotter():
  global plot1,fig1

  fig1 = plt.figure(figsize=(3,3),dpi=100)
  plot1 = fig1.add_subplot(111)

  frameFigure1 = tk.Frame(master=window, width=10, height=10, borderwidth=2, relief=tk.FLAT)
  frameFigure1.grid(row=10, column=1,pady=4, rowspan=2,columnspan=3)

  frameExit = tk.Frame(master=window, width=10, height=10, borderwidth=2, bg = 'red', relief=tk.RAISED)
  frameExit.grid(row=13,column=1,columnspan=2,pady=2)

  buttonExit = tk.Button(master=frameExit, text='Close', width=5, command=clickEnd, font=('Arial', 9))
  buttonExit.pack()

  line1 = FigureCanvasTkAgg(fig1, frameFigure1)
  line1.draw()
  line1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

  while True:
      ani = animation.FuncAnimation(fig1, animate, interval=1000, blit=False)
      #plt.show()
      fig1.show(ani)
  #window.after(1,animate)

  #plt.show()
    #plt.show()



  #plot1.cla()
  #plot1.plot(xar, yar)


def click():
    global enteredText1
    enteredText1= entryUserName.get()
    entryUserName.delete(0,len(enteredText1))

    global enteredText2
    enteredText2= entryInputPassword.get()
    entryInputPassword.delete(0,len(enteredText2))

    return messagebox.showinfo(title = 'User Info', message = 'Name: ' + enteredText1 +'\n'*2 + 'Password: ' + enteredText2)

def dashTextLabels():
    frameUser = tk.Frame(master=window, width=10, height=10, borderwidth=5, relief=tk.SUNKEN)
    frameUser.grid(row=0, column=1,pady=2)

    framePassword = tk.Frame(master=window, width=10, height=10, borderwidth=5, relief=tk.SUNKEN)
    framePassword.grid(row=1, column=1,pady=2)

    frameDate = tk.Frame(master=window, width=10, height=10, borderwidth=3, relief=tk.RIDGE)
    frameDate.grid(row=7, column=1, columnspan=2)

    labelUser = tk.Label(master=frameUser,
                         text='Enter your name:',
                         fg='black',
                         bg='white', width=25,
                         height=1,
                         font=('Arial', 9))
    labelUser.pack()

    labelPassword = tk.Label(master=framePassword,
                      text='Enter your password:',
                      fg='black',
                      bg='white', width=25,
                      height=1,
                      font=('Arial', 9))
    labelPassword.pack()

    labelDate = tk.Label(master=frameDate,
                         text= f"{dt.now():%a %b %d, %Y}",
                         fg='black',
                         bg='white', width=15,
                         height=1,
                         font=('Arial', 9))
    labelDate.pack()

def dashInputLabels():
    frameUserName = tk.Frame(master=window, width=10, height=10, relief=tk.GROOVE,borderwidth=5)
    frameUserName.grid(row=0, column=2, padx=5,pady=2)

    frameInputPassword = tk.Frame(master=window, width=10, height=10, relief=tk.GROOVE,borderwidth=5)
    frameInputPassword.grid(row=1, column=2,padx=5,pady=2)

    global entryUserName
    entryUserName= tk.Entry(master=frameUserName, width=25, bg='lightgreen')
    entryUserName.pack()

    global entryInputPassword
    entryInputPassword= tk.Entry(master=frameInputPassword, width=25, bg='lightgreen')
    entryInputPassword.pack()

def dashButtons():
    frameSubmit = tk.Frame(master=window, width=10, height=10,borderwidth=2,bg='green')
    frameSubmit.grid(row=3, column=1,columnspan=2)

    framePlot = tk.Frame(master=window, width=10, height=10, borderwidth=2, bg='orange')
    framePlot.grid(row=5, column=1, columnspan=2)

    button = tk.Button(master=frameSubmit, text='Submit', width=5, command=click, font=('Arial', 9))
    button.pack()

    plot = tk.Button(master=framePlot, text='Plot', width=5, command=plotter, font=('Arial', 9))
    plot.pack()

def main():
    global window
    window = tk.Tk()
    window.configure(bg='light gray')
    window.title("User Entry Form")
    window.geometry('700x700')
    window.columnconfigure([0,1,2,3,4,5,6],minsize=10,weight=0)
    window.rowconfigure([0,1,2,3,4,5,6],minsize=10,weight=0)

    #above functions
    dashTextLabels()
    dashInputLabels()
    dashButtons()

    window.mainloop()

if __name__ == "__main__":
    main()
