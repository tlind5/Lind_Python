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
    
    print("Trent Lind")
