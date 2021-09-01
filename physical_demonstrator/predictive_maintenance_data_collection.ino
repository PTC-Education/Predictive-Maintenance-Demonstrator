/*
    Use this code for the ThingworxAnalyticsIntroduction-guide
    Arduino Code to read sensor data of SmartServos, write position of SmartServos and handle serial conncection with Raspi
    Version 1
    2021.08.31
*/


#include <SoftwareSerial.h>  // for serial connections
#include "MeAuriga.h" // Makeblock Libraries
#include "ArduinoJson-v6.17.3.h" // JSON library to send data to raspi

class Demonstrator
{
  public:
    Demonstrator();
    void updateSensorValues();
    void updateAngleValues();
    void sendSensorValuesToSerial(int cycle);

    // Future update: change back to getters and setters
    float smartServo1[4] = {0, 0, 0, 0}; // Angle, Temp, Current, Voltage
    float smartServo2[4] = {0, 0, 0, 0};
    float smartServo3[4] = {0, 0, 0, 0};
  private:
    MeSmartServo* smartServoConn;
};

Demonstrator::Demonstrator()
{
  smartServoConn = new MeSmartServo(PORT5); //UART2 is on port 5
  smartServoConn->begin(115200);
  delay(5);
  smartServoConn->assignDevIdRequest();
  delay(50);
}


void Demonstrator::updateAngleValues()
{
  smartServo1[0] = smartServoConn->getAngleRequest(1);
  smartServo2[0] = smartServoConn->getAngleRequest(2);
  smartServo3[0] = smartServoConn->getAngleRequest(3);
}


void Demonstrator::updateSensorValues()
{
  smartServo1[0] = smartServoConn->getAngleRequest(1);
  smartServo2[0] = smartServoConn->getAngleRequest(2);
  smartServo3[0] = smartServoConn->getAngleRequest(3);

  smartServo1[1] = smartServoConn->getTempRequest(1);
  smartServo2[1] = smartServoConn->getTempRequest(2);
  smartServo3[1] = smartServoConn->getTempRequest(3);

  smartServo1[2] = smartServoConn->getCurrentRequest(1);
  smartServo2[2] = smartServoConn->getCurrentRequest(2);
  smartServo3[2] = smartServoConn->getCurrentRequest(3);

  smartServo1[3] = smartServoConn->getVoltageRequest(1);
  smartServo2[3] = smartServoConn->getVoltageRequest(2);
  smartServo3[3] = smartServoConn->getVoltageRequest(3);
}

void Demonstrator::sendSensorValuesToSerial(int cycle)
{
  DynamicJsonDocument smartServoDoc(128);

  smartServoDoc["1A"] = smartServo1[0];
  smartServoDoc["1T"] = smartServo1[1];
  smartServoDoc["1C"] = smartServo1[2];
  smartServoDoc["1V"] = smartServo1[3];

  smartServoDoc["2A"] = smartServo2[0];
  smartServoDoc["2T"] = smartServo2[1];
  smartServoDoc["2C"] = smartServo2[2];
  smartServoDoc["2V"] = smartServo2[3];


  smartServoDoc["3A"] = smartServo3[0];
  smartServoDoc["3T"] = smartServo3[1];
  smartServoDoc["3C"] = smartServo3[2];
  smartServoDoc["3V"] = smartServo3[3];

  smartServoDoc["t"] = cycle;
  serializeJson(smartServoDoc, Serial);
  Serial.print('\n');
}

Demonstrator* drawingRobot;
unsigned long lastTime = 0;
unsigned long curTime = 0;
int cycle = 0;
int state = 0;
bool start = false;
bool publishValues = false;

void setup()
{
  Serial.begin(1000000);
  drawingRobot = new Demonstrator();
  delay(2000);
  lastTime = millis();
}

void loop()
{
  if (!start && Serial.available() > 0) {
    publishValues = Serial.readString().toInt();
    if (publishValues) //check if values should be published
    {
      start = true; // double if to ensure correct behaviour while serial port is busy
    }
  }

  if ( start )
  {
    if (millis() - lastTime >= 60)
    {
      drawingRobot->updateSensorValues();
      drawingRobot->sendSensorValuesToSerial(cycle);
      lastTime = millis();
    }
  
    switch (state) {
        // send move command and check if position (+/- tolerance) is reached in next case
        // Future update: function using a tolerance variable instead of repeated code blocks
      case 0: drawingRobot->smartServoConn->moveTo(1, 125, 0.1);
        drawingRobot->smartServoConn->moveTo(2, 105, 1);
        drawingRobot->smartServoConn->moveTo(3, -152, 0.1);
        state ++;
        break;
      case 1: 
        if ((drawingRobot->smartServo1[0] >= 124 && drawingRobot->smartServo1[0] <= 126) &&
            (drawingRobot->smartServo2[0] >= 104 && drawingRobot->smartServo2[0] <= 106) &&
            (drawingRobot->smartServo3[0] >= -152 && drawingRobot->smartServo3[0] <= -150)) {
          state ++;
        }
        break;
      case 2: drawingRobot->smartServoConn->moveTo(1, 125, 0.1);
        drawingRobot->smartServoConn->moveTo(2, 105, 1);
        drawingRobot->smartServoConn->moveTo(3, -145, 0.1);
        state ++;
        break;
      case 3: 
        if ((drawingRobot->smartServo1[0] >= 124 && drawingRobot->smartServo1[0] <= 126) &&
            (drawingRobot->smartServo2[0] >= 104 && drawingRobot->smartServo2[0] <= 106) &&
            (drawingRobot->smartServo3[0] >= -145 && drawingRobot->smartServo3[0] <= -143)) {
          state ++;
        }
        break;
      case 4: drawingRobot->smartServoConn->moveTo(1, 20, 0.1);
        drawingRobot->smartServoConn->moveTo(2, 105, 1);
        drawingRobot->smartServoConn->moveTo(3, -145, 0.1);
        state ++;
        break;
      case 5: 
        if ((drawingRobot->smartServo1[0] >= 19 && drawingRobot->smartServo1[0] <= 21) &&
            (drawingRobot->smartServo2[0] >= 104 && drawingRobot->smartServo2[0] <= 106) &&
            (drawingRobot->smartServo3[0] >= -145 && drawingRobot->smartServo3[0] <= -143)) {
          state ++;
        }
        break;
      case 6: drawingRobot->smartServoConn->moveTo(1, 20, 0.1);
        drawingRobot->smartServoConn->moveTo(2, 105, 1);
        drawingRobot->smartServoConn->moveTo(3, -152, 0.1);
        state ++;
        break;
      case 7: 
        if ((drawingRobot->smartServo1[0] >= 19 && drawingRobot->smartServo1[0] <= 21) &&
            (drawingRobot->smartServo2[0] >= 104 && drawingRobot->smartServo2[0] <= 106) &&
            (drawingRobot->smartServo3[0] >= -152 && drawingRobot->smartServo3[0] <= -150)) {
          state = 0;
          cycle ++;
        }
        break;
    }
  }


}
