import pygame

# controller mapping
speedMapping = 0 # 0 for joystick, 1 for right trigger

# left and right joystick dead zones (current dead zone for ps4 controller)
xDeadZoneLeft = 0.06
yDeadZoneLeft = 0.06
xDeadZoneRight = 0.06
yDeadZoneRight = 0.06

# motor speeds (assumes there is the same possible speeds going in reverse)
maxMotorL = 1000
maxMotorR = 1000

# Initialize
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
    if speedMapping == 0:
        motorL = maxMotorL * -yAxisRight
        motorR = maxMotorR * -yAxisRight
    if speedMapping == 1:
        motorL = maxMotorL * -triggerRight
        motorR = maxMotorL * -triggerRight

def roboDirection():
    "hey"

while True:
   joysticks()
   roboSpeed()
