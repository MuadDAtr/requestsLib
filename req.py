import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)
print("      ")
print(response.text)
print("      ")
print(response.json())
