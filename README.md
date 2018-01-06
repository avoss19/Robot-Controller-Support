# Robot-Controller-Support

- Only tested w/ ps4 controller
- use PS4 controller due to native support w/out drivers

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

## Communication with robot

- Uses laptop and use ssh to connect to robot

## Troubleshooting

You will receive this error if the program does not recognize your controller

Traceback (most recent call last): </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 116, in <module> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    roboSpeed() </br>
&nbsp;&nbsp;&nbsp;  File "Controller.py", line 72, in roboSpeed </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    if -yDeadZoneRight < yAxisRight < yDeadZoneLeft: </br>
NameError: global name 'yAxisRight' is not defined </br>
