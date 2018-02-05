#include <Servo.h>
int servoPin1 = 3;
Servo Servo1;

int incomingBit = 0;

void setup() {
 
  Servo1.attach(servoPin1);
  
  pinMode(servoPin1, OUTPUT); 
  Serial.begin(19200);  
}
void loop() {
  if (Serial.available() > 0) { 
    incomingBit = Serial.read();

    switch (incomingBit) {
       // for RHS camera (dirtection:from front facing AgBot)
       case '1':
        //weed detected,move spray to weed
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

       
       // for LHS camera (dirtection:from front facing AgBot)
       case '7':
        //weed detected,move spray to weed
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

        default://rest facing earth
         Servo1.write(90);
       break;
    }
  }
}

