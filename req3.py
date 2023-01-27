import requests

r = requests.get("https://httpbin.org/user-agent")

print(r.text)
print(" ")
print(r.headers)