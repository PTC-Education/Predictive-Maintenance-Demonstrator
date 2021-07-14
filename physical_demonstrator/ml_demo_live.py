import serial
import json
import time #https://www.gtkdb.de/index_31_2492.html#:~:text=Um%20in%20einem%20Python%2DSkript,in%20einen%20String%20konvertiert%20werden.
import csv
import datetime
import requests
"""
disable https warning from python
source: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


arduino = serial.Serial(port='COM4', baudrate=1000000, timeout=.03)
time.sleep(3)
url = 'https://pp-2101111403aw.portal.ptc.io/Thingworx/Things/MM_Machine_Learning_Demo' #ptc
#url = 'https://pp-1909092003t5.portal.ptc.io/Thingworx' #UAS Technikum Wien
headers = { 'Content-Type': 'application/json',  'accept': 'application/json', 'appKey': '2dea7a1e-2b35-4b53-8afe-33470e6b6edc'} #ptc
#headers = { 'Content-Type': 'application/json',  'accept': 'application/json', 'appKey': '8dbbc287-a9f9-43bf-9c4f-b7337d0e461a'} #UAS Technikum Wien

def readFeedback():
    data = arduino.readline()
    return data

def callToTwx(feedbackJson):
    payload = {"smartServo1Angle" : feedbackJson["1A"], "smartServo1Temp" : feedbackJson["1T"], "smartServo1Current" : feedbackJson["1C"], "smartServo1Voltage" : feedbackJson["1V"],
              "smartServo2Angle" : feedbackJson["2A"], "smartServo2Temp" : feedbackJson["2T"], "smartServo2Current" : feedbackJson["2C"], "smartServo2Voltage" : feedbackJson["2V"],
              "smartServo3Angle" : feedbackJson["3A"], "smartServo3Temp" : feedbackJson["3T"], "smartServo3Current" : feedbackJson["3C"], "smartServo3Voltage" : feedbackJson["3V"]}
    response = requests.put(url + '/Properties/*', headers=headers, json=payload, verify=False)
    return response

def readFromTwx():
    response = requests.get(url + '/Properties/Goal', headers=headers, verify=False)
    value = json.loads(response.text)
    return value["rows"][0]["Goal"]

arduino.write(bytes(str(-100)+'\n', 'utf-8'))
time.sleep(0.04)


while True:
    feedbackString = readFeedback()
    if feedbackString:
        feedbackJson = json.loads(feedbackString)
        callToTwx(feedbackJson)
        servo3Angle = readFromTwx()
        #print(servo3Angle)
        if(servo3Angle):
            arduino.write(bytes(str(servo3Angle*-1)+'\n', 'utf-8'))
            time.sleep(0.04)
            

        
     
        
  


    

  
    
    
