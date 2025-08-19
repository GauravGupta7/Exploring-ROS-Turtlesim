#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest

def spawnAdditionTurtle(starting_x, starting_y):
    rospy.init_node("Spawn_Additional_Turtles", anonymous=True)

    """
    The '/spawn' service is used to spawn a new turtle in the turtlesim simulator.
    """
    rospy.wait_for_service('/spawn')

    # Create the service connection:
    spawner = rospy.ServiceProxy('/spawn', Spawn)

    # Call the service for spawning the turtlebot
    spawner(2,2,0,"turtle2")
    rospy.loginfo("Spawned turtle2 at (2, 2) with orientation 0 radians.")

if __name__ == '__main__':
    starting_x = rospy.get_param('~starting_x', 2.0)
    starting_y = rospy.get_param('~starting_y', 2.0)
    rospy.loginfo("Starting to spawn additional turtle at coordinates: (%f, %f)", starting_x, starting_y)
    try:
        spawnAdditionTurtle(starting_x, starting_y)
    except rospy.ROSInterruptException:
        pass
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)