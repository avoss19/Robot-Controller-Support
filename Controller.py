import pygame # controller
import paramiko # ssh

# controller mapping
speedMapping = 0 # 0 for joystick, 1 for triggers

# left and right joystick dead zones (current dead zone for ps4 controller)
xDeadZoneLeft = 0.06
yDeadZoneLeft = 0.06
xDeadZoneRight = 0.06
yDeadZoneRight = 0.06

# motor speeds (assumes there is the same possible speeds going in reverse)
maxMotorL = 1000
maxMotorR = 1000

def ssh():
    "hey"

# Initialize pygame
pygame.init()
pygame.joystick.init()

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
    global motorL, motorR

    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft:
        motorL = 0
        motorR = 0

    elif speedMapping == 0:
        motorL = maxMotorL * -yAxisRight
        motorR = maxMotorR * -yAxisRight
        
    if speedMapping == 1:
        if triggerRight >= 0:
            motorL = .5 * maxMotorL * (triggerRight+1)
            motorR = .5 * maxMotorL * (triggerRight+1)
        elif triggerLeft > 0:
            motorL = .5 * maxMotorL * -(triggerLeft+1)
            motorR = .5 * maxMotorL * -(triggerLeft+1)

def roboDirection():
    "hey"

while True:
   joysticks()
   roboSpeed()
   print motorL, motorR, xAxisRight, yAxisRight, triggerRight
