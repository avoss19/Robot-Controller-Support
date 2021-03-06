import pygame # controller
import robotonomy.RoboPiLib as RPL
import robotonomy.setup
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal
import os

os.putenv('SDL_VIDEODRIVER', 'fbcon')

# Weclome Screen
print "#"*60
print "Welcome to the BSM robot controller support python program!"
print "#"*60
print "I recommend choosing the joystick layout."
print "For support please visit https://github.com/avoss19/Robot-Controller-Support"
print "#"*60
print "Please select a controller scheme:"
print "0. Speed control w/ right joystick"
print "1. Speed control w/ triggers"
speedMapping = input("$: ")
print "#"*60

# Defualts to joystick control if input was not put in correctly
if speedMapping == 0:
    speedMapping = 0
if speedMapping == 1:
    speedMapping = 1
else:
    speedMapping = 0

# left and right joystick dead zones (current dead zone for ps4 controller)
xDeadZoneLeft = 0.06
yDeadZoneLeft = 0.06
xDeadZoneRight = 0.06
yDeadZoneRight = 0.06

# motor speeds (assumes there is the same possible speeds going in reverse)
maxMotorL = 500
maxMotorR = 500

# Initialize pygame
pygame.init()
pygame.joystick.init()
pygame.display.init()

# get joystick readings
def joysticks():
    global xAxisLeft, yAxisLeft, xAxisRight, yAxisRight, triggerLeft, triggerRight

    pygame.event.get()

    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        xAxisLeft = joystick.get_axis(0)
        yAxisLeft = joystick.get_axis(1)

        xAxisRight = joystick.get_axis(2)
        yAxisRight = joystick.get_axis(3)

        triggerLeft = joystick.get_axis(4)
        triggerRight = joystick.get_axis(5)

# control speed
def roboSpeed():
    global motorSpeedL, motorSpeedR

    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft:
        motorSpeedL = 0
        motorSpeedR = 0

    elif speedMapping == 0:
        motorSpeedL = maxMotorL * -yAxisRight
        motorSpeedR = maxMotorR * -yAxisRight

    if speedMapping == 1:
        if triggerRight >= 0:
            motorSpeedL = .5 * maxMotorL * (triggerRight+1)
            motorSpeedR = .5 * maxMotorL * (triggerRight+1)
        elif triggerLeft > 0:
            motorSpeedL = .5 * maxMotorL * -(triggerLeft+1)
            motorSpeedR = .5 * maxMotorL * -(triggerLeft+1)

def roboDirection():
    global motorL, motorR

    if -xDeadZoneLeft < xAxisLeft < xDeadZoneLeft:
        motorL = motorSpeedL
        motorR = motorSpeedR

    elif xAxisLeft <= 0:
        motorL = motorSpeedL - (motorSpeedL * (-xAxisLeft))
        motorR = motorSpeedR
    elif xAxisLeft > 0:
        motorL = motorSpeedL
        motorR = motorSpeedR + (motorSpeedR * (-xAxisLeft))

def switchControllerScheme():
    global speedMapping
    joystick = pygame.joystick.Joystick(0)
    if joystick.get_button(5) == 1:
        speedMapping = (speedMapping + 1) % 2

def KitBotSpeed(speed):
    center = 1500
    return speed + center

def interrupted(signum, frame): # this is the method called at the end of the alarm]
    stopAll()

def stopAll():
  try:
    RPL.servoWrite(motorL,1500)
    RPL.servoWrite(motorR,1500)
  except:
    print "error except"
    pass

events = pygame.event.get()
for e in events:
    pass
# -------------------Main Program--------------------------
# Current Issues:
# Does not read input from computer
while True:
    joysticks()
    roboSpeed()
    roboDirection()
    print motorL, motorR
    RPL.servoWrite(0,KitBotSpeed(motorL))
    RPL.servoWrite(1,KitBotSpeed(-motorR))
    switchControllerScheme()
