
void setup(){
  //start serial connection
  Serial.begin(9600);
  //signal arduino is ready
  Serial.write('1'); 
}

void loop(){
  char inData[21]; // Allocate some space for the string
  char inChar; // Where to store the character read
  int goodRead = 0;
  while(Serial.available() > 0){
    goodRead = Serial.readBytesUntil('#', inData, 21);
  }
  if (goodRead != 0){
    String command = inData;
    activate(command);
  }
}

void activate(String command){
  char mode = getMode(command);
  int pin = getPin(command);
  int power = getPower(command);
  int input = 0;
  switch(mode){
    case 'r':
      pinMode(pin, INPUT);
      input = analogRead(pin);
      Serial.write(input);
      break;
    case 'w':
      pinMode(pin, OUTPUT);
      analogWrite(pin, power);
      break;
    default: break;
  }
}

char getMode(String command){
  return command.charAt(0);
}

int getPin(String command){
  int pin;
  int pinEnd = command.indexOf('@');
  String pinStr = command.substring(1, pinEnd);
  char buffer[pinStr.length()+1];
  pinStr.toCharArray(buffer, pinStr.length()+1);
  /*if (command.indexOf('@') >= 2){
    buffer[0] = command.charAt(1);
    buffer[1] = command.charAt(2);
  }
  else{ 
    buffer[0] = '0';
    buffer[1] = command.charAt(1);
  }*/
  pin = atoi(buffer);
  return pin;
}

int getPower(String command){
  int power;
  int pwrBegin = command.indexOf('@')+1;
  int pwrEnd = command.indexOf('#');
  String pwrStr = command.substring(pwrBegin, pwrEnd);
  char buffer[pwrStr.length()+1];
  pwrStr.toCharArray(buffer, pwrStr.length()+1);
  power = atoi(buffer);
  return power;
}


