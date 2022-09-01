int HeadInputPin = 7;
int RightHandInputPin = 6;
void setup() {
  pinMode(RightHandInputPin, OUTPUT);

}

void loop() {
  digitalWrite(RightHandInputPin, HIGH);
  delay(5000);
  digitalWrite(RightHandInputPin, LOW);
  delay(5000);

}
