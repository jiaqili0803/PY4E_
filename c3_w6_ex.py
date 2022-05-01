import json
import urllib.error
import urllib.parse
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)

data_before = urllib.request.urlopen(url)
data = data_before.read().decode()

info = json.loads(data)


comments = info['comments']
sum = 0
for item in comments:
    sum = sum + item['count']

print(sum)

    