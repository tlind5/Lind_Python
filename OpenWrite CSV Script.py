import csv
import testDashboard

testDashboard.animate()

def openCSV():
    with open(r'C:\Users\WKYTUK0\Downloads\lathrop.csv') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',',quotechar='|')
        df = list(file_reader)

    for i in range(len(df)):
         print(df[i])

def writeCSV():
    with open(r'C:\Users\WKYTUK0\Documents\TestingCode\PumpData.csv', mode='a', newline='') as PumpSystemData:
        file_writer = csv.writer(PumpSystemData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow()

if __name__ == "__main__":
    openCSV()