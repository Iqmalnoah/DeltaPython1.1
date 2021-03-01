import requests

# Set the target webpage
url = ('http://172.18.58.238')
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code

print("Status code:")
print("\t *", r.status_code)