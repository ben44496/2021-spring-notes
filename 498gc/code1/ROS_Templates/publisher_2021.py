#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:00:44 2021

@author: andres
"""


import rospy
from std_msgs.msg import Int32

class PublisherNode():
    
    def __init__(self):
        self.loop_hertz = 10.0
        
    def run(self):
        self.rate = rospy.Rate(self.loop_hertz)#this line is used to declare the time loop
        pub = rospy.Publisher('publisher_node_example',Int32,queue_size=1)
        A = 0
        while not rospy.is_shutdown():
            pub.publish(A)
            A+=1#this is equal to A = A+1
            print(A)
            self.rate.sleep()

if __name__ == '__main__':
    #Initialize the node and name it
    rospy.init_node('rospy_publisher', anonymous = True)
    ne = PublisherNode()
    ne.run()