/*
  the source code
*/

#include "Arduino.h"
#include "CameraMovement.h"

//libraries needed for sin function and printing, apparently
#include "stdio.h"      /* printf */
#include "math.h"       /* sin */

//libs needed for time
/*#include "chrono"
#include "iostream"
#include "sys/time.h"
#include "ctime"*/

//add another comment

// visit here https://www.arduino.cc/en/Hacking/libraryTutorial for a simple tutorial
// visit https://docs.arduino.cc/hacking/software/ArduinoStyleGuide for the style guide
// Basically: 1. avoid #define 2. avoid pointer (besides this->) 3.that's it
// here is the place for the source code, make sure it matches with the CameraMovement.h file!
//double CameraMovement:: _PI = 3.14159265;

CameraMovement::CameraMovement(){
    current[0] =0;
    current[1] =0;
    myTime =0;
}


void CameraMovement::getNext(int arr[]){
  int currentv= current[0];
  int currenth = current[1];

      // do sth to update arr[]
      int phs= (millis()/1000) - myTime;
      if (phs >= 360){
        noInterrupts ();
        timer0_millis = 0;
        interrupts ();
        myTime = millis()/1000;
      }
      //storing the sine value
      mySin = sin((float)phs);

      // use multiple sin waves that can add ontop of each other

      //get the value of the random number at time of read and at time of beginning
      // randTimeBegin = 0;
      // randTimeCurrent = randTime;
      //
      // //map randtimeCurrent and -Begin to the max min angle that the robots allow to
      // map servoBigAngle (randTimeBegin, RandTimeBegin, RandTimeCurrent, 45, 135);
      // //can I limit the overflow to another value?
      // // use if value myTime=0

      //mapping the sine to the max min degrees
      myAngle = mapf(mySin, -1.0, 1, 45, 135);

      // turning the mapped float into an int
      arr[0] = (int)myAngle ;
      arr[1] = (int)myAngle;



  current[0] = arr[0];
  current[1] = arr[1];
  //current[] = arr[];
}

float CameraMovement::mapf(float x, float in_min, float in_max, int out_min, int out_max){
    return (float) (x-in_min) * (out_max-out_min) / (float)(in_max-in_min)+out_min;
}
