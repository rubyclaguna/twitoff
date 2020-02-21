import json
import requests


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=abc123"

response = requests.get(request_url)

print(response)

print(response.status_code)
print(response.text)

parsed_response = json.loads(response.text)
print(type(parsed_response))
print(parsed_response.keys())


#breakpoint()