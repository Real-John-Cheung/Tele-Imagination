/*
  the source code
*/

#include "Arduino.h"
#include "CameraMovement.h"

// visit here https://www.arduino.cc/en/Hacking/libraryTutorial for a simple tutorial
// visit https://docs.arduino.cc/hacking/software/ArduinoStyleGuide for the style guide 
// Basically: 1. avoid #define 2. avoid pointer (besides this->) 3.that's it
// here is the place for the source code, make sure it matches with the CameraMovement.h file!

CameraMovement:: CameraMovement(int v, int h){
    // this is the constructor that initialize the instance when a new instance is created
    this->current_horizontalcurrent_horizontal = h;
    this->current_vertical = v;
    // personally I think it is a good habit to use the prepend this for any local attribute & function in the class, those this is not required for compile
}

int[] CameraMovement:: getNext(){
    // return an array of integer, int[0] is the next angle for the bottom servo (horizontal) (between -90 to 90)
    // int[1] is the next angle for the top servo (vertical) (between 0 to 90)  -JC
}

