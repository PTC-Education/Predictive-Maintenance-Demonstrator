import requests
"""
disable https warning from python
source: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 'appKey': '37376417-3c5f-4356-a4a6-023f03821ad4' ,

def callToTwx(propertyValue):
    #url = 'http://localhost:8080/Thingworx'
    headers = { 'Content-Type': 'application/json',  'accept': 'application/json'}
    payload = {'servo1Temperature': propertyValue}
    response = requests.get('http://localhost:8080/Thingworx/JA_EMS_Demonstrator_Thing/Properties/servo1Temperature', headers=headers, verify=False)
    return response

try:
    for temperature in range(30):
        print("temperature: " , temperature , callToTwx(temperature))
        
except KeyboardInterrupt:
    pass

    
    
