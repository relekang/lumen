String inputString = "";
boolean stringComplete = false;
int led = 5;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);

  pinMode(led, OUTPUT);
  pinMode(lon, OUTPUT);
  pinMode(loff, OUTPUT);
}

void loop() {
  if (stringComplete) {
    if(inputString == "on"){
      digitalWrite(led, HIGH);
    } else if (inputString == "off"){
      digitalWrite(led, LOW);
    } else if (inputString == "blink"){
      digitalWrite(led, HIGH);
      delay(1000);
      digitalWrite(led, LOW);
    } else {
      Serial.println("Not a known command: " + inputString);
    }
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read(); 
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}


