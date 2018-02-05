#include <Servo.h> 
// Declare the Servo pin 
int servoPin1 = 11; 
int servoPin2 = 10;
int servoPin3 = 9;
// Create a servo object 
Servo Servo1;
Servo Servo2;
Servo Servo3;

int incomingBit = 0;
//char incomingBit;    // for incoming serial data
 
void setup() {
  // We need to attach the servo to the used pin number 
  Servo1.attach(servoPin1);
  Servo2.attach(servoPin2);
  Servo3.attach(servoPin3);
  
  pinMode(servoPin1, OUTPUT);      // sets the digital pin as output
  pinMode(servoPin2, OUTPUT); 
  pinMode(servoPin3, OUTPUT);
   
  Serial.begin(19200);    // opens serial port, sets data rate to 19200 bps
}
void loop() {
  if (Serial.available() > 0) { 
    incomingBit = Serial.read();
/*The switch statement has a variable which can be an integer (int) or character (char) 
 * variable.The switch variable will be tested against the value in each case to see if 
 * they match. When a case is found that matches, the statements below the case will be 
 * run until the break keyword is reached. This will break the program flow out of the 
 * body of the switch statement and execution of the sketch will continue below the closing 
 * brace of the switch statement.If no matching case is found, then the code under the 
 default keyword will be run until its break statement is found.*/
    switch (incomingBit) {
      case '1':
          Servo1.write(0); 
          delay(1000); 
        // Make servo go to 90 degrees 
          Servo1.write(90); 
          delay(1000); 
          // Make servo go to 180 degrees 
          Servo1.write(180); 
          delay(1000); 
          //exit(0);
       break;

       case '2' :
         Servo1.write(0);
       break;

       case '3':
          Servo2.write(0); 
          delay(1000); 
        // Make servo go to 90 degrees 
          Servo2.write(90); 
          delay(1000); 
          // Make servo go to 180 degrees 
          Servo2.write(180); 
          delay(1000); 
          //exit(0);
       break;

       
       case '4' :
         Servo2.write(0);
       break;

       case '5':
          Servo3.write(0); 
          delay(1000); 
        // Make servo go to 90 degrees 
          Servo3.write(90); 
          delay(1000); 
          // Make servo go to 180 degrees 
          Servo3.write(180); 
          delay(1000); 
          //exit(0);
       break;

       case '6' :
         Servo3.write(0);
       break;

       default:
         Servo1.write(0);
         Servo2.write(0);
         Servo3.write(0);
       break;
    }
  }
}
  

