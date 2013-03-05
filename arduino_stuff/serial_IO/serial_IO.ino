
void setup(){
  //start serial connection
  Serial.begin(9600);
  //signal arduino is ready
  Serial.write('1'); 
}

void loop(){
  char inData[21]; // Allocate some space for the string
  char inChar; // Where to store the character read
  int goodRead = 0; //0 if readBytes fails
  //read bytes when serial is sending data
  while(Serial.available() > 0){
    if (Serial.read() == '!'){
      //when start byte is read, bytes are stored in 
      //buffer until the end byte is read
      goodRead = Serial.readBytesUntil('#', inData, 21);
    }
  }
  if (goodRead != 0){ //nothing is done if readByte failed
    String command = inData; //convert from char array to String object
    activate(command); //parse and interpret command
  }
}

void activate(String command){
  char mode = getMode(command);
  int pin = getPin(command);
  int power = getPower(command);
  int input = 0;//to store data from reading pin
  switch(mode){
    //read
  case 'r':
    pinMode(pin, INPUT);
    input = analogRead(pin);
    Serial.write(input);
    break;
    //write
  case 'w':
    pinMode(pin, OUTPUT);
    analogWrite(pin, power);
    break;
    //tone (generates a square wave of the appropriate frequency)
  case 't':
    pinMode(pin, OUTPUT);
    tone(pin, power);
    break;
    //quiet (turns off square wave)
  case 'q':
    noTone(pin);
    break;
  default: 
    break;
  }
}

//returns the mode as a char
char getMode(String command){
  return command.charAt(0);
}

//returns pin number as an int
int getPin(String command){
  int pin;
  int pinEnd = command.indexOf('@');
  //finds substring of command between mode character and @ flag
  String pinStr = command.substring(1, pinEnd);
  char buffer[pinStr.length()+1];
  //converts string object to char array
  pinStr.toCharArray(buffer, pinStr.length()+1);
  //converts char array to int
  pin = atoi(buffer);
  return pin;
  
  //how I attempted to solve this before
  //without atoi
  //left here for an example of bad code
  /*if (command.indexOf('@') >= 2){
   buffer[0] = command.charAt(1);
   buffer[1] = command.charAt(2);
   }
   else{ 
   buffer[0] = '0';
   buffer[1] = command.charAt(1);
   }*/
}

//returns the power as an int
int getPower(String command){
  //uses the same procedure as getPin
  int power;
  int pwrBegin = command.indexOf('@')+1;
  int pwrEnd = command.indexOf('#');
  //finds the string between @ and #
  String pwrStr = command.substring(pwrBegin, pwrEnd);
  char buffer[pwrStr.length()+1];
  pwrStr.toCharArray(buffer, pwrStr.length()+1);
  power = atoi(buffer);
  return power;
}



