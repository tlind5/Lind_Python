import csv

def openCSV():
    try:
        with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Data Analytics\AGV Data.csv', mode='a', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    except IOError:
        with open(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Data Analytics\AGV Data.csv', mode='w+', newline='') as df:
            file_writer = csv.writer(df, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow("Alpha")
            file_writer.writerow("Beta")

        print('The file could not be opened')


    for i in range(len(df)):
         print(df[i])