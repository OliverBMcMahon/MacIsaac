/* DHT-22 sensor with Arduino uno */

//Libraries
#include <DHT.h>
#include <Wire.h>
#include <SPI.h>
#include <Ethernet.h>

byte mac[] = {  0xA8, 0x61, 0x0A, 0x0F, 0x1A, 0xAA }; // Ethernet shield #1
IPAddress ip(192, 168, 40, 199); // Change to match Arduino static IP as needed
byte gateway[] = {192, 168, 40, 1}; // Change to match network gateway
byte subnet[] = {255, 255, 255, 0}; // Change to match network subnet mask
boolean haveMsg = false;

//Constants
#define DHTPIN 2        // DHT22 signal pin
#define DHTTYPE DHT22   // DHT 22  (AM2302)

DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
EthernetServer server(23);

//Variables
int chk;
float hum;  // % humidity value
float temp; // temperature value
char buff[80];
char humStr[12];
char tempStr[12];

void setup()
{
  char msg[32];
  Serial.begin(9600);
  while(!Serial);
  Serial.println();

	dht.begin();
  
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip, gateway, gateway, subnet);
  delay(1000);

  ip = Ethernet.localIP();
  Serial.println("Arduino IP address is: ");
  for (byte b=0; b < 4; b++)
  {
    Serial.print(ip[b], DEC);
    Serial.print(",");
  }
  Serial.println();
  server.begin();
  delay(1000);
}

void loop()
{
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) 
  {
    if (haveMsg == false) // Only do this once
    {
      Serial.println("New client connected.");
      haveMsg = true;
    }
    //Read data and store it to variables hum and temp
    hum = getHumidity();
    temp= getTemperature();

    //Print temp and humidity values to serial monitor
    dtostrf((double)hum, 6, 1, humStr);
    dtostrf((double)temp, 6, 1, tempStr);
    sprintf(buff, "%s,%s", humStr, tempStr);
    Serial.println(buff);
    
    client.flush();
    client.write(buff);
    client.stop();
  }
    
    delay(1000); 
}

double getTemperature()
{
  double t = dht.readTemperature();
  return t;
}

double getHumidity()
{
  double h = dht.readHumidity();
  return h;
}


   