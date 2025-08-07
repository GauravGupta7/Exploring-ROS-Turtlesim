# Exploring-ROS-Turtlesim
Repository that contains special tasks implemented using turtlesim


Beginner Tasks

    Move the turtle in a straight line:
    Write a ROS node that makes the turtle move straight ahead for 5 seconds, then stop.

    Draw a square:
    Make the turtle draw a square by moving straight and turning 90° at each corner. Use publishers to /turtle1/cmd_vel for control.

    Draw shapes (triangle, star, etc.):
    Program the turtle to draw polygons or more complex patterns.

    Keyboard teleoperation:
    Use the built-in turtle_teleop_key to manually control the turtle with your keyboard.

Intermediate Tasks

    Move to user-specified coordinate:
    Write a node or script that asks for X, Y coordinates and moves the turtle to that position using the /turtle1/teleport_absolute service.

    Change the turtle's pen (color, width, on/off):
    Use the /turtle1/set_pen service to change the pen color and width mid-drawing.

    Clear the screen:
    Call the /clear service to erase all previous drawings.

    Spawn additional turtles:
    Use the /spawn service to add a new turtle at a specific location and control it separately.

    Kill a turtle:
    Use the /kill service to remove a turtle from the simulation.

Advanced Tasks

    Follow a path:
    Publish a series of velocity commands or waypoints making the turtle trace a more complex path (like a spiral or sine wave).

    Control multiple turtles:
    Control two or more turtles to follow patterns or chase each other.

    Event-based movement:
    Subscribe to topics (e.g., a /goal_reached topic you create) and trigger turtle actions based on messages (ROS subscribers and publishers).

    Write an action client-server pair:
    Implement a simple action server that moves the turtle to a goal and reports feedback (great intro to ROS actions if you're ready for them).
