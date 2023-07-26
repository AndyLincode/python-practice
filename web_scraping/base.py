import requests

parameters = {'key1': 1, 'key2': 2}
result = requests.get("http://www.example.com", params=parameters)
print(result.url)  # http://www.example.com/?key1=1&key2=2
