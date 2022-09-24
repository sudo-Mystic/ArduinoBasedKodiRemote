/*
Code By - Mystic
GITHUB - https://github.com/sudo-Mystic/ArduinoBasedKodiRemote/
*/
#include <IRremote.h>

int RECV_PIN = 8;  //Pin on which IR receiver is connected

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn(); 
  Serial.setTimeout(1);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);   //Sending the Hex code to host as soon as we receive it
    irrecv.resume();  //ready to get new code
}
}
