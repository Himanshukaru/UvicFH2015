//
// CAN_Arduino
//
// Create a dummy CAN network transmitting device
// Developed with [embedXcode](http://embedXcode.weebly.com)
//
// Author 		Adam Hjermstad
// 				Uvic Formula Hybrid
//
// Date			2015-02-05 8:52 AM
// Version		<#version#>
//
// Copyright	© Adam Hjermstad, 2015
// Licence		<#license#>
//
// See         ReadMe.txt for references
//

// Extra Libraries for CAN and SPI
#include <Arduino.h>
#include <arduino.h>
#include "mcp_can.h"
#include <SPI.h>

// Core library for code-sense - IDE-based
#if defined(WIRING) // Wiring specific
#include "Wiring.h"
#elif defined(MAPLE_IDE) // Maple specific
#include "WProgram.h"
#elif defined(MPIDE) // chipKIT specific
#include "WProgram.h"
#elif defined(DIGISPARK) // Digispark specific
#include "Arduino.h"
#elif defined(ENERGIA) // LaunchPad specific
#include "Energia.h"
#elif defined(LITTLEROBOTFRIENDS) // LittleRobotFriends specific
#include "LRF.h"
#elif defined(MICRODUINO) // Microduino specific
#include "Arduino.h"
#elif defined(TEENSYDUINO) // Teensy specific
#include "Arduino.h"
#elif defined(REDBEARLAB) // RedBearLab specific
#include "Arduino.h"
#elif defined(SPARK) // Spark specific
#include "application.h"
#elif defined(ARDUINO) // Arduino 1.0 and 1.5 specific
#include "Arduino.h"
#else // error
#error Platform not defined
#endif // end IDE

// Include application, user and local libraries
#include "LocalLibrary.h"


// Define constants
#define trigPin 5
#define echoPin 6
#define distance_cm 0x00
#define distance_mm 0x01

// Set CS pin to 10
MCP_CAN CAN(10);

// Initialize data section of CAN frame
unsigned char stmp_cm[8] = {    0x00, //looping variable
                                0x00, //distance in cm
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00};

unsigned char stmp_mm[8] = {    0x00, //most sig bits distance in mm
                                0x00, //least sig bits distance in mm
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00,
                                0x00};

//

// Initial Setup:
// Start CAN bus, Start serial Communication
void setup() {
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

// Function returns distance as read from hypersonic distance sensor
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

void loop() {
    long centimeters = ping();
    stmp_cm[0]++;
    stmp_cm[1] = (char)centimeters;

    long milimeters = centimeters*10;
    long mm_LSB_temp = milimeters & 0x000000ff;
    char mm_LSB = (char) mm_LSB_temp;

    long mm_MSB_temp = milimeters & 0x0000ff00;
    mm_MSB_temp = mm_MSB_temp >> 8;
    char mm_MSB = (char) mm_MSB_temp;

    stmp_mm[0] = mm_MSB;
    stmp_mm[1] = mm_LSB;
    
    
    if(stmp_cm[0]>0xff){
        stmp_cm[0]=0x00;
    }

    CAN.sendMsgBuf(distance_cm, 0, 8, stmp_cm); //send cm
    delay(75);
    CAN.sendMsgBuf(distance_mm, 0, 8, stmp_mm); //send mm
    delay(75);                       // send data per 100ms
    
    
}
