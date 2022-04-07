import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import csv
import pandas as pd


def animate(i):
    j = 1
    data = pd.read_csv(r"C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\ExcelDocuments\UpdateCSV.csv")
    #print(data)
    xar = data['Number']
    yar = data['Value']

    plt.cla()
    plt.plot(xar[len(xar)-20:len(xar)],yar[len(yar)-20:len(yar)])

    j=j+1

if __name__== "__main__":
    fig = plt.gcf()
    ax1 = fig.add_subplot(1, 1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

#https://stackoverflow.com/questions/59534043/update-chart-every-time-a-point-added-to-csv-file-python