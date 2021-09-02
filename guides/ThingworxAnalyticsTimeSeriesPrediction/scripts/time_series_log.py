import serial
import json
import time
import csv


arduino = serial.Serial(port='COM4', baudrate=1000000, timeout=.04) # change to the USB port of the plugged in demonstrator
time.sleep(3) # wait for connection with Arduino

def readFeedback():
    data = arduino.readline()
    return data


def processing_loop(csvfile):
    isDrawing = True
    HEADER = ["asset", "smartServo1Angle", "smartServo1Temp", "smartServo1Current", "smartServo1Voltage",
              "smartServo2Angle", "smartServo2Temp", "smartServo2Current", "smartServo2Voltage",
              "smartServo3Angle", "smartServo3Temp", "smartServo3Current", "smartServo3Voltage" , "time", "cycle", "isDrawing"]
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    
    while True:
        try:
            feedbackString = readFeedback()
             # Debugging message
            if feedbackString:
                feedbackJson = json.loads(feedbackString)
                csv_writer.writerow(["JA_Demonstrator_1",
                      feedbackJson["1A"], feedbackJson["1T"], feedbackJson["1C"], feedbackJson["1V"],
                      feedbackJson["2A"], feedbackJson["2T"], feedbackJson["2C"], feedbackJson["2V"],
                      feedbackJson["3A"], feedbackJson["3T"], feedbackJson["3C"], feedbackJson["3V"], feedbackJson["t"] ,feedbackJson["c"], isDrawing])

        except KeyboardInterrupt:
            if isDrawing:
               isDrawing = False
               print("Pencil not drawing anymore \n")
               continue
            else :
               break


value = input("Enter s to start:\n") # wait for the user to trigger the data collection process
if value == "s":
    arduino.write(bytes('1'+'\n', 'utf-8')) # send Arduino command to start
    time.sleep(0.05) 
with open('dataset.csv', 'w', newline='') as csvfile: # change the name of the output csv file here
    processing_loop(csvfile)

  
    
    
