import requests

params = {
    "name": "Joshua",
    "age" : 21
}

payload = {
    "name": "Joshua",
    "age" : 21
}

response = requests.post("https://httpbin.org/post", data=payload)

print(response.url)

print(response.status_code)
print("      ")
print(response.text)
print("      ")
print(response.json())
