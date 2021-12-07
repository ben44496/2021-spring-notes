import rospy
import numpy as np
import tf
from sensor_msgs.msg import *
from nav_msgs.msg import *
import linear_regression as LR
from my_datatypes import Marker
from std_msgs.msg import *
from geometry_msgs.msg import Point

# Make sure to set Fixed Frame as odom in rviz

class listenerNode():
    def __init__(self):
        self.loop_hertz = 10
        self.laser_scan = None
        self.odometry = None

    def run(self):
        self.rate = rospy.Rate(self.loop_hertz)
        robot = "/terrasentia"
        rospy.Subscriber(robot + "/scan", LaserScan, self.laserscan_callback)
        rospy.Subscriber(robot + "/ekf", Odometry, self.odometry_callback)

        self.pub_lines = rospy.Publisher("/ans/lines", Marker, queue_size=1)
        # self.pub_lines = rospy.Publisher("/ans/lines", Float32, queue_size=1)

        self.t = 0
        while not rospy.is_shutdown():
            if not self.laser_scan is None:
                self.publish()
                self.t += 1
            self.rate.sleep()

    def publish(self):
        ans = self.fit_lines()
        self.pub_lines.publish(ans)

    def fit_lines(self):
        # self.pub_lines.publish(...)
        # Marker.type = 5 # Line List (0-1, 2-3, 4-5)

        point_cloud = LR.preprocess(self.laser_scan) # (1081, 2)
        marker = Marker()
        marker.ns += str(self.t)
        marker.points = LR.incremental_model(point_cloud, threshold=0.01, min_points=4, dead_radius=0.5)

        return marker

    def laserscan_callback(self, msg):
        self.laser_scan = msg
    
    def odometry_callback(self, msg):
        self.odometry = msg
    
if __name__ == "__main__":
    rospy.init_node("rospy_subscriber", anonymous=True)
    ne = listenerNode()
    ne.run()