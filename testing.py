import requests
from requests.api import get
import Serial
import time
import requests
import json

arduino = Serial.Serial('COM1', 9600)

def ledControl(cmd):
    arduino.write(cmd.encode())
    
payload = {'username':'Tatak', 'password': 'atw'}

res = requests.get("http://localhost/UAS1/index.php", params=payload )
print(res.text)

# cookies = dict(key1 = 'value1')
# res = requests.get("http://localhost/IoTUAS/cookies", cookies=cookies)
# print(res.text)