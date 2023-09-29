import requests

access_token = '65155c4b9e4d906b7e03d149|e3dc30eb443e837bdedd73b88796225d'
api_endpoint = 'https://api.netatmo.com/api/getstationsdata'


def getTemp():
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        modules = data['body']['devices'][0]['modules']
        for module in modules:
            module_type = module['type']
            module_name = module['module_name']
            temperature = module['dashboard_data']['Temperature']

            print(f'{module_name}: {temperature}°C')

        indoor_module = data['body']['devices'][0]
        indoor_temperature = indoor_module['dashboard_data']['Temperature']
        print(f'Indoor: {indoor_temperature}°C')
    else:
        print(f'Error: {response.status_code} - {response.text}')
    return

if __name__ == '__main__':
    print(getTemp())

 