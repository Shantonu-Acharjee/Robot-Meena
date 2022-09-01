#include <Servo.h>

Servo Head; 
Servo RightHand;  
Servo LeftHand;
Servo Wrist;

int pos = 0;    

void setup() {
  Head.attach(9);
  RightHand.attach(10);
  LeftHand.attach(11);
  Wrist.attach(6);
  Serial.begin(9600);
}

void loop() {
  
  Head.write(0); 
  RightHand.write(0);
  LeftHand.write(0);
  Wrist.write(0); 
  delay(1000);



  Head.write(110); 
  RightHand.write(100);
  LeftHand.write(100);
  Wrist.write(45);
  delay(1000);

  
  
  
  
  
  
              
    
}
