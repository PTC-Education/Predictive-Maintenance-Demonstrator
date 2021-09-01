/*
    Use this code for the ThingworxAnalyticsTimeSeriesPrediction-guide
    Arduino Code to read sensor data of SmartServos, write position of SmartServos and handle serial conncection with Raspi/PC
    Version 1
    2021.08.30
*/

#include <SoftwareSerial.h>  // for serial connections
#include "MeAuriga.h" // Makeblock Libraries
#include "ArduinoJson-v6.17.3.h" // JSON library to send data to raspi


#define mode 1  // 0 => collect data; 1 => live demo


class Demonstrator
{
  public:
    Demonstrator();
    void updateSensorValues();
    void sendSensorValuesToSerial(unsigned long time);

  private:
    float smartServo1[4] = {0, 0, 0, 0}; // Angle, Temp, Current, Voltage
    float smartServo2[4] = {0, 0, 0, 0};
    float smartServo3[4] = {0, 0, 0, 0};
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

void Demonstrator::sendSensorValuesToSerial(unsigned long time)
{
  DynamicJsonDocument smartServoDoc(128);

  smartServoDoc["1A"] = smartServo1[0];
  smartServoDoc["1T"] = smartServo1[1];
  smartServoDoc["1C"] = smartServo1[2];
  smartServoDoc["1V"] = smartServo1[3];

  smartServoDoc["2A"] = smartServo2[0] * -1;
  smartServoDoc["2T"] = smartServo2[1];
  smartServoDoc["2C"] = smartServo2[2];
  smartServoDoc["2V"] = smartServo2[3];

  smartServoDoc["3A"] = (smartServo3[0] * -1) + 1;
  smartServoDoc["3T"] = smartServo3[1];
  smartServoDoc["3C"] = smartServo3[2];
  smartServoDoc["3V"] = smartServo3[3];

  smartServoDoc["t"] = time;
  serializeJson(smartServoDoc, Serial);
  Serial.print('\n');
}


/*
    Execution starts here
*/

Demonstrator* drawingRobot;
unsigned long lastTime = 0;
unsigned long curTime = 0;

void setup()
{
  Serial.begin(1000000); // start serial communication to communicate with Raspi/PC
  drawingRobot = new Demonstrator(); // create instance of Demonstrator class and connect to SmartServos
  delay(2000); // wait for all the connection to complete
  lastTime = millis(); // set start time, used for timing intervals between messages (soft interval)
}

void loop()
{
  drawingRobot->smartServoConn->moveTo(1, 58, 0.1); change position (2nd value) according to the position of your arm
  drawingRobot->smartServoConn->moveTo(2, -150, 0.1); change position (2nd value) according to the position of your arm
  bool publishValues = false;
  int servo3AngleFromTwx = -100;

  switch (mode) {
    case 0:
      if (Serial.available() > 0) {
        publishValues = Serial.readString().toInt();
        if (publishValues) //check if values should be published
        {
          for (int i = 0; i < 10; i++)
          {
            if (millis() - drawingRobot->lastTime >= 200)
            {
              drawingRobot->updateSensorValues();
              drawingRobot->sendSensorValuesToSerial(lastTime);

              drawingRobot->lastTime = millis();
            } else i--;
          }
          publishValues = false;
        }
      }
      break;

    case 1:
      if (Serial.available() > 0) {
        servo3AngleFromTwx = Serial.readString().toInt();
        if (servo3AngleFromTwx < -60 && servo3AngleFromTwx > -180) // change limits according to the position of your arm
        {
          drawingRobot->smartServoConn->moveTo(3, servo3AngleFromTwx, 0.1);
        }
        drawingRobot->updateSensorValues();
        drawingRobot->sendSensorValuesToSerial(drawingRobot->curTime + 200);
      }
      break;
    default: break;
  }
}
