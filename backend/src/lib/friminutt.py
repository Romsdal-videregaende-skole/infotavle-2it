import time
from time import sleep
from datetime import time as Time
from datetime import datetime, time

today = datetime.now()
current_time = datetime.now().time()


friminutt_start = ["9:5", "9:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
friminutt_end = ["9:10", "10:15", "11:00", "12:15", "13:05", "13:55"]



def liste(friminutt):

    for x in range(len(friminutt)):
        split_tider = friminutt[x].split(":")
        res = [eval(i) for i in split_tider]
        test = datetime(today.year, today.month, today.day, res[0], res[1])
        if today < test:
            current_datetime = datetime.combine(datetime.today(), current_time)
            time_difference = test - current_datetime
            total_minutes_until_recess = time_difference.total_seconds() / 60
            percentage_difference = (total_minutes_until_recess / 40) * 100
            return friminutt[x], percentage_difference

        

#1% av 45min = 27 sekund 45/100 = 0,45*60 =27 sekund




if __name__ =='__main__':
    x = Time(13,0)
    print(today)
    friminutter = liste(friminutt_start)
    print(f"Percentage difference: {friminutter/100}")

