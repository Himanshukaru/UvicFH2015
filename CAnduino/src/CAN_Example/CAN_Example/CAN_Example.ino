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

long ping()
{
    long duration, distance;
    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    distance = (duration/2) / 29.1; //in cm
    return distance;
}

unsigned char stmp[8] = {   0x00, //looping variable
                            0x00, //distance in cm
                            0x00, //most sig bits distance in mm
                            0x00, //least sig bits distance in mm
                            0x00, 
                            0x00, 
                            0x00, 
                            0x00};
void loop()
{
    long centimeters = ping();
    //Serial.print(distance, DEC);
    stmp[0]++;
    stmp[1] = (char)centimeters; //in cm

/*  //This probably won't work as is but basically I want to break a num larger than 0xff into 2 pieces 
    //it's most sig and least sig bits and then send those individually, then we can work on figuring out
    //how to recombine them on the other side

    long milimeters = centimeters*10;
    long mm_LSB_temp = milimeters && 0x000000ff;
    char mm_LSB = (char) mm_LSB_temp;

    long mm_MSB_temp = milimeters && 0x0000ff00;
    mm_MSB_temp = mm_MSB_temp >> 8;
    char mm_MSB = (char) mm_MSB_temp;

    stmp[2] = mm_MSB;
    stmp[3] = mm_LSB;
*/

    if(stmp[0]>0xff){
      stmp[0]=0x00;
    }

    CAN.sendMsgBuf(0x00, 0, 8, stmp);
    delay(100);                       // send data per 100ms
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
