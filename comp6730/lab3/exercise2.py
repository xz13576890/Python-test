#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:59:23 2018

@author: u6469050
"""
import robot

def move_to_next_stack():
    '''move robot two steps right'''
    robot.drive_right()
    robot.drive_right()

def pickup_next():
    '''Release the box in gripper (if any) and pick up the one below.
    Assumption: robot is in front of a box/stack; lift is at level 1.'''
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

def make_tower(n):
    robot.init(width = 2*n-1, boxes = "flat") 
    robot.drive_right()
    robot.lift_up()
    i = 0
    while i < n-1:
        pickup_next()
        move_to_next_stack()
        i = i+1
    robot.gripper_to_folded()
    robot.lift_down()
    return "Tower complete!"

def find(colour):
    robot.init(height=5, boxes=[["black", "blue", "white", "red"]])
    j = 1
    while robot.sense_color() != "":
        if robot.sense_color == colour:
            return True # Why this doesn't work?
        robot.lift_up()
        j = j+1
    return False
    

def count_boxes():
    if robot.sense_color() == "":
        return 0
    else:
        robot.lift_up()
        num_above = count_boxes()
        robot.lift_down()
        return 1 + num_above











