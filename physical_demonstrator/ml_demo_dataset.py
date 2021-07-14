import serial
import json
import time #https://www.gtkdb.de/index_31_2492.html#:~:text=Um%20in%20einem%20Python%2DSkript,in%20einen%20String%20konvertiert%20werden.
import csv
import datetime


arduino = serial.Serial(port='COM4', baudrate=1000000, timeout=.03)
time.sleep(3) # wait for connection with Arduino



########################### define functions ###########################
    
def readFeedback(): # reads the data sent from the Arduino
    data = arduino.readline()
    return data

def processing_loop(csvfile): # loop while the csv file is opened
    # set Headers in the csv file, used in Thingworx to assign Metadata
    HEADER = ["asset", "smartServo1Angle", "smartServo1Temp", "smartServo1Current", "smartServo1Voltage",
              "smartServo2Angle", "smartServo2Temp", "smartServo2Current", "smartServo2Voltage",
              "smartServo3Angle", "smartServo3Temp", "smartServo3Current", "smartServo3Voltage" ]
    csv_writer = csv.writer(csvfile) 
    csv_writer.writerow(HEADER) # writes Headers into the csv file
    #arduino.reset_input_buffer()
    #arduino.reset_output_buffer

    while True: 
            i=0
            value = input("Enter s to save 10 data points, any other key to exit:\n") # wait for the user to trigger the data collection process
            if value == "s":
                arduino.write(bytes('1'+'\n', 'utf-8')) # send Arduino command to publish Servo feedback 10 times
                #time.sleep(0.05) #
                while i<10:
                    feedbackString = readFeedback()
                     
                    if feedbackString:
                        #print(feedbackString) # Debugging message
                        feedbackJson = json.loads(feedbackString)
                        print(feedbackJson) # Debugging message
                        csv_writer.writerow(["JA_Machine_Learning_Demonstrator",
                          feedbackJson["1A"], feedbackJson["1T"], feedbackJson["1C"], feedbackJson["1V"],
                          feedbackJson["2A"], feedbackJson["2T"], feedbackJson["2C"], feedbackJson["2V"],
                          feedbackJson["3A"], feedbackJson["3T"], feedbackJson["3C"], feedbackJson["3V"]])
                        i+=1
                    #csvfile.flush() print to csv every iteration
                print("\n")
            else: exit()

########################### ################# ###########################

with open('results.csv', 'w', newline='') as csvfile: # open csv file and execute processing_loop function
    processing_loop(csvfile)
