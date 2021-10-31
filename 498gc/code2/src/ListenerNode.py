#!/usr/bin/env python3

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from nav_msgs.msg import *

class listerner_node():

    def __init__(self):
        self.loop_hertz = 10


    def run(self):
        self.rate = rospy.Rate(self.loop_hertz)

        while not rospy.is_shutdown():
            # Do something

            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node('rospy_subscriber', anonymous=True)
    ne = listerner_node()
    ne.run()