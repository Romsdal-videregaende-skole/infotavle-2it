import requests

access_token = '65155c4b9e4d906b7e03d149|e3dc30eb443e837bdedd73b88796225d'
refresh_token = '65155c4b9e4d906b7e03d149|7dbe56aeb9e9209c8018f38192ac5d7f'

api_endpoint = 'https://api.netatmo.com/api/getstationsdata'


headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(api_endpoint, headers=headers)

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print(f'Error: {response.status_code} - {response.text}')
    data = response.text
    print(data.get("body"))

