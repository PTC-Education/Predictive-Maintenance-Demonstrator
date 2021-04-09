import serial
import json
import time #https://www.gtkdb.de/index_31_2492.html#:~:text=Um%20in%20einem%20Python%2DSkript,in%20einen%20String%20konvertiert%20werden.
import csv
import datetime


arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=1000000, timeout=.1)

def readFeedback():
    data = arduino.readline()
    return data
    

def processing_loop(csvfile):
    HEADER = ["timestamp", "asset", "smartServo1Angle", "smartServo1Temp", "smartServo1Current", "smartServo1Voltage",
              "smartServo2Angle", "smartServo2Temp", "smartServo2Current", "smartServo2Voltage",
              "smartServo3Angle", "smartServo3Temp", "smartServo3Current", "smartServo3Voltage" , "time", "isBroken"]
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)


    while True:
        feedbackString = readFeedback()
        #print(feedbackString) # Debugging message
        feedbackJson = json.loads(feedbackString)
        
        csv_writer.writerow([datetime.datetime.now(), "JA_EMS_Demonstrator_Thing",
              feedbackJson["1A"], feedbackJson["1T"], feedbackJson["1C"], feedbackJson["1V"],
              feedbackJson["2A"], feedbackJson["2T"], feedbackJson["2C"], feedbackJson["2V"],
              feedbackJson["3A"], feedbackJson["3T"], feedbackJson["3C"], feedbackJson["3V"], feedbackJson["t"], 0])
        #csvfile.flush()
        


with open('results.csv', 'w', newline='') as csvfile:
    processing_loop(csvfile)

  
    
    
