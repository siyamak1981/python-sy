import datetime
import requests
r = requests.get('http://httpbin.org/get')




import datetime
datetime.datetime.now()
>>> import requests
>>> r = requests.get('http://httpbin.org/get')
>>> r
<Response [200]>
>>> r.ok
True
>>> r.headers
>>> r.headers[ 'Content-Length']
>>>r.text
>>> r.json()
>>> timeline = r.json()
>>> timeline[0]['id']

