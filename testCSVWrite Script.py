import csv
from random import randint
import time
import numpy as np

x = []
y = []
x=1
y=2

a = 25
b = 0
P = 0
q = 100 / a

L = '█'

def loadingBar(a,b):

    print('\r', end = '')
    Z = (b/25) * 100

    if b < (a - 23):
        print(f'{L}',end = '')
        print(f' {int(Z)}% Complete', end='')

    elif b < (a - 18):
        print(f'{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}', end ='')
        print(f' {int(Z)}% Complete', end='')

    elif b < (a - 13):
        print(f'{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}',end ='')
        print(f' {int(Z)}% Complete', end='')

    elif b < (a - 8):
        print(f'{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}', end = '')
        print(f' {int(Z)}% Complete', end='')

    elif b <= (a - 2):
        print(f'{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}{L}', end = '')
        print(f' {int(Z)}% Complete', end='')


while b <= a:
    #print(f"The current step is {b}")

    #print(f'{P}', end = '')
    x = x+1
    y = np.sin(randint(0,10))

    b = b+1
    P = P + q

    loadingBar(a,b)

    with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\ExcelDocuments\UpdateCSV.csv', mode='a', newline='') as csvFile:
        file_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([x,y])

    time.sleep(1)