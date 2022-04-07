
import csv

def insert(a, b):
    if a == 1:
        thePumpType = ["Fixed Displacement"]
    elif a == 2:
        thePumpType = ["Variable Displacement"]

    systemLines = [b]
    Index = [0]

    Total = [thePumpType[0],systemLines[0],Index[0]]
    Data = ['Pump','# of Lines',"ID Number"]


    try:
        with open(r'C:\Users\WKYTUK0\Documents\TestingCode\PumpData.csv', mode='a', newline='') as PumpSystemData:
            file_writer = csv.writer(PumpSystemData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(Total)
    except IOError:
        with open(r'C:\Users\WKYTUK0\Documents\TestingCode\PumpData.csv', mode='w+', newline='') as PumpSystemData:
            file_writer = csv.writer(PumpSystemData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(Data)
            file_writer.writerow(Total)

    print("Your Pump type is:", thePumpType[0])
    print("The number of lines your system has is equal to:", systemLines[0])