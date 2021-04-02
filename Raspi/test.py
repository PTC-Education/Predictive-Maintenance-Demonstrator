#import serial
import json
import time #https://www.gtkdb.de/index_31_2492.html#:~:text=Um%20in%20einem%20Python%2DSkript,in%20einen%20String%20konvertiert%20werden.
import csv
import datetime


#arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def readFeedback():
    #arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data
    

def processing_loop(csvfile):
    HEADER = ["timestamp", "asset", "smartServo1Angle", "smartServo1Temp", "smartServo1Current", "smartServo1Voltage",
              "smartServo2Angle", "smartServo2Temp", "smartServo2Current", "smartServo2Voltage",
              "smartServo3Angle", "smartServo3Temp", "smartServo3Current", "smartServo3Voltage"]
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)


    while True:
        #feedbackString = readFeedback()
        #print(feedbackString) # Debugging message
        #feedbackJson = json.loads(feedbackString)
        csv_writer.writerow([datetime.datetime.now(), "JA_EMS_Demonstrator_Thing",
              feedbackJson["smartServo1Angle"], feedbackJson["smartServo1Temp"], feedbackJson["smartServo1Current"], feedbackJson["smartServo1Voltage"],
              feedbackJson["smartServo2Angle"], feedbackJson["smartServo2Temp"], feedbackJson["smartServo2Current"], feedbackJson["smartServo2Voltage"],
              feedbackJson["smartServo3Angle"], feedbackJson["smartServo3Temp"], feedbackJson["smartServo3Current"], feedbackJson["smartServo3Voltage"]])
        csvfile.flush()
        time.sleep(1)


with open('results.csv', 'w', newline='') as csvfile:
    processing_loop(csvfile)

  
    
    
