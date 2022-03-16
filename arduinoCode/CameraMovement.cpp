/*
  the source code
*/

#include "Arduino.h"#include "CameraMovement.h"

//libraries needed for sin function and printing, apparently
#include "stdio.h"      /* printf */
#include "math.h"       /* sin */
#define PI 3.14159265

//libs needed for time
#include "chrono"
#include "iostream"
#include "sys/time.h"
#include "ctime"

//add another comment

// visit here https://www.arduino.cc/en/Hacking/libraryTutorial for a simple tutorial
// visit https://docs.arduino.cc/hacking/software/ArduinoStyleGuide for the style guide
// Basically: 1. avoid #define 2. avoid pointer (besides this->) 3.that's it
// here is the place for the source code, make sure it matches with the CameraMovement.h file!

CameraMovement:: CameraMovement(int v, int h){
    // this is the constructor that initialize the instance when a new instance is created
    // I guess it makes sense to use some sort of random function or use sin/cos
    // but as a seed we can use the time in milis and store it as unsigned long

    // starting to count the time in seconds
    time_t elapsedseconds = time();

    int param = elapsedseconds; /* seed for the sin calculation */
    int result; /* stores the result of the calculation */

    // calculating the sin function
    result = sin (param*PI/180);

    printf(result);

    h = result;
    v = result / 10;

    this->current_horizontalcurrent_horizontal = h;
    this->current_vertical = v;
    // personally I think it is a good habit to use the prepend this for any local attribute & function in the class, those this is not required for compile
}


int[] CameraMovement:: getNext(){
    // return an array of integer, int[0] is the next angle for the bottom servo (horizontal) (between -90 to 90)
    // int[1] is the next angle for the top servo (vertical) (between 0 to 90)  -JC
}
