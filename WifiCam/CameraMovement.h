#ifndef CameraMovement_h
#define CameraMovement_h

#include "Arduino.h"
class CameraMovement
{
  public:
    int current_vertical;
    int current_horizontal;

    CameraMovement();
    void getNext(int arr[]);
  private:
    static double _PI;
    unsigned long myTime;
    unsigned long randTime;
    volatile unsigned long timer0_millis;
    float mapf(float x, float in_min, float in_max, int out_min, int out_max);
    float myTimeF;
    float mySin;
    float myAngle;
    int myAngleInt;
    int randTimeBegin;
    int randTimeCurrent;
    int current[];
    // private attributes are only visible for functions and subclass inside this class
};

#endif
