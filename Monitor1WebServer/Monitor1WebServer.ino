/*
 Web Server
 */

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {  0xA8, 0x61, 0x0A, 0x0F, 0x1A, 0xAA };
IPAddress ip(169, 254, 168, 139);
byte gateway[] = {192, 168, 40, 1};
byte subnet[] = {255, 255, 0, 0};
boolean haveMsg = false;

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(23);

void setup() {
 
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Ethernet WebServer Example");

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

  // start the server
  server.begin();
  
}


void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) 
  {
    if (haveMsg == false)
    {
      Serial.println("New client connected.");
      
      haveMsg = true;
    }
    client.println("Hello, client");
    
    char clientMsg = client.read();
    server.write(clientMsg);
    Serial.println(clientMsg);
    
  }
}
