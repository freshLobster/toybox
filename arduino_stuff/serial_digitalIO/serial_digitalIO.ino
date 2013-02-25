/* 
Uses serial data to turn on and off pins.
currently only reads one character at a time.
Also the pin numbers are offset by 2 because 
pins 0 and 1 are used for serial communication.
so if the serial reads 11 pin 13 will be controlled.
*/

const int numPins = 12;//for now I'm using 10 pins
                  //0-9 in the array
                  //2-12 on the arduino
                  //I'll expand to more numbers
                  //when I get around the serial's 
                  //read() limitations
boolean pins[numPins];

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  //initialize all non serial pins as output
  for (int i = 0; i < numPins; i++){
    pins[i] = false;
    pinMode(i+2, OUTPUT);
  } 
  //signals arduino is ready
  Serial.write('1'); 
}


void loop(){
 if (Serial.available() > 0) {
  int pin = Serial.read();
  //ascii offset
  pin -= 48;
  Serial.print("read ");
  Serial.println(pin);
  toggle(pin);
  setPins();
 }
} 

//sets individual pin states
void toggle(int pin){
 if (pins[pin] == true) pins[pin] = false;
  else pins[pin] = true; 
}

//goes through pins array and turns on appropriate pins
void setPins(){
 for (int i = 0; i < 12; i++){
   if (pins[i]== true) digitalWrite(i+2, HIGH);
   else digitalWrite(i+2, LOW);
 }
}
int readPin(int pin){
  return pins[pin];
}
