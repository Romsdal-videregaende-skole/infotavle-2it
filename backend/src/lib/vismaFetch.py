import requests
from datetime import datetime, timedelta
import operator


def get_formatted_date():
    # Get the current date
    current_date = datetime.now()

    # Format the date as "DD/MM/YYYY"
    formatted_date = current_date.strftime("%d/%m/%Y")
    day_name = current_date.strftime("%A")

    # Check if the day is Saturday or Sunday
    if day_name.lower() == "saturday" or day_name.lower() == "sunday":
        # If it's a weekend, add 2 days to the current date
        new_date = current_date + timedelta(days=2)
        formatted_date = new_date.strftime("%d/%m/%Y")

    return formatted_date


# Call the function and print the result
formatted_date = get_formatted_date()

ID = 9390648


ENDPOINT = f"https://romsdal-vgs.inschool.visma.no/control/timetablev2/learner/{ID}/fetch/ALL/0/current?forWeek={formatted_date}&extra-info=true&types=LESSON,EVENT,ACTIVITY,SUBSTITUTION&_=1702672538858"
HEADER = {
    "Cookie": "XSRF-TOKEN=cb555d07-9607-432e-b15e-a663e90ca59a; JSESSIONID=1A8D58AED5969079D0F462CD9BEF6194-n1; Authorization=eyJ0eXAiOiJKV1QiLCJ0b2tlblR5cGUiOiJBQ0NFU1MiLCJhbGciOiJSUzI1NiJ9.eyJzZXJpYWxpemVkVXNlckRldGFpbHMiOiJINHNJQUFBQUFBQUEvNzFRN1VyRFFCQjhsWEsvVDdtdmJPN3l5eUpGaFJJbDRnK1JJa2R6YVlQSnBlUnFwWWlQNDVQNFl1NjJXbndDQ1VkdVpuZm1kdmFkYmZ4MnpRckdPSHU5cVZraHJkRTVXTWZaTmlMS2hNUnJFMHBzNlh4YSs1MTBGLzNZN0x1WGNCNEhWTlZVbXZ1VXd1VGE3MkpJeUFWV2JNZlhnQjVrNmJRVFlDeG55K24rOElRR3E0QXpmNFQwdEwrZjduODFkYk5COHJJalN6THJCb1J4T0N0dkVjUTU2amxiQlNMTFlYenplMlFUMll4RG4ycmZuZTFXcE9vcnBLcmIrZXg1UHB0VzVheWlzZnBqaWhRdTFvZFJ6OXZZVUFiL3VNU0tFa3JqTVFmaUI1TTVCYXlPNXBOZFc0Y3hyTDQrUTZ6REpMME1YYUNXUGwzOW5XZDV4NHJHZHduVHJFN3JRYjRoY05wU1gxSUlsK1ZPYTVFanNia2ZUN3JZNHZxWnhNMEpjQ3FYZ3VvZXd5dVFTa3FGano2Y210dWFWdFlFSEk3YWJ1ckVpaWNqSEhESUFBd1hQRU9GRWxibzNPVFdjQWxLWkVRN0tZemcwbVZVem9EbkZvd0Jib1FDWnlSZ0NSZUNqUkswUGZ5VjVWcmg1VisrQllZSlk5K20xQTR4SFdNdFByNEJBN2NZejdRQ0FBQT0iLCJpZCI6IjQ3ODY2YWZmLTA1N2UtNGFhNi05NDFmLTU4YjhmMTFhZGI4ZiIsImlzTW9iaWxlIjpmYWxzZSwiZXhwIjoxNzAyNjcyNzY2LCJwYXJ0UmVmIjoiMGU2Zjg3Y2FhMjI3OTAxMmQ3NmVlMzZmMGZmM2Y1MjMiLCJpc1N1cHBvcnRVc2VyIjpmYWxzZSwiaWF0IjoxNzAyNjcyNDY2LCJ0ZW5hbnQiOjE1MDE5LCJzYW1sQ3JlZGVudGlhbHNSZWZJZCI6ImZmZGQwY2M4LWY3NGEtNDUyMi1iZTIwLTYyMzVlMTJkNzVmYzoyMDIzLTEyLTE1VDIwOjI4OjM5LjIzMzE2NjU1MyIsInRva2VuR2VuZXJhdGlvblZlcnNpb25JZCI6IjU5OTM4MzVmYTE4NzBiMjY0MWY0N2I4NmI2NmE1MmUxZTYwZWZhYjY3YmU5M2I2NDVkNmFjMzE0Mjc3NzI5ZWIifQ.V3iCc5jgO6LjBdLWknmQrJbauxCjmuBO3PLr_5R6h4tYerpyQkW6ohDhH6FnJUg4Bq9yXpWoAcBlKPBozq-GL_AW2SqFUtPmMtdyEvltzryAtNsNZXZDDwHEq-tESPavKJ2mgF_kdJdr5voZffWT6mDEpnxt4wPcQk0OdIf2fGN0dKYnB7wt6Un7wl6JdWpjDSDfXIQy7mELu5ePzY3pgm0jT8XOMUgayUM8ExvykC0GXhzeqs13_77MwnE-UE8lvJ3S7Emn0IhIxIXSWBxmUG6kTR7hOT81xNlfdves95xg-KCQ6lAJZtQ-9iEFA0MxbQp5pZJEffj_HQjhpZUsqQ; SameSite=None; pdfcc=7; AWSALB=/wF7Lowz+iQIXD6DzPNINBc89mpPJdTRBi4by+keQb+njXmrBo74Soqjj5StEF2VP5t0nrhb7WbbgEK13von0ZwutVbBDbS9Q6pkmhmk+lI0EG9DEJWQw35xGCNT; AWSALBCORS=/wF7Lowz+iQIXD6DzPNINBc89mpPJdTRBi4by+keQb+njXmrBo74Soqjj5StEF2VP5t0nrhb7WbbgEK13von0ZwutVbBDbS9Q6pkmhmk+lI0EG9DEJWQw35xGCNT"
}

req = requests.get(ENDPOINT, headers=HEADER)


def getVisma():
    resp = {}
    response = req.json()
    timetable = response.get('timetableItems')

    for item in range(len(timetable)):
        if timetable[item].get('date') == formatted_date:
            items = timetable[item]
            resp[items.get('startTime')] = [
                items.get('subject'), items.get('teacherName'), items.get('endTime')]

    # Sort the dictionary by keys in ascending order
    sorted_resp = dict(sorted(resp.items(), key=operator.itemgetter(0)))

    return sorted_resp


if __name__ == '__main__':
    print(req.text)
