print("hello world!")

import requests

pageresults = requests.get('url')
print(pageresults)

feitjes = paginaresults.json()
print(feitjes["data"][0][fact])