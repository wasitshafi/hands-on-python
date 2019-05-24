import datetime as dt
import time

while( True):
    dateTime = dt.datetime.now()
    print ("Date = ", dateTime.strftime("%x"))
    print ("Time = ", dateTime.strftime("%X"), end = "\n\n")
    time.sleep(1)
