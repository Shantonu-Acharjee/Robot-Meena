#include <Servo.h>

Servo Head; 
Servo RightHand;  
Servo LeftHand;
Servo Wrist;

int HeadInputPin = A0;
int RightHandInputPin = A1;
int LeftHandInputPin = A2;
int WristInputPin = A3;

int HeadInputPinState;
int RightHandInputPinState;
int LeftHandInputPinState;
int WristInputPinState;


int HeadMiddle = 65;
int RightHandMiddle = 0;
int LeftHandMiddle = 100;
int WristMiddle = 0;

int pos = 0;    

void setup() {
  Head.attach(9);
  RightHand.attach(10);
  LeftHand.attach(11);
  Wrist.attach(6);


  Head.write(HeadMiddle);
  RightHand.write(RightHandMiddle);
  LeftHand.write(LeftHandMiddle);
  Wrist.write(WristMiddle);

  pinMode(HeadInputPin, INPUT); 
  pinMode(RightHandInputPin, INPUT); 
  pinMode(LeftHandInputPin, INPUT); 
  pinMode(WristInputPin, INPUT); 
  
  Serial.begin(9600);
}

void loop() {


  HeadInputPinState = digitalRead(HeadInputPin); 
  RightHandInputPinState = digitalRead(RightHandInputPin); 
  LeftHandInputPinState = digitalRead(LeftHandInputPin); 
  WristInputPinState = digitalRead(WristInputPin); 




// Head -------------------------------------------------
  if(HeadInputPinState == HIGH){
    for (pos = 10; pos <= 110; pos += 1) { 
    Head.write(pos);              
    delay(15);                       
  }

  
  for (pos = 110; pos >= 10; pos -= 1) { 
    Head.write(pos);              
    delay(15);                       
  }
    
  }






  

  if(HeadInputPinState == LOW){
    Head.write(HeadMiddle);
  }

// Head End -----------------------------------------------




 

// RightHand ------------------------------------------------


  if(RightHandInputPinState == HIGH){
    for (pos = RightHandMiddle; pos <= 100; pos += 1){
    RightHand.write(pos);              
    delay(25);                       
  }

  
  for (pos = 100; pos >= RightHandMiddle; pos -= 1){ 
    RightHand.write(pos);              
    delay(25);                       
  }
    
  }





  


  if(RightHandInputPinState == LOW){
    RightHand.write(RightHandMiddle);
    
    
  }

 // RightHand -----------------------------------------------








 // LeftHand-----------------------------------------------------

  if(LeftHandInputPinState == HIGH){
   for (pos = 0; pos <= LeftHandMiddle; pos += 1){
    LeftHand.write(pos);              
    delay(25);                       
  }

  
  for (pos = LeftHandMiddle; pos >= 0; pos -= 1) { 
    LeftHand.write(pos);              
    delay(25);                       
  }
  }


  if(LeftHandInputPinState == LOW){
    LeftHand.write(LeftHandMiddle);
  }



  // LeftHand End----------------------------------------------  


  


//Wrist-------------------------------------------------------------
  
  if(WristInputPinState == HIGH){
    for (pos = 0; pos <= 50; pos += 1){
    Wrist.write(pos);              
    delay(10);                       
  }

  
  for (pos = 50; pos >= 0; pos -= 1) { 
    Wrist.write(pos);              
    delay(10);                       
  }

}


  if(WristInputPinState == LOW){
    Wrist.write(WristMiddle);
  }
  
  
//Wrist End-------------------------------------------------------------





}// End Loop
