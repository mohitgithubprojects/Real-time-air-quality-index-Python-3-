import urllib.request, urllib.parse, urllib.error
import json
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd00000138923aa6add34ffc6089ac6871f966b5&format=json&offset=0&limit=500'
html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()
info = json.loads(data)

if info['status'] == 'ok':
    print("All over India :-")
    for i in range(0,len(info['records'])):
        print(info['records'][i]['state'],':- ')
        print(info['records'][i]['city'])
        print(info['records'][i]['station'])
        print(info['records'][i]['pollutant_id'])
        print(info['records'][i]['pollutant_avg'])
else:
    print('==== Failure To Retrieve ====')
