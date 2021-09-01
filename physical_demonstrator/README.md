# Physical robot arm

A 3-axis robot arm was used for the guides and creation of the datasets. Three pieces of [makeblock Smart Servo MS-12A](https://www.makeblock.com/project/smart-servo-ms-12a) are used. The brackets, screws and nuts are included. Only a base is needed on which the arm can be mounted. The [makeblock me-auriga](https://www.makeblock.com/project/me-auriga) board was used but it is compatible with the Arduino Mega 2560 and other Arduinos can be used as well. The following figure shows the basic setup:

<img src="C:\Users\Juergen\Documents\GitHub\Predictive-Maintenance-Demonstrator\misc\demonstrator_overview.jpg" alt="3-axis robot arm" style="zoom:50%;" />

<img src="C:\Users\Juergen\Documents\GitHub\Predictive-Maintenance-Demonstrator\misc\demonstrator_technology_map.png" alt="3-axis robot arm" style="zoom:50%;" />

This section of the repository contains the Arduino code to run the Thingworx Analytics Guides with this hardware. If you want to use other hardware, these files serve as information regarding the data exchange for the python scripts. Data is transferred via the serial interface using the JSON format.

## Usage

Copy the .ino files in your Arduino Sketchbook folder and install the required libraries (libraries and the project folder need to be in the same directory). Then build and upload the code to your Arduino. For this project the Arduino IDE was used.

For the [ThingworxAnalyticsIntroduction](../guides/ThingworxAnalyticsIntroduction/Create an Analytics model and use it with a Thing.pdf)-guide use the [ml_demo.ino](ml_demo.ino) file.
For the [ThingworxAnalyticsTimeSeriesPrediction](../guides/ThingworxAnalyticsTimeSeriesPrediction/ThingworxAnalyticsTimeSeriesPredictionExample.pdf)-guide use the [predictive_maintenance_data_collection.ino](predictive_maintenance_data_collection.ino) file.

## Requirements:

A guide on how to install Arduino libraries can be found here: http://arduino.cc/en/Guide/Libraries

- Makeblock Arduino libraries, instructions @ https://github.com/Makeblock-official/Makeblock-Libraries
- ArduinoJson library, instruction @ https://arduinojson.org/ 
  Navigate to Header-only for the download

