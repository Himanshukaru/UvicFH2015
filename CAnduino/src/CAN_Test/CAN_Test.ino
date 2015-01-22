//Task: Create a dummy CAN network with a real world data being input
#include <mcp_can.h>
#include <SPI.h>

MCP_CAN CAN(10);                                      // Set CS to pin 10

void setup()
{
    Serial.begin(115200);

	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);

START_INIT:

    if(CAN_OK == CAN.begin(CAN_500KBPS))                   // init can bus : baudrate = 500k
    {
        Serial.println("CAN BUS Shield init ok!");
    }
    else
    {
        Serial.println("CAN BUS Shield init fail");
        Serial.println("Init CAN BUS Shield again");
        delay(100);
        goto START_INIT;
    }
}

long ping(){
	long duration, distance;
	digitalWrite(trigPin, LOW);  
	delayMicroseconds(2); 
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10); 
	digitalWrite(trigPin, LOW);
	duration = pulseIn(echoPin, HIGH);
	distance = (duration/2) / 29.1;	
	return distance;
}

void loop()
{
	//Needs a bit of refinning but I'll do that when I set up the circuit
	distance = ping();

	if (distance >= 200 || distance <= 0){
		Serial.println("Out of range");
	}
	else {
		Serial.print(distance);
		Serial.println(" cm");
	}
    CAN.sendMsgBuf(0x00, 0, 8, int(distance));
  
    
    delay(2500);
    // send data per 2.5s
}