#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtlebotNavigation:
    def __init__(self):
        rospy.init_node('move_turtle_to_target', anonymous=True)

        self.vel_topic = rospy.get_param('~vel_topic')
        self.pose_topic = rospy.get_param('~pose_topic')

        rospy.loginfo("______________________Using velocity topic: %s and pose topic: %s", self.vel_topic, self.pose_topic)

        # Publisher to publish the command velocity
        self.velocity_publisher = rospy.Publisher(self.vel_topic, Twist, queue_size=10)

        # Subscriber to get the turtle's current pose
        self.pose_subscriber = rospy.Subscriber(self.pose_topic, Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    """
    This function updates the turtlebot's current pose
    """
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        rospy.loginfo("Publishing to topics: %s and %s", self.vel_topic, self.pose_topic)

    """
    Function to calculate euclidean distance between goal and target
    """
    def get_euclidean_distance(self, goal_pose):
        return math.sqrt((goal_pose.x - self.pose.x) ** 2 + (goal_pose.y - self.pose.y) ** 2)
    
    
    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.get_euclidean_distance(goal_pose)
    
    def steering_angle(self, goal_pose):
        return math.atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
    

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)
    
    def move_to_goal(self):
        target_x = rospy.get_param('~target_x', 10)
        target_y = rospy.get_param('~target_y', 10)
        goal_pose = Pose()
        goal_pose.x = target_x
        goal_pose.y = target_y
        distance_tolerance = 0.01

        vel_msg = Twist()

        while self.get_euclidean_distance(goal_pose) >= distance_tolerance and not rospy.is_shutdown():
            # Proportional controller
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.angular.z = self.angular_vel(goal_pose)

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        # Stop movement once goal reached
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.loginfo("Goal reached!")

if __name__ == '__main__':
    try:
        x = TurtlebotNavigation()
        x.move_to_goal()
    except rospy.ROSInterruptException:
        pass
    
