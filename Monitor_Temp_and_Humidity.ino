/* DHT-22 sensor with Arduino uno */

//Libraries
#include <DHT.h>
#include <Wire.h>
#include <SPI.h>
#include <Ethernet.h>

byte mac[] = {0xA8, 0x61, 0x0A, 0x0F, 0x1A, 0xAA}; // Ethernet shield #1
IPAddress ip(10, 10, 25, 199); // Change to match Arduino static IP as needed
byte gateway[] = {10, 10, 25, 1}; // Change to match network gateway
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
  Serial.begin(9600);
  dht.begin();

  Ethernet.begin(mac, ip);
  server.begin();
}

void loop()
{
  EthernetClient client = server.available();
  if (!client) return;

  float hum = dht.readHumidity();
  float temp = dht.readTemperature();

  if (isnan(hum) || isnan(temp)) {
    client.println("ERR");
    client.stop();
    return;
  }

  client.print(hum, 1);
  client.print(",");
  client.println(temp, 1);
  client.stop();
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


   
