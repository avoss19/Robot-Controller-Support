import argv
import robotonomy.RoboPiLib as RPL
import setup

leftMotor, rightMotor = argv

RPL.servoWrite(0,leftMotor)
RPL.servoWrite(1,rightMotor)
