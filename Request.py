import requests

# Set the target webpage
url = ('http://www.wikipedia.org')
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code

print("Status code:")
print("\t *", r.status_code)