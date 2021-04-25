#define pirPIN 2
int PIRValue = 0;
int waitTime = 5000;
boolean lockLow = true;
boolean takeLowTime = false;
long unsigned int lowIn;

#define ledPin 3

void setup() {
  // setup the serial connection
  Serial.begin(9600);
  // set the pin to take input
  pinMode(pirPIN, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
//  blinkLED(ledPin, 100);
  PIRSensor();
}

void PIRSensor(){
   if(digitalRead(pirPIN) == HIGH) {
    blinkLED(ledPin, 100);
    // checks if there was no previous motion detected
    // this shows the state has changed
    if(lockLow){
      PIRValue = 1;
      lockLow = false;
      Serial.println("Motion detected!");
      delay(50);
    }
    takeLowTime = true;
  }
  
  if(digitalRead(pirPIN) == LOW){
    // saves the current runtime if motion is not detected after being previously detected
    // this allows for downtime to be calculated and reset 
    // this will run the first time the motion is no longer detected
      if (takeLowTime){
          lowIn = millis();
          // stops the downtime from being calculated if the state has not changed
          takeLowTime = false;
      }
      // checks if no motion has been detected beyond a certain period so as to reset
      // and allow for motion to be detected again
      // this only runs only if the state of the motion sensor has not changed
      if(!lockLow && millis() - lowIn > waitTime){
        PIRValue = 0;
        lockLow = true;
        Serial.println("Motion ended");
        delay(50);
      }
  }

}

void blinkLED(int pin, int blinkRate){
  digitalWrite(pin, HIGH);
  delay(blinkRate);
  digitalWrite(pin, LOW);
  delay(blinkRate);
 }
