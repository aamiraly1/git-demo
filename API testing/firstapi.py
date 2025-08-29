import requests

res=requests.get("https://www.google.com/")
print(res.url)
print("******************")
print("\n")
print(res.cookies)
print("******************")
print("\n")
print(res)
