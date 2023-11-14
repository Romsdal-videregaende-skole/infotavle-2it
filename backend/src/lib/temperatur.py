import requests

access_token = '65155c4b9e4d906b7e03d149|3a5fd1c9dd239df69795e9f9a4df42de'
refresh_token = '65155c4b9e4d906b7e03d149|1932729e3cca65233005d34281a43735'

api_endpoint = 'https://api.netatmo.com/api/getstationsdata'

def getTemp():
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return {"netatmo": data['body']['devices'][0]['dashboard_data']}
    else:
        print(f'Error: {response.status_code} - {response.text}')
        data = response.text
    return None

if __name__ == '__main__':
    getTemp()