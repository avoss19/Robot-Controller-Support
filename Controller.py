import pygame # controller
import sys, paramiko # ssh

# SSH login
hostname = "192.168.21.113" # ip address
password = "Engineering!1"

username = "student"
port = 22

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

def SSH(command):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read(),

# -------------------Main Program--------------------------
SSH("python")
SSH("import setup")
SSH("import RoboPiLib as RPL")
while True:
    joysticks()
    roboSpeed()
    roboDirection()
    SSH("RPL.servoWrite(0,%d)" % motorL)
    SSH("RPL.servoWrite(1,%d)" % motorR)
