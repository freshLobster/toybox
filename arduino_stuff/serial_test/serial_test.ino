// Open a serial connection and flash LED when input is received

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  pinMode(13, OUTPUT); 
}

void loop(){ 
  Serial.write('1');
  if(Serial.read() > 0){      // if data present, blink
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    Serial.write('0');
  }
} 

