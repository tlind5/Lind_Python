from selenium import webdriver
import pandas as pd
import time
from datetime import date, timedelta, datetime
import os
from webdriver_manager.chrome import ChromeDriverManager
import pyodbc
import sys

#######################################################################################################################
#######################################################################################################################
'''This block of code finds the current date and time. It then solves for our desired 2 week time period back and trims
 that time period so it is in the date format we want'''

today = date.today()
timeNow = datetime.now().strftime("%I:%M %p")

activeweekend = today - timedelta(days = 8)
activeweekstart = today - timedelta(days = 14)

myend = activeweekend.strftime("%Y%m%d")
mystart = activeweekstart.strftime("%Y%m%d")

#######################################################################################################################
#######################################################################################################################
def errorRecording(e,a,tryName):
    '''The error recording connects to a SQL server table and adds the error if the program has one along with date,
    time, error info, and line number. It then ends the program a depending on where we are in the code, it cleans up
    the run so that a new run can be initiated.'''
    try:
        cnxn = pyodbc.connect(r"Driver={SQL Server Native Client 11.0};"
                              "Server=FDXX90SQL146\INST1;"
                              "Database=Utilities;"
                              "Trusted_Connection=yes;")

        print("connection has been made")


        cnxn.execute(''' INSERT INTO DATABRICKS_AI_CATCHER (RUN_DATE, RUN_TIME, RUN_NAME, RUN_STATUS, RUN_DESCRIPTION, RUN_LINE_ERROR)
                                    VALUES(?,?,?,?,?,?);''', (today,timeNow,'A&I DATABRICKS FILE CATCHER ','FAILED',str(e),a))
        cnxn.commit()
        cnxn.close()

        print('ERROR RECORDED')
        sys.exit(1) #keeps python code from continuing
    except Exception as e:
        print(e)
    finally:
        print("Program did not run correctly")
        if tryName == 'Try1' or tryName == 'Try2': #every try block has a corresponding try label attached to it
            driver.close()
            driver.quit()
        elif tryName == 'Try3':
            os.remove(f'{df}{slash}lathrop.csv')
            os.remove(f'{df}{slash}dallas.csv')
            os.remove(f'{df}{slash}regina.csv')
            os.remove(f'{df}{slash}grimsby.csv')
            driver.quit()
        elif tryName == 'Try4':
            driver.quit()

def completionRecording():
    '''If the program makes it down to the very bottom of the code, then a completed run will be added to a SQL server
    table. This works the same as above, but only for completed runs and the code has to get down to the bottom
    for this to be called.'''
    #try:
    cnxn = pyodbc.connect(r"Driver={ODBC Driver 11 for SQL Server};"
                            "Server=FDXX90SQL146\INST1;"
                            "Database=Utilities;"
                            "UID=Reporter;"
                            "PWD=RptDriver;")

    print("connection has been made")

    cnxn.execute(''' INSERT INTO DATABRICKS_AI_CATCHER (RUN_DATE,RUN_TIME,RUN_NAME,RUN_STATUS,RUN_DESCRIPTION,RUN_LINE_ERROR)
                                    VALUES(?,?,?,?,?,?);''', (today,timeNow,'A&I DATABRICKS FILE CATCHER ','COMPLETED','no error',0))
    cnxn.commit()
    cnxn.close()

    print('No Error Found')
    #except Exception as e:
     #   print(e)
    #finally:
     #   print('Completion Recording Finished')

#######################################################################################################################
#######################################################################################################################
'''In this block, we intialize the link for google to open and the files for google to open within databricks.
chrome is then opened, databricks is logged into, the files are downloaded, and chrome closes. If an error occurs
it is reported to the error function.'''

loginLink = "https://deere.cloud.databricks.com/login.html"

try:
    driver = webdriver.Chrome(ChromeDriverManager().install()) #this updates the chrome driver and automatically sets the correct path
    driver.get(loginLink)
    time.sleep(20)
    button = driver.find_element_by_xpath(r"/html/body/uses-legacy-bootstrap/div/div/div[1]/div/div/div/div/div/button")
    button.click()

except Exception as e:
    tryName = 'Try1'
    a = sys.exc_info()[-1].tb_lineno #records line number of error
    errorRecording(e,a,tryName)

#######################################################################################################################
#######################################################################################################################
'''This block of codes uses the needed download links below to download the files from the filestore.'''

linkNames = ['https://deere.cloud.databricks.com/files/A&I-stuff/lathrop.csv',
             'https://deere.cloud.databricks.com/files/A&I-stuff/dallas.csv',
             'https://deere.cloud.databricks.com/files/A&I-stuff/regina.csv',
             'https://deere.cloud.databricks.com/files/A&I-stuff/grimsby.csv']
try:
    for x in range(len(linkNames)):
        driver.get(linkNames[x])
        time.sleep(3)

    driver.close()  # closes chrome'
except Exception as e:
    tryName = 'Try2'
    a = sys.exc_info()[-1].tb_lineno  # records line number of error
    errorRecording(e,a,tryName)

#######################################################################################################################
#######################################################################################################################
'''This block of code uses the operating system to find out who the user is and then use that to set the path to the 
downloads folder. It then initializes an arbitrary download name list. '''

user = os.environ['USERPROFILE']
df = user + '\downloads'
fileDownload = ['lathrop.csv','dallas.csv','regina.csv','grimsby.csv']
slash = '\\' #one of the backslashes is removed, left with a single "\"

#######################################################################################################################
#######################################################################################################################
'''This block of code uses the link names list to iterate through loading and formatting the downloaded files.
An extra row is always loaded so this block of code deletes that extra row. After it goes through the downloaded files,
it will delete them from the downloads folder.'''

try:
    for x in range(len(linkNames)):
        if linkNames[x] == 'https://deere.cloud.databricks.com/files/A&I-stuff/lathrop.csv':
            hfLathrop = pd.read_csv(f'{df}{slash}lathrop.csv')
            hfLathrop.drop('Unnamed: 0',axis=1,inplace=True)

        elif linkNames[x] == 'https://deere.cloud.databricks.com/files/A&I-stuff/dallas.csv':
            hfDallas = pd.read_csv(f'{df}{slash}dallas.csv')
            hfDallas.drop('Unnamed: 0',axis=1,inplace=True)

        elif linkNames[x] == 'https://deere.cloud.databricks.com/files/A&I-stuff/regina.csv':
            hfRegina = pd.read_csv(f'{df}{slash}regina.csv')
            hfRegina.drop('Unnamed: 0', axis=1, inplace=True)

        elif linkNames[x] == 'https://deere.cloud.databricks.com/files/A&I-stuff/grimsby.csv':
            hfGrimsby = pd.read_csv(f'{df}{slash}grimsby.csv')
            hfGrimsby.drop('Unnamed: 0', axis=1, inplace=True)

    os.remove(f'{df}{slash}lathrop.csv')
    os.remove(f'{df}{slash}dallas.csv')
    os.remove(f'{df}{slash}regina.csv')
    os.remove(f'{df}{slash}grimsby.csv')

except Exception as e:
    tryName = 'Try3'
    a = sys.exc_info()[-1].tb_lineno
    errorRecording(e,a,tryName)

#######################################################################################################################
#######################################################################################################################
'''This block of code generates the file name and then save the file as a .csv to the desired network share folder.'''

try:
    for x in range(len(linkNames)):
        if fileDownload[x] == 'lathrop.csv':
            filename = "\Lathrop"+'12' + ' ' + mystart +'--' + myend +'.csv'
            extension = r'\\ndxxnasc9301\parts\HOST_FTP\A&I'

            fullname = extension + filename
            hfLathrop.to_csv(fullname)

            print("Lathrop upload complete")

        elif fileDownload[x] == 'dallas.csv':
            filename = "\Dallas" + '35' + ' ' + mystart + '--' + myend + '.csv'
            extension = r'\\ndxxnasc9301\parts\HOST_FTP\A&I'

            fullname = extension + filename
            hfDallas.to_csv(fullname)

            print("Dallas upload complete")


        elif fileDownload[x] == 'regina.csv':
            filename = "\Regina" + '27' + ' ' + mystart + '--' + myend + '.csv'
            extension = r'\\ndxxnasc9301\parts\HOST_FTP\A&I'

            fullname = extension + filename
            hfRegina.to_csv(fullname)

            print("Regina upload complete")

        elif fileDownload[x] == 'grimsby.csv':
            filename = "\Grimsby" + '37' + ' ' + mystart + '--' + myend + '.csv'
            extension = r'\\ndxxnasc9301\parts\HOST_FTP\A&I'

            fullname = extension + filename
            hfGrimsby.to_csv(fullname)

            print("Grimsby upload complete")

except Exception as e:
    tryName = 'Try4'
    a = sys.exc_info()[-1].tb_lineno
    errorRecording(e,a,tryName)

###########################################################
###########################################################
'''This block of code records the completed run and closes the terminal on the computer.'''

print("Process Complete")
completionRecording()
driver.quit() #quits the terminal that is brought up






"""
THIS IS EXTRA CODE THAT CAN WORK, BUT BETTER ALTERNATIVES WERE FOUND
"""
#######################################################################################################################
#######################################################################################################################

#webbrowser.register('chrome',
 #                  None,
  #                  webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
#webbrowser.get('chrome').open(a)

#webbrowser.register('edge',
 #                   None,
  #                  webbrowser.BackgroundBrowser(f"{user}\AppData\Local\Microsoft\WindowsApps\MicrosoftEdge.exe"))
#webbrowser.get('edge').open(a)

#df = pd.read_csv(r'C:\Users\dy81db2\Downloads\Downloads\lathrop.csv')

#df = os.path.join(os.environ['USERPROFILE'], '\downloads')

#subprocess.call(["taskkill","/F","/IM","GoogleSearcher.exe"])
#driver.quit()

#slash = r'\''