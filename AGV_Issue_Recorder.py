import csv

def openCSV():
    try:
        with open(r'C:\Users\WKYTUK0\Documents\TestingCode\PumpData.csv', mode='a', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    except IOError:
        print('The file could not be opened')


    for i in range(len(df)):
         print(df[i])