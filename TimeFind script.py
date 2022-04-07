import time
from datetime import datetime

def currentTime():
    timeMe = datetime.now().strftime("%I:%M%p")
    print(timeMe)

def currentJulianTime():
    timenow = str(time.time())
    print(timenow[0:5])

if __name__ == "__main__":
    print(__name__)
    currentTime()

    print("Hello World")
    
    print("Trent Lind")

    print("Trento Lind0")

    print("Newest Commit")
    
    #dfk;skf;ldskf;lskf;slakd
