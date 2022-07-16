import requests

api_key = 'YOUR_API_KEY'
url = 'https://api.alpaca.markets/v2/stocks/screener?sort=shortable&direction=desc&limit=100'
headers = {'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': api_secret}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # parse the response JSON to get the list of shortable stocks
    shortable_stocks = response.json()
    print(shortable_stocks)
else:
    print('Error:', response.status_code)
