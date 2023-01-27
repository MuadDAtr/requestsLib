import requests

response = requests.get("https://httpbin.org/delay/7", timeout = 3)

print(response)