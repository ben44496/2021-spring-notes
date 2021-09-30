#!/usr/bin/env python3

import rospy
import math
import numpy as np
import tf
from std_msgs.msg import Float32
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from nav_msgs.msg import Odometry

def latlong_to_position(lat, lon):
    # WGS84 ellipsoid constants:
    a = 6378137
    e = 8.1819190842622e-2
    # Urbana Altitude in meters
    altitude = 222
    # (prime vertical radius of curvature)
    N = a / math.sqrt(1 - e*e * math.sin(math.radians(lat))* math.sin(math.radians(lon)))
    x = (N+altitude) * math.cos(math.radians(lat)) * math.cos(math.radians(lon))
    y = (N+altitude) * math.cos(math.radians(lat)) * math.sin(math.radians(lon))
    #z = ((1-e*e) * N + altitude) * math.sin(math.radians(latitude))
    return x, y

def normalize_radians(angle):
    while angle > np.pi:
        angle -= 2*np.pi
    while angle < -np.pi:
        angle += 2*np.pi
    return angle


class listenerNode():

    def __init__(self):
        self.loop_hertz = 9.67
        
        # position
        self.lat = -1
        self.long = -1
        self.x = 0.0
        self.y = 0.0

        # heading
        self.angular_vel = np.full(3, -1.0, dtype=Float32) # droll, dpitch, dyaw
        self.yaw = 0
        self.roll = 0
        self.pitch = 0
        self.heading = Quaternion(0, 1, 0, 0)

        # encoders, meters per second
        self.blspeed = -1
        self.brspeed = -1
        self.flspeed = -1
        self.frspeed = -1
        self.linear_vel = -1

        # time
        self.deltat = 0
        self.time = 0

    def run(self):
        self.rate = rospy.Rate(self.loop_hertz)
        rospy.Subscriber("/latitude", Float32, self.latitude_callback)
        rospy.Subscriber("/longitude", Float32, self.longitude_callback)
        rospy.Subscriber("/Gyro_pitch", Float32, self.pitch_callback)
        rospy.Subscriber("/Gyro_roll", Float32, self.roll_callback)
        rospy.Subscriber("/Gyro_yaw", Float32, self.yaw_callback)
        rospy.Subscriber("/Blspeed", Float32, self.blspeed_callback)
        rospy.Subscriber("/Brspeed", Float32, self.brspeed_callback)
        rospy.Subscriber("/Flspeed", Float32, self.flspeed_callback)
        rospy.Subscriber("/Frspeed", Float32, self.frspeed_callback)
        rospy.Subscriber("/Timestamp", Float32, self.time_callback)

        self.pub_position_x = rospy.Publisher('/ans/position/x', Float32, queue_size=1)
        self.pub_position_y = rospy.Publisher('/ans/position/y', Float32, queue_size=1)
        self.pub_linear_vel = rospy.Publisher('/ans/linear_velocity', Float32, queue_size=1)
        self.pub_angular_vel_roll = rospy.Publisher('/ans/angular_velocity/droll', Float32, queue_size=1)
        self.pub_angular_vel_pitch = rospy.Publisher('/ans/angular_velocity/dpitch', Float32, queue_size=1)
        self.pub_angular_vel_yaw = rospy.Publisher('/ans/angular_velocity/dyaw', Float32, queue_size=1)
        # self.pub_heading = rospy.Publisher('/ans/heading', Quaternion, queue_size=1)

        pub_odom = rospy.Publisher('/ans/odom', Odometry, queue_size=1)
        self.br = tf.TransformBroadcaster()

        while not rospy.is_shutdown():
            self.update_position()
            self.linearvelocity()
            self.br.sendTransform((self.x, self.y, 0.0), self.q, rospy.Time.now(),"/base_link" , "/map")#this line is used to transform from local frame to global frame and it is necessary to plot the trajectory in RVIZ
            pub_odom.publish(self.odom)

            # self.publish()
            self.print_ans()
            self.rate.sleep()
    
    def publish(self):
        self.pub_position_x.publish(self.x)
        self.pub_position_y.publish(self.y)
        self.pub_linear_vel.publish(self.linear_vel)
        self.pub_angular_vel_roll.publish(self.angular_vel[0])
        self.pub_angular_vel_pitch.publish(self.angular_vel[1])
        self.pub_angular_vel_yaw.publish(self.angular_vel[2])
        # self.pub_heading.publish(self.heading)

    def print_ans(self):
        print("Pos:", self.x, self.y)
        print("Vel:", self.linear_vel, self.angular_vel)
        print("Heading:", self.heading)

    def linearvelocity(self):
        # self.q = quaternion_from_euler(self.roll, self.pitch, self.yaw)#function used to convert euler angles to quaternions
        self.q = quaternion_from_euler(0.0, 0.0, self.yaw)
        self.odom = Odometry()
        self.odom.pose.pose.position.x = self.x # self.linear_vel * np.cos(self.yaw)
        self.odom.pose.pose.position.y = self.y # self.linear_vel * np.sin(self.yaw)
        self.odom.pose.pose.position.z = 0.0
        self.odom.pose.pose.orientation.x = self.q[0]
        self.odom.pose.pose.orientation.y = self.q[1]
        self.odom.pose.pose.orientation.z = self.q[2]
        self.odom.pose.pose.orientation.w = self.q[3]
        self.odom.twist.twist.linear.x = self.linear_vel
        self.odom.twist.twist.angular.z = self.angular_vel[2]
        self.odom.header.stamp = rospy.Time.now()
        self.odom.header.frame_id = "/map"
        self.odom.child_frame_id = "/base_link"

    ### UPDATE IMPORTANT PARAMETERS ###
    def update_position(self):
        # self.position = latlong_to_position(self.lat, self.long)
        self.x += self.deltat * self.linear_vel * np.cos(self.yaw)
        self.y += self.deltat * self.linear_vel * np.sin(self.yaw)
    
    def update_linear_velocity(self):
        self.linear_vel = (self.blspeed + self.brspeed + self.flspeed + self.frspeed) / 4
    
    def update_roll(self):
        self.roll += self.angular_vel[0] * self.deltat
        self.roll = normalize_radians(self.roll)
        self.update_heading()
    
    def update_pitch(self):
        self.pitch += self.angular_vel[1] * self.deltat
        self.pitch = normalize_radians(self.pitch)
        self.update_heading()

    def update_yaw(self):
        self.yaw += self.angular_vel[2] * self.deltat
        self.yaw = normalize_radians(self.yaw)
        self.update_heading()
    
    def update_heading(self):
        # roll, pitch, yaw)
        # q = quaternion_from_euler(self.roll, self.pitch, self.yaw)
        q = quaternion_from_euler(0.0, 0.0, self.yaw)
        self.heading = q

    ### CALLBACK FUNCTIONS ###
    def latitude_callback(self, msg):
        self.lat = msg.data
        # self.update_position()
    
    def longitude_callback(self, msg):
        self.long = msg.data
        # self.update_position()
    
    def roll_callback(self, msg):
        self.angular_vel[0] = msg.data
        self.update_roll()
    
    def pitch_callback(self, msg):
        self.angular_vel[1] = msg.data
        self.update_pitch()
    
    def yaw_callback(self, msg):
        self.angular_vel[2] = msg.data
        self.update_yaw()
    
    def blspeed_callback(self, msg):
        self.blspeed = msg.data
        self.update_linear_velocity()
    
    def brspeed_callback(self, msg):
        self.brspeed = msg.data
        self.update_linear_velocity()
    
    def flspeed_callback(self, msg):
        self.flspeed = msg.data
        self.update_linear_velocity()
    
    def frspeed_callback(self, msg):
        self.frspeed = msg.data
        self.update_linear_velocity()

    def time_callback(self, msg):
        curr_time = msg.data/1000 # convert to seconds
        self.deltat = curr_time - self.time
        self.time = curr_time

if __name__ == '__main__':
    #Initialize the node and name it
    rospy.init_node('rospy_subscriber', anonymous = True)
    ne = listenerNode()
    ne.run()