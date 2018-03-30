import robot

robot.init()

'''
robot.drive_right()
robot.lift_up()
robot.gripper_to_open()
robot.lift_down()
robot.gripper_to_closed()
'''


# robot can only open/folding on the top!!!!

def swap_left_and_middle():
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    # red box is in gripper!
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    # red box is on the top of green box!
    robot.lift_down()
    robot.gripper_to_closed()
    #green box is in gripper!
    robot.drive_left()
    robot.drive_left()
    #greem box is on the right!
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    #red box is in the middle!


swap_left_and_middle()


def swap_middle_and_right():
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    #blue box is in gripper!
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    #blue box is in the middle!
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    #red box is in the right!


swap_middle_and_right()


def swap_middle_and_left():
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_closed()
    #green box is in the gripper!
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    #blue box is in the gripper!
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_folded()


swap_middle_and_left()
