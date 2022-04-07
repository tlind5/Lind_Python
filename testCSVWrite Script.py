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

while b <= a:
    print(f"The current step is {b}")

    x = x+1
    y = np.sin(randint(0,10))

    b = b+1

    with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\ExcelDocuments\UpdateCSV.csv', mode='a', newline='') as csvFile:
        file_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([x,y])

    time.sleep(1)