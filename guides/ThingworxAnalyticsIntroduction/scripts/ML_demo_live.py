import serial
import json
import time
import requests
"""
disable https warning from python
source: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


arduino = serial.Serial(port='COM4', baudrate=1000000, timeout=.03) # change to the USB port of the plugged in demonstrator
time.sleep(3)
url = 'https://pp-2101111403aw.portal.ptc.io' #change "pp-2101111403aw.portal.ptc.io" part to the url of your Thingworx instance, do not edit the other parts
url = url + '/Thingworx/Things/JA_Machine_Learning_Demo'
headers = { 'Content-Type': 'application/json',  'accept': 'application/json', 'appKey': 'Insert your appKey here, example: "f4b00336-e8cd-4042-9743-b75ad3fffeef"'}

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
