// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>
#define trigPin 5
#define echoPin 6
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

unsigned char stmp[8] = {0, 1, 2, 3, 4, 5, 6, 7};
void loop()
{
    // send data:  id = 0x00, standrad flame, data len = 8, stmp: data buf
    	long duration, distance;
	digitalWrite(trigPin, LOW);  // Added this line
	delayMicroseconds(2); // Added this line
	digitalWrite(trigPin, HIGH);
//  delayMicroseconds(1000); - Removed this line
	delayMicroseconds(10); // Added this line
	digitalWrite(trigPin, LOW);
	duration = pulseIn(echoPin, HIGH);
	distance = (duration/2) / 29.1;
    
    Serial.print(distance, DEC);
    stmp[1] = (char)distance;
    stmp[0]++;
    
    
    CAN.sendMsgBuf(0x00, 0, 8, stmp);
    if(stmp[0]>0xff){
      stmp[0]=0;
    }
    delay(100);                       // send data per 100ms
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
