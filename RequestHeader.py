import requests
h = requests.head("http://172.18.58.238/headers.php")
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
headers = {
    'User-Agent' : 'Mobile'
}

url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)