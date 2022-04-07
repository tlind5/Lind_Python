import pyodbc
import datetime

#alpha = "POST TEST"
beta = input("Enter A number: ")
delta = datetime.date.today()

cnxn = pyodbc.connect(r"Driver={SQL Server Native Client 11.0};"
                      "Server=FDXX90SQL146\INST1;"
                      "Database=Utilities;"
                      "Trusted_Connection=yes;")

print("connection has been made")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM LIND_TEST')

title = [i[0] for i in cursor.description]
print(title[:])

results = []

#cursor returns all values in each row
for row in cursor:
   results.append(row)

x = 0
for i in range(len(results)):
    x = 0
    for x in range(len(results[0])):
        if results[i][x] is None:
            print("it was True")
            results[i][x] = 0
        else:
            print("Fine")

try:
    for i in range(len(results)):
        cnxn.execute(''' INSERT INTO LIND_TEST (LIND_DATE, LIND_NAME, LIND_F1, LIND_F2, LIND_F3)
                        VALUES(?,?,?,?,?);''', (delta,results[i][2],beta,results[i][4],results[i][5]))
        cnxn.commit()
except Exception as e:
    print(e)
    cnxn.rollback() #will undo any and all changes made to table if the program does not work

cnxn.close()

print('Table Updated')


###########################################################################
###########################################################################
#for row in cursor:
#   #print('row = %r' % (row,))
    #print(row)
    #results.append(dict(zip(title,row)))

#totalNumber = 0
#for i in range(len(results)):
 #  totalNumber = totalNumber + float(results[i][3])

#print(totalNumber)