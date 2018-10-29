////////////////////////////////////////////////////////////////////////////////////
// Autor: Arturo P Y Alejandro M
//
// Programa que lee valores del sensor de luz y los envia a la
// raspberry pi a traves de un modulo bluetooth 
//
////////////////////////////////////////////////////////////////////////////////////
int lighPin=0; //Selecciona el pin 0 como la fuente del dato que recive

void setup() {
  Serial.begin(9600);
  pinMode(lighPin,INPUT);
}

void loop() {
  int reading = analogRead(lighPin); //Reading lee valores del LightPin
  //Serial.print('D');
  char str_reading[12];
  sprintf(str_reading,"%d",reading); //El dato de int se convierte a str
  Serial.print(str_reading);
  Serial.print('\n');
  //delay(10); //
}
