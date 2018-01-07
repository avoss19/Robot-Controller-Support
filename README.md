# Robot-Controller-Support

Welcome to Robot Controller Support! This repo was created for the BSM robot.

## Supported Controllers/Tested Controllers

Full Support:
- PS4 Controller

Partial Support:
- Xbox One Controller - changing controller scheme on the fly doesn't work
- Xbox 360 Controller - changing controller scheme on the fly doesn't work

Not Supported:

Not Tested:

## Setup

- Make sure you have the required packages
- clone this repo to the robot
- clone on computer then run one of the python programs, like "Wireless KitBot.py"

## Required Packages

- pip </br>
$ curl -O http://python-distribute.org/distribute_setup.py </br>
$ python distribute_setup.py </br>
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py </br>
$ python get-pip.py
- pygame </br>
$ pip install pygame
- paramiko </br>
$ pip install paramiko

## Mapping Options

- can choose to control speed w/ right and left triggers or use right joystick
- recommend using right joystick due to trigger dead zones
- can changing mapping during use by pressing right bumper (does not work 100% of the time, may need to hold it for a sec or press multiple times)

## Communication with robot

- Uses laptop and use ssh to connect to robot

## Issues

- Xbox One & Xbox 360 Controller can't swap controller scheme on the fly

## Troubleshooting

You will receive this error if the program does not recognize your controller

Traceback (most recent call last): </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 116, in <module> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    roboSpeed() </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 72, in roboSpeed </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft: </br>
NameError: global name 'yAxisRight' is not defined </br>
