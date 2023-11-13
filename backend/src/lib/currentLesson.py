import datetime



timeliste = {
  "08:20": "Brukerst\u00f8tte",
  "09:10": "Brukerst\u00f8tte",
  "10:10": "Brukerst\u00f8tte",
  "11:00": "Samfunnskunnskap",
  "12:15": "Driftsst\u00f8tte",
  "13:05": "Driftsst\u00f8tte",
  "13:55": "Driftsst\u00f8tte"
}


    
today = datetime.datetime.now()
current_time = datetime.datetime.now().time()


for tid in timeliste:
    today = datetime.datetime.now()
    current_time = datetime.datetime.now().time()
    timenow = str(f"{current_time.hour}:{current_time.minute}")
if timenow > tid:
  print(tid)