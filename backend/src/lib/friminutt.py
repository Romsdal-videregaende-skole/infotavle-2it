import time
from time import sleep
from datetime import datetime

today = datetime.now()

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M", named_tuple)
friminutt_start = ["9:5", "9:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
friminutt_end = ["9:10", "10:15", "11:00", "12:15", "13:05", "13:55"]



def liste(friminutt):

    for x in range(len(friminutt)):
        split_tider = friminutt[x].split(":")
        res = [eval(i) for i in split_tider]
        test = datetime(year=today.year, month=today.month, day=today.day, hour=res[0], minute=res[1])
        if today < test:
            print(friminutt[x],(test.minute/today.minute)/100)
        

#1% av 45min = 27 sekund 45/100 = 0,45*60 =27 sekund




if __name__ =='__main__':

    print(liste(friminutt_start))

