/* How to use the DHT-22 sensor with Arduino uno
   Temperature and humidity sensor
   More info: http://www.ardumotive.com/how-to-use-dht-22-sensor-en.html
   Dev: Michalis Vasilakis // Date: 1/7/2015 // www.ardumotive.com */

//Libraries
#include <DHT.h>
#include <Wire.h>
#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {  0xA8, 0x61, 0x0A, 0x0F, 0x1A, 0xAA };
IPAddress ip(169, 254, 168, 139);
byte gateway[] = {192, 168, 40, 1};
byte subnet[] = {255, 255, 0, 0};
boolean haveMsg = false;

//Constants
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)

DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
EthernetServer server(23);

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value
char buff[80];
char humStr[12];
char tempStr[12];

void setup()
{
  Serial.begin(9600);
  while(!Serial);
	dht.begin();
  Serial.println();

    // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip, gateway, gateway, subnet);

  ip = Ethernet.localIP();
  Serial.println("My IP address is: ");
  for (byte b=0; b < 4; b++)
  {
    Serial.print(ip[b], DEC);
    Serial.print(",");
  }
  Serial.println();
  server.begin();

}

void loop()
{
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) 
  {
    if (haveMsg == false)
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
    
    //char clientMsg = client.read();
    server.write(buff);
    client.write(buff);
    //Serial.println(clientMsg);
    client.stop();
  }
    
    
    delay(2000); //Delay 2 sec.
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


   