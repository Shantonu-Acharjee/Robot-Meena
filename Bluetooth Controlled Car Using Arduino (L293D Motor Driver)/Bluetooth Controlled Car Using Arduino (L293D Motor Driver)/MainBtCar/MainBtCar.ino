#include <AFMotor.h>
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

char t;
void setup() {
Serial.begin(9600);

}

void loop() {

/*
  
if(Serial.available()){
  
  t = Serial.read();
  Serial.println(t);
  Serial.print(t);
  
}

*/

t = 'f';

if(t == 'F'){//move forward(all motors rotate in forward direction)
   
  motor1.setSpeed(255);
  motor1.run(FORWARD);

  motor2.setSpeed(255);
  motor2.run(FORWARD);

  motor3.setSpeed(255);
  motor3.run(FORWARD);
  
  motor4.setSpeed(255);
  motor4.run(FORWARD);
}




if(t == 'B'){//move Back(all motors rotate in Back direction)
   
  motor1.setSpeed(255);
  motor1.run(BACKWARD);

  motor2.setSpeed(255);
  motor2.run(BACKWARD);

  motor3.setSpeed(255);
  motor3.run(BACKWARD);
  
  motor4.setSpeed(255);
  motor4.run(BACKWARD);
}




if(t == 'R'){//move Left(all motors rotate in Left direction)
   
  motor1.setSpeed(255);
  motor1.run(BACKWARD);

  motor2.setSpeed(255);
  motor2.run(BACKWARD);

  motor3.setSpeed(255);
  motor3.run(FORWARD);
  
  motor4.setSpeed(255);
  motor4.run(FORWARD);
}




if(t == 'L'){//move RIGHT(all motors rotate in RIGHT direction)
   
  motor1.setSpeed(255);
  motor1.run(FORWARD);

  motor2.setSpeed(255);
  motor2.run(FORWARD);

  motor3.setSpeed(255);
  motor3.run(BACKWARD);
  
  motor4.setSpeed(255);
  motor4.run(BACKWARD);
}


else{
   motor1.setSpeed(0);
   motor2.setSpeed(0);
   motor3.setSpeed(0);
   motor4.setSpeed(0);
}
}
