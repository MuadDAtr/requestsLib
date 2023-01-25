import requests

response = requests.get("https://httpbin.org/status/204")


if response.status_code == requests.codes.no_content:
    print("NO CONTENT")
else: 
    print(response.status_code)
    