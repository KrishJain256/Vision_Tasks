#!/usr/bin/env python3

import rospy
import subprocess

if __name__ == '__main__':
    # Initialize ROS node
    rospy.init_node('lab1_launch', anonymous=True)

    # Specify the package name and node names
    package_name = 'lab1_pkg'
    talker_node = 'talker.py'
    relay_node = 'relay.py'

    # Launch the parameter file
    parameter_process = subprocess.Popen(['rosrun', package_name, "parameter.sh"])

    # Launch the talker node
    talker_process = subprocess.Popen(['rosrun', package_name, talker_node])

    # Launch the relay node
    relay_process = subprocess.Popen(['rosrun', package_name, relay_node])

    # Log a message indicating successful launch
    rospy.loginfo("Nodes launched.")

    # Wait for nodes to complete execution
    parameter_process.wait()
    talker_process.wait()
    relay_process.wait()