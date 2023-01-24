import requests

response = requests.get("https://httpbin.org/status/300")


if response.status_code == requests.codes.not_found:
    print("Page not found")
else: 
    print(response.status_code)