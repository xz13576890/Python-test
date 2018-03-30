import robot
import unstack

robot.init(pos = 0, boxes = [[], [], [], [], ["red", "green", "blue"]])

def grasp_blocks_above():
    robot.drive_left
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()



grasp_blocks_above()