import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M", named_tuple)



def liste(time_string):
    friminut = ["09:05", "09:55", "10:55", "11:45", "13:00", "13:50", "14:40"]
    for x in friminut:
        if time.strftime("%H:%M", named_tuple) < x:
            print(x)
            return



#1% av 45min = 27 sekund 45/100 = 0,45*60 =27 sekund


if __name__ == __main__:
    liste(time_string)

