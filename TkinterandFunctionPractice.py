import time
from datetime import date, timedelta
import os
import pyodbc
import datetime
import sys
import tkinter as tk
from tkinter import messagebox

delta = datetime.date.today()

fileNames = ['https://deere.cloud.databricks.com/files/A&I-stuff/lathrop.csv',
             'https://deere.cloud.databricks.com/files/A&I-stuff/dallas.csv',
             'https://deere.cloud.databricks.com/files/A&I-stuff/regina.csv']

print(fileNames[1][-10:]) #last 10 characters in string

slash = '\\'
print(slash)

#x = dir(os)
#print(x)

#make this a def function
def errorRecording(e,a):
    try:
        cnxn = pyodbc.connect(r"Driver={SQL Server Native Client 11.0};"
                              "Server=FDXX90SQL146\INST1;"
                              "Database=Utilities;"
                              "Trusted_Connection=yes;")

        print("connection has been made")


        cnxn.execute(''' INSERT INTO LIND_TEST (LIND_DATE, LIND_NAME, LIND_F1, LIND_F2, LIND_F3)
                                    VALUES(?,?,?,?,?);''', (delta, 'ERROR RECORDING', 1, str(e), a))
        cnxn.commit()
        cnxn.close()

        print(a)

        print('ERROR RECORDED')
    except Exception as e:
        print(e)
    finally:
        print("Program will stop")

def completionRecording():
    try:
        cnxn = pyodbc.connect(r"Driver={SQL Server Native Client 11.0};"
                              "Server=FDXX90SQL146\INST1;"
                              "Database=Utilities;"
                              "Trusted_Connection=yes;")

        print("connection has been made")

        cursor = cnxn.cursor()

        cnxn.execute(''' INSERT INTO LIND_TEST (LIND_DATE, LIND_NAME, LIND_F1, LIND_F2, LIND_F3)
                                     VALUES(?,?,?,?,?);''', (delta, 'ERROR RECORDING', 1, 'no error', 1))
        cnxn.commit()
        cnxn.close()

        print('No Error Found')
    except Exception as e:
        print(e)
    finally:
        print('Program will continue')


try:
    a = 1
except Exception as e:
    a = sys.exc_info()[-1].tb_lineno
    errorRecording(e,a)
else:
    print("Done")
    #completionRecording()
finally:
    print('finish code')

print("End of code")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printer(self):
      print(self.name)
      print(self.age)

mine = Person('Trent',21)
mine.printer()

def click():
    enteredText1 = entry1.get()
    entry1.delete(0,len(enteredText1))

    enteredText2 = entry2.get()
    entry2.delete(0,len(enteredText2))

    return messagebox.showinfo(title = 'User Info', message = 'Name: ' + enteredText1 +'\n'*2 + 'Password: ' + enteredText2)

window = tk.Tk()
window.geometry('175x200')
window.title("Graphics Test")

label1 = tk.Label(window,
    text = 'Enter your name please:',
    fg = 'black',
    bg = 'light grey',width = 21,
    height = 1)
label1.grid(row=0,column=0,sticky='W')

entry1 = tk.Entry(window, width=25, bg='lightgreen')
entry1.grid(row=1, column=0, sticky='W')

label2 = tk.Label(window,
    text = 'Enter your password:',
    fg = 'black',
    bg = 'light grey',width = 21,
    height = 1)
label2.grid(row=3,column=0,sticky='W')

entry2 = tk.Entry(window, width=25, bg='lightgreen')
entry2.grid(row=4, column=0, sticky='W')

button = tk.Button(window,text='Submit',width=5,command=click)
button.grid(row=6,column=0,sticky = 'W')


window.mainloop()

#messagebox.showinfo('Hello', 'Your code ran!!!')