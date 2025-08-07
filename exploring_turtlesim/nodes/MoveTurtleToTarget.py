#!/usr/bin/env python

"""
This script is used to publish commands to the /turtle1/cmd_vel topic
to move the turtle in a square boundary.
"""

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

# Global variable to store the current position
current_position = Pose()

# Publisher for turtle movement
movePublisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

def current_pose_callback(msg):
    global current_position
    # Update the current position with the incoming message
    current_position = msg

def subscribePosition():
    rospy.Subscriber("/turtle1/pose", Pose, current_pose_callback)

def turtleConsole(target, direction):
    moveCommand = Twist()
    
    # Calculate time for movement based on difference (not accurate, better to use distances)
    distance = target - current_position.x if direction == "x" else target - current_position.y
    timeInSeconds = abs(distance) / 2.0  # Example simple time estimate

    if direction == "x":
        moveCommand.linear.x = 2.0 if distance > 0 else -2.0
    elif direction == "y":
        moveCommand.linear.y = 2.0 if distance > 0 else -2.0

    # Publish the movement command
    movePublisher.publish(moveCommand)

def navigationBeginsHere():
    # Define the target position
    target = Pose()
    target.x = 10
    target.y = 10

    # Start subscribing to the pose
    subscribePosition()

    # Wait until we have the initial pose data
    rospy.sleep(1)

    # Move in the x direction if needed
    if current_position.x < target.x:
        while current_position.x < target.x:
            turtleConsole(target.x, "x")
            rospy.sleep(0.1)  # small sleep to allow time for movement and feedback

    # Move in the y direction if needed
    if current_position.y < target.y:
        while current_position.y < target.y:
            turtleConsole(target.y, "y")
            rospy.sleep(0.1)

    rospy.loginfo("Target reached at position (%.2f, %.2f)", current_position.x, current_position.y)

if __name__ == "__main__":
    rospy.init_node("move_turtle_in_square")
    navigationBeginsHere()
