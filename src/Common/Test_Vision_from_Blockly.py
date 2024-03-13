# !/usr/bin/env python3

from pyniryo import *
import sys
# import rospy
import time
import math
import keyboard
import pynput

n = NiryoRobot("192.168.0.21")     # --- connexion   ----
n.calibrate_auto() 

for count in range(7):
  # Move to an observation position:
  n.move_pose(*[0.16, 0, 0.35, 0, 1.57, 0])
  # Try to do a vision pick:
  if n.vision_pick('wp_square', 0/1000.0, ObjectShape.ANY, ObjectColor.RED)[0]:
    # If an object has been taken, do:
    n.place_from_pose(*[0.15, -0.1, 0.25, 0.2, 1.57, 0])
 
