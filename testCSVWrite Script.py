import csv
from random import randint
import time
import numpy as np

import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

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

    #loadingBar(a,b)



    with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\ExcelDocuments\UpdateCSV.csv', mode='a', newline='') as csvFile:
        file_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([x,y])

    #time.sleep(1)

import time

for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(1) # any calculation you need