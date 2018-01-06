# -----------------File on Robot--------------------
# Reason for this file: Less down on latency

# Example:
import argv
import robotonomy.RoboPiLib as RPL
import setup

leftMotor, rightMotor = argv

RPL.servoWrite(0,leftMotor)
RPL.servoWrite(1,rightMotor)
