import json, requests

API = "500d2adb0a6f4c140f8d47efa4c7f564"

def temperature():
    request = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Molde/today?unitGroup=metric&elements=temp&include=current&key=27GDK56WQN6ZD7C929SHA5YM6&contentType=json')                
    response = json.loads(request.text)
    return response['currentConditions']['temp']


