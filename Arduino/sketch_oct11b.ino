#include <SoftwareSerial.h>
const int rxpin=0;
const int txpin=1;
int lightPin=0;
SoftwareSerial Bluetooth(rxpin,txpin);



void setup() {
  // put your setup code here, to run once:
pinMode(lightPin,INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int reading=analogRead(lightPin);

Bluetooth.println(reading);
Serial.println(reading);
delay(100);

}
