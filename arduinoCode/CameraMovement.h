/*
  Control the cameramovement
*/
#ifndef CameraMovement_h
#define CameraMovement_h

#include "Arduino.h"
// visit here https://www.arduino.cc/en/Hacking/libraryTutorial for a simple tutorial
// .h file is the header file, it should list out all the attributes and functions in the class
class CameraMovement
{
  public:
    // public attributes and methods are "visiable" for other class and function
    int current_vertical;
    int current_horizontal;
    
    CameraMovement(int v, int h);
    // I will suggest have a function like this to be used in the main code
    // return an array of integer, int[0] is the next angle for the bottom servo (horizontal) (between -90 to 90)
    // int[1] is the next angle for the top servo (vertical) (between 0 to 90)  -JC
    void getNext(int arr[]);
  private:
    static double _PI;    
    unsigned long myTime;
    unsigned long randTime;
    int randTimeBegin;
    int randTimeCurrent;
    int current[];
    float mapf(long x, long in_min, long in_max, long out_min, long out_max);
    // private attributes are only visible for functions and subclass inside this class
};

#endif
