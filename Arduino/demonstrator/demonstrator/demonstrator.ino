/*
 *  Arduino Code to read sensor data of SmartServos, write position of SmartServos and handle serial conncection with Raspi 
 *  Author: Juergen Altenriederer
 *  Version 0.1
 *  2021.04.02
*/


#include <SoftwareSerial.h>  // for serial connections
#include "MeAuriga.h" // Makeblock Libraries
#include "ArduinoJson-v6.17.3.h" // JSON library to send data to raspi

 // use as member variable, error with setting port when used as private member


class Demonstrator
{
  public:
    Demonstrator();
    void updateSensorValues();
    void sendSensorValuesToSerial();
  private:
    MeSmartServo* smartServoConn;
    float smartServo1[4] = {0,0,0,0}; // Angle, Temp, Current, Voltage
    float smartServo2[4] = {0,0,0,0}; 
    float smartServo3[4] = {0,0,0,0};
    int axisPosArray[4][3] = {{100, -200, -145},
                           {100, -200, -150},
                           {20, -120, -150},
                           {20, -120, -145}};
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
  //Serial.println(String(smartServoConn->getAngleRequest(1)) );
}

void Demonstrator::sendSensorValuesToSerial()
{
  DynamicJsonDocument doc(1024);

  doc["smartServo1Angle"] = smartServo1[0];
  doc["smartServo1Temp"] = smartServo1[1];
  doc["smartServo1Current"] = smartServo1[2];
  doc["smartServo1Voltage"] = smartServo1[3];

  doc["smartServo2Angle"] = smartServo2[0];
  doc["smartServo2Temp"] = smartServo2[1];
  doc["smartServo2Current"] = smartServo2[2];
  doc["smartServo2Voltage"] = smartServo2[3];

  doc["smartServo3Angle"] = smartServo3[0];
  doc["smartServo3Temp"] = smartServo3[1];
  doc["smartServo3Current"] = smartServo3[2];
  doc["smartServo3Voltage"] = smartServo3[3];

  serializeJson(doc, Serial);
}


/*
void callback_test(uint8_t servoNum)
{
   switch(servoNum)
   {
     case 1:
      // Serial.println("servo 1 has been reached!");
       break;
     case 2:
      // Serial.println("servo 2 has been reached!");
       break;
   }
}
*/

Demonstrator* drawingRobot;
void setup()
{
  Serial.begin(115200);
  //Serial.println("setup!");
  drawingRobot = new Demonstrator();
  //loopTime = millis();
  //smartServoConn.moveTo(1,0,50);
  //smartServoConn.moveTo(2,0,50);
  delay(2000);
}
int i =0;

void loop()
{
  drawingRobot->updateSensorValues();
  drawingRobot->sendSensorValuesToSerial();
  
  
  
  
  /*
  //smartServoConn.moveTo(1,360,50,callback_test);    //device ID, angle, speed;  relative angle move;
  //smartServoConn.moveTo(2,360,50,callback_test);    //device ID, angle, speed;  relative angle move;
   Serial.println(String(smartServoConn.getAngleRequest(1)) );
  smartServoConn.moveTo(1,100,0.1);
  //1 ist von 60 bis 70safe
  Serial.println(String(smartServoConn.getAngleRequest(2)) );
  smartServoConn.moveTo(2,-200,0.1);
  //2 ist von -170 bis 200 safe   200 ist rechts
  Serial.println(String(smartServoConn.getAngleRequest(3)) );
  smartServoConn.moveTo(3,-145,0.1);
  //3 ist von -111 bis 120 safe   120 ist unten
  delay(2000);
  
  Serial.println(String(smartServoConn.getAngleRequest(1)) );
  i+=10;
  smartServoConn.moveTo(1,20,0.1);
  //1 ist von 60 bis 70safe
  Serial.println(String(smartServoConn.getAngleRequest(2)) );
  smartServoConn.moveTo(2,-120,0.1);
  //2 ist von -170 bis 200 safe   200 ist rechts
  Serial.println(String(smartServoConn.getAngleRequest(3)) );
  smartServoConn.moveTo(3,-158,0.1);
  //3 ist von -111 bis 120 safe   120 ist unten
  delay(6000);
 */
}
