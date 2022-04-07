import csv
import smtplib
import os
from email.message import EmailMessage
import webbrowser
import time
from pynput import keyboard
#############################################################################################
#############################################################################################

#a = 'https://deere.cloud.databricks.com/files/export__3_.csv'

#with open(r'C:\Users\WKYTUK0\Downloads\TestFile.csv') as csvfile:
  #  file_reader = csv.reader(csvfile, delimiter=' ')
   # filetest = list(file_reader)

#for i in range(len(filetest)):
 #   print(filetest[i])
#############################################################################################
#############################################################################################

webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome') #.open(a)

#############################################################################################
#############################################################################################
s = smtplib.SMTP(host='smtp.gmail.com',port=587) #given by outlook: 587

passwrd = "Soccerstar13"
sender= 'trentlind8@gmail.com'
reviever= 'trentlind8@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'NEW_CSV_TESTING'
msg['From'] = 'trentlind8@gmail.com'
msg['To'] = 'trentlind8@gmail.com'
msg.set_content('File Attached below '
                'hopefully this works well')

files = [r'C:\Users\WKYTUK0\Downloads\TestFile.csv']
filer = [r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\Internship2021\Internship2021_ActionLog_TrentLind.xlsx']

for file in filer:
    with open(file, 'rb') as f: #the 'b' in rb makes it a binary file
        file_data = f.read()
        file_name = f.name

msg.add_attachment(file_data,maintype='application',subtype='octet-string',filename=file_name)

try:
    with s:
        s.ehlo()
        s.starttls()
        #s.login('trentlind8@gmail.com',passwrd)
        #s.sendmail(sender,reviever,msg.as_string())
except Exception as e:
    print(e)

print("The email has been sent")

break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        print ('program running')
        time.sleep(5)
    listener.join()