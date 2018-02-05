#include <Servo.h>
int servoPin1 = 3;
int servoPin2 = 10;
int servoPin3 = 9;

Servo Servo1; //for weed 1 (face)
Servo Servo2; //for weed 2 (nose)
Servo Servo3; //for weed 3 (eye)

int incomingBit = 0;

void setup() {
 
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
  Servo3.attach(servoPin3);
  
  pinMode(servoPin1, OUTPUT); 
  pinMode(servoPin2, OUTPUT); 
  pinMode(servoPin3, OUTPUT);
  
  Serial.begin(19200);  
}
void loop() {
  if (Serial.available() > 0) { 
    incomingBit = Serial.read();

    switch (incomingBit) {
       // for RHS camera (dirtection:from front facing AgBot)

       
       case '1':
        //weed 1 detected,move spray to weed
        // servo 180 degree,facing right side weed(dirtection:from front facing AgBot)
          Servo1.write(180); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo1.write(90); 
       break;

       case '2' : //no weed detected, rest spray facing earth
         Servo1.write(90);
       break;

        case '3':
        //weed 2 detected,move spray to weed
        // servo 180 degree,facing right side weed(dirtection:from front facing AgBot)
          Servo2.write(180); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo2.write(90); 
       break;

       case '4' : //no weed detected, rest spray facing earth
         Servo2.write(90);
       break;

       case '5':
        //weed 3 detected,move spray to weed
        // servo 180 degree,facing right side weed(dirtection:from front facing AgBot)
          Servo3.write(180); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo3.write(90); 
       break;

       case '6' : //no weed detected, rest spray facing earth
         Servo3.write(90);
       break;



       
       // for LHS camera (dirtection:from front facing AgBot)

       
       case '7':
        //weed 1 detected,move spray to weed
        // servo 0 degree,facing left side weed(dirtection:from front facing AgBot)
          Servo1.write(0); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo1.write(90); 
       break;

       case '8' : //no weed detected, rest spray facing earth
         Servo1.write(90);
       break;

       case '9':
        //weed 2 detected,move spray to weed
        // servo 0 degree,facing left side weed(dirtection:from front facing AgBot)
          Servo2.write(0); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo2.write(90); 
       break;

       case '10' : //no weed detected, rest spray facing earth
         Servo2.write(90);
       break;

       case '11':
        //weed 3 detected,move spray to weed
        // servo 0 degree,facing left side weed(dirtection:from front facing AgBot)
          Servo3.write(0); 
         //spray for 3 second
          delay(3000); 
        // Servo 90 degree, facing earth
          Servo3.write(90); 
       break;

       case '12' : //no weed detected, rest spray facing earth
         Servo3.write(90);
       break;


        default://rest facing earth
         Servo1.write(90);
         Servo2.write(90);
         Servo3.write(90);
       break;
    }
  }
}

