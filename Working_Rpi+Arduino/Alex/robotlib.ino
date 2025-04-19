#include <AFMotor.h>
#include "constants.h"
// Direction values

//extern long deltaDist;
//extern long newDist;
//extern long forwardDist;

// Motor control
#define FRONT_LEFT   2 // M4 on the driver shield
#define FRONT_RIGHT  1 // M1 on the driver shield
#define BACK_LEFT    3 // M3 on the driver shield
#define BACK_RIGHT   4 // M2 on the driver shield

AF_DCMotor motorFL(FRONT_LEFT);
AF_DCMotor motorFR(FRONT_RIGHT);
AF_DCMotor motorBL(BACK_LEFT);
AF_DCMotor motorBR(BACK_RIGHT);

void move(int speed, int direction)
{
  
  motorFL.setSpeed(speed);
  motorFR.setSpeed(speed);
  motorBL.setSpeed(speed);
  motorBR.setSpeed(speed);

  switch(direction)
    {
      case BACK:
        motorFL.run(FORWARD);
        motorFR.run(BACKWARD);
        motorBL.run(BACKWARD);
        motorBR.run(FORWARD); 
      break;
      case GO:
        motorFL.run(BACKWARD);
        motorFR.run(FORWARD);
        motorBL.run(FORWARD);
        motorBR.run(BACKWARD); 
      break;
      case CW:
        motorFL.run(FORWARD);
        motorFR.run(FORWARD);
        motorBL.run(BACKWARD);
        motorBR.run(BACKWARD); 
      break;
      case CCW:
        motorFL.run(BACKWARD);
        motorFR.run(BACKWARD);
        motorBL.run(FORWARD);
        motorBR.run(FORWARD); 
      break;
      case STOP:
      default:
        motorFL.run(STOP);
        motorFR.run(STOP);
        motorBL.run(STOP);
        motorBR.run(STOP);
    }
}

void forward(float dist, float speed)
{
  if (dist > 0)
  {
    deltaDist = dist;
  }
  else
  {
    deltaDist = 9999999;
  }
  newDist = forwardDist + deltaDist;
  dir = (TDirection) FORWARD;
  move(speed, FORWARD);
}

void backward(float dist, float speed)
{
  if (dist > 0)
  {
    deltaDist = dist;
  }
  else
  {
    deltaDist = 9999999;
  }
  newDist = reverseDist + deltaDist;
  dir = (TDirection) BACKWARD;
  move(speed, BACKWARD);
}

void ccw(float dist, float speed)
{
  dir = (TDirection) LEFT;
  move(speed, CCW);
}

void cw(float dist, float speed)
{
  dir = (TDirection) RIGHT;
  move(speed, CW);
}

void stop()
{
  dir = (TDirection) STOP;
  move(0, STOP);
}
