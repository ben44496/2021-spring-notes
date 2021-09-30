#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:06:12 2021

@author: andres
"""

import rospy
from std_msgs.msg import Int32

class listenerNode():
   
    
    number = 0.0
    A=0.0
    def __init__(self):
        self.loop_hertz = 10.0
    
    def run(self):
        self.rate = rospy.Rate(self.loop_hertz)#this line is used to declare the time loop
        rospy.Subscriber("publisher_node_example", Int32, self.callback)
        while not rospy.is_shutdown():
            print("The number is: ",listenerNode.number)
            self.rate.sleep()

   
    def callback(self,msg):
        listenerNode.number = msg.data
        rospy.loginfo("number %s", self.number)
        
if __name__ == '__main__':
    #Initialize the node and name it
    rospy.init_node('rospy_subscriber', anonymous = True)
    ne = listenerNode()
    ne.run()