import serial
import json
import time #https://www.gtkdb.de/index_31_2492.html#:~:text=Um%20in%20einem%20Python%2DSkript,in%20einen%20String%20konvertiert%20werden.
import csv
import datetime


arduino = serial.Serial(port='COM4', baudrate=1000000, timeout=.04)
time.sleep(3) # wait for connection with Arduino

def readFeedback():
    data = arduino.readline()
    return data
    
isDrawing = True
timing = 0

def processing_loop(csvfile):
    global isDrawing
    global timing
    HEADER = ["timestamp", "asset", "smartServo1Angle", "smartServo1Temp", "smartServo1Current", "smartServo1Voltage",
              "smartServo2Angle", "smartServo2Temp", "smartServo2Current", "smartServo2Voltage",
              "smartServo3Angle", "smartServo3Temp", "smartServo3Current", "smartServo3Voltage" , "time", "cycle", "isDrawing"]
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)

    
    while True:
        try:
            #print("begin \n")
            feedbackString = readFeedback()
             # Debugging message
            if feedbackString:
        
                feedbackJson = json.loads(feedbackString)
                timing = timing + 60
                csv_writer.writerow([datetime.datetime.now(), "JA_Demonstrator_1",
                      feedbackJson["1A"], feedbackJson["1T"], feedbackJson["1C"], feedbackJson["1V"],
                      feedbackJson["2A"], feedbackJson["2T"], feedbackJson["2C"], feedbackJson["2V"],
                      feedbackJson["3A"], feedbackJson["3T"], feedbackJson["3C"], feedbackJson["3V"], timing ,feedbackJson["t"], isDrawing])
                #print("end \n")
                #csvfile.flush()
        except KeyboardInterrupt:
            if isDrawing:
                isDrawing = False
                print("interrupt \n")
                
                continue
            else :
               break


value = input("Enter s to start:\n") # wait for the user to trigger the data collection process
if value == "s":
    arduino.write(bytes('1'+'\n', 'utf-8')) # send Arduino command to start
    time.sleep(0.05) 
with open('RUL_03mm_B_1.csv', 'w', newline='') as csvfile:
    processing_loop(csvfile)

  
    
    
