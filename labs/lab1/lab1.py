"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020

Lab 1 - Driving in Shapes
"""

########################################################################################
# Imports
########################################################################################

import sys

sys.path.insert(1, "../../library")
import racecar_core
import racecar_utils as rc_utils

########################################################################################
# Global variables
########################################################################################

rc = racecar_core.create_racecar()

# Put any global variables here

########################################################################################
# Functions
########################################################################################


def start():
    """
    This function is run once every time the start button is pressed
    """
    # Begin at a full stop
    rc.drive.stop()

    # Print start message
    # TODO (main challenge): add a line explaining what the Y button does
    print(
        ">> Lab 1 - Driving in Shapes\n"
        "\n"
        "Controls:\n"
        "    Right trigger = accelerate forward\n"
        "    Left trigger = accelerate backward\n"
        "    Left joystick = turn front wheels\n"
        "    A button = drive in a circle\n"
        "    B button = drive in a square\n"
        "    X button = drive in a figure eight\n"
        "    Y button = manual drive\n"
    )


def update():
    """
    After start() is run, this function is run every frame until the back button
    is pressed
    """
    # TODO (warmup): Implement acceleration and steering
    rc.drive.set_speed_angle(0, 0)

    if rc.controller.was_pressed(rc.controller.Button.A):
        print("Driving in a circle...")
        # TODO (main challenge): Drive in a circle
    if rc.controller.was_pressed(rc.controller.Button.A):
        counter = 0
        isDriving= True
    if isDriving = True:
        counter += rc.get_delta_time()
    if counter < 360:
        rc.drive.set_speed_angle(1,1)
        rc.drive.set_speed_angle(1,0)
    else:
        rc.drive.stop()
        isDriving = False
        
    # TODO (main challenge): Drive in a square when the B button is pressed
global x
    if rc.controller.was_pressed(rc.controller.Button.B):
        counter = 0
        x = 1
        isDriving = True
    if isDriving = True:
        counter += rc.get_delta_time()
    while x<=8:
        if counter < x:
            rc.drive.set_speed_angle(1,0)
            x=x+1
        elif counter < x:
            rc.drive.set_speed_angle(1,90)
            x=x+1
    else:
        rc.drive.stop()
        isDriving = False
    # TODO (main challenge): Drive in a figure eight when the X button is pressed
if rc.controller.was_pressed(rc.controller.Button.X):
    counter = 0
    isDriving = True
if counter < 180:
    rc.drive.set_speed_angle(1,1)
    rc.drive.set_speed_angle(1,0)
elif counter < 185:
    rc.drive.set_speed_angle(5,45)
elif counter < 190:
    rc.drive.set_speed_angle(5,0)
elif counter < 370:
    rc.drive.set_speed_angle(1,-1)
    rc.drive.set_speed_angle(1,0)
elif counter < 375:
    rc.drive.set_speed_angle(5,45)
elif counter < 380:
    rc.drive.set_speed_angle(5,0)
else:
    rc.drive.stop()
    isDriving = False
    # TODO (main challenge): Drive in a shape of your choice when the Y button
    # is pressed
    if rc.controller.was_pressed(rc.controller.Button.Y):
        counter = 0
        isDriving = True
        print("Use the Joystick and Triggers to operate the Racecar")
    if rc.controller.was_pressed(rc.controller.Trigger.Left):
        rc.drive.set_speed_angle(1,0)
    if rc.controller.waspressed(rc.controller.Trigger.Right):
        rc.drive.set_speed_angle(-1,0)
    if rc.controller.waspressed(rc.controller.Joystick.Left):
        rc.drive.set_speed_angle(1,1)
        
    
        

########################################################################################
# DO NOT MODIFY: Register start and update and begin execution
########################################################################################

if __name__ == "__main__":
    rc.set_start_update(start, update)
    rc.go()
