# Tested w/ PS4 controller on Mac OSX

import pygame # controller
import sys, paramiko # ssh

# Weclome Screen
print "#"*60
print "Welcome to the BSM robot controller support python program!"
print "#"*60
print "I recommend choosing the joystick layout."
print "For support please visit https://github.com/avoss19/Robot-Controller-Support"
print "#"*60
print "Please select a controller sceme:"
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

# SSH login
hostname = "192.168.21.113" # ip address
password = "Engineering!1"

username = "student"
port = 22

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

def KitBotSpeed(speed):
    center = 1500
    return speed + center

# SSH (tested on personal computer, but not robot)
def sshInit():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())

    client.connect(hostname, port=port, username=username, password=password)

def KitBotCommands(left, right):
    stdin, stdout, stderr = client.exec_command('python Robot-Controller-Support/Robot.py %d %d' % (left, right))

# -------------------Main Program--------------------------
sshInit()
while True:
    joysticks()
    roboSpeed()
    roboDirection()
    KitBotCommands(KitBotSpeed(motorL), -KitBotSpeed(motorR))