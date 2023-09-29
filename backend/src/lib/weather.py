import json, requests

API = "500d2adb0a6f4c140f8d47efa4c7f564"

def temperature():
    request = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Molde/today?unitGroup=metric&elements=temp&include=current&key=27GDK56WQN6ZD7C929SHA5YM6&contentType=json')                
    response = json.loads(request.text)
    print (response['currentConditions']['temp'])  #magnus fiksa william sin kode  ƪ(˘⌣˘)ʃ
    return

<<<<<<< HEAD
if __name__ == '__main__':
    temperature()
=======
>>>>>>> a34be625ad7c229d4b422456cee8b8ad1f20c80c
