import csv
import matplotlib.pyplot as plt

def openCSV():
 with open(r"C:\Users\WKYTUK0\Downloads\export (3).csv") as csvfile:
  file_reader = csv.reader(csvfile, delimiter=',',quotechar='|')
  df = list(file_reader)

  #print(len(df))
  #print(df[0])
  #print(df[1][0])
  #print(df[1][2])

 rows = len(df)
 columns = len(df[1])

 print(df[1:rows])

 results = []
 for z in range(len(df)):
  results.append(df[z])

 print(results[0][1])

 global x
 global y
 x= []
 y = []

 for i in df[1:rows]:
  x.append(int(i[0]))
  y.append(int(i[2]))


def graphCSV():
 print(y)
 plt.figure(figsize=(10,4))
 plt.plot(x,y)

 plt.show(block = False) #ensure that all figure windows are displayed and return immediately
 plt.pause(3)
 plt.close()

if __name__ == "__main__":
 openCSV()
 graphCSV()