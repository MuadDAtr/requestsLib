import requests

response = requests.get("https://httpbin.org/delay/7")

print(response)