#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#define USE_SERIAL Serial
ESP8266WiFiMulti WiFiMulti;

const int relayPin =  2;
void setup() {
   USE_SERIAL.begin(9600);
  // USE_SERIAL.setDebugOutput(true);
   USE_SERIAL.println();
   USE_SERIAL.println();
   USE_SERIAL.println();
   for(uint8_t t = 4; t > 0; t--) {
     //  USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
       USE_SERIAL.flush();
       delay(1000);
   }
   WiFi.mode(WIFI_STA);
   // provide our SSID and Password for WIFI network connection
   WiFiMulti.addAP("AE326E", "100865146");
  pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  pinMode(relayPin, OUTPUT);
  

   
}
void loop() {
   // wait for WiFi connection
   if((WiFiMulti.run() == WL_CONNECTED)) {
       HTTPClient http;
       USE_SERIAL.println("Sending Get Request to Server.......");
       http.begin("http://www.crescente.com.ar/dev/data.html"); //HTTP URL for hosted server(local server)
       //192.168.43.161 - HOST     PORT: 3000 and /api is the target api we need to hit to get response
       int httpCode = http.GET();
       // USE_SERIAL.println("After GET Request");
       // httpCode will be negative on error
       if(httpCode > 0) {
           if(httpCode == HTTP_CODE_OK) {
             //HTTP_CODE_OK means code == 200
               String payload = http.getString();// gives us the message received by the GET Request
               USE_SERIAL.println("payload");// Displays the message onto the Serial Monitor
               USE_SERIAL.println(payload);
               if(payload.equals("1")){
                  USE_SERIAL.println("yeah man");
                  digitalWrite(LED_BUILTIN, LOW);// LOW means ON in esp8266
                  digitalWrite(relayPin, LOW);
                  delay(2000);
               }else if(payload.equals("0")){
                  digitalWrite(LED_BUILTIN, HIGH);
                  digitalWrite(relayPin, HIGH);
                  delay(2000);
               }else{
                  USE_SERIAL.println("Something's wrong dude");
               }
           }
       } else {
           USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
       }
       http.end();
   }
   delay(5000);// repeat the cycle every 5 seconds.
}
