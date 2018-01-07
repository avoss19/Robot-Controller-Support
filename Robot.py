# -----------------File on Robot--------------------
# Reason for this file: Less latency

# Example:
from sys import argv
import robotonomy.RoboPiLib as RPL
import setup

pyProgam, leftMotor, rightMotor = argv

RPL.servoWrite(0,leftMotor)
RPL.servoWrite(1,rightMotor)
