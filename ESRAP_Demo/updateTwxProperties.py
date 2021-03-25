import requests
"""
disable https warning from python
source: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def callToTwx(propertyValue):
    url = 'https://pp-2101111403aw.portal.ptc.io/Thingworx'
    headers = { 'Content-Type': 'application/json', 'appKey': '22f8f92b-2299-402a-bb76-df2f274a4426' , 'accept': 'application/json'}
    payload = {'Temperature': propertyValue}
    response = requests.put(url + '/Things/JA_Temperature_Sensor/Properties/*', headers=headers, json=payload, verify=False)
    return response

try:
    for temperature in range(30):
        print("temperature: " , temperature , callToTwx(temperature))
        
except KeyboardInterrupt:
    pass

    
    
