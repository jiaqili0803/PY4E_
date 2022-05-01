import json

url = input('Enter location: ')
print('Retrieving', url)

data_before = urllib.request.urlopen(url)
data = data_before.read().decode()

info = json.loads(data)

print(info[0])

    