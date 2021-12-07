import visualization_msgs.msg as viz_msg
from rospy.rostime import Duration

class Marker(viz_msg.Marker):

    def __init__(self, frame_id="laser"):
        super().__init__()
        self.type = viz_msg.Marker.LINE_LIST
        self.action = Marker.ADD
        self.header.frame_id = frame_id
        self.ns = "line"
        self.scale.x = 0.03
        self.color.r = 1.0
        self.color.a = 1.0
        self.lifetime = Duration(secs=0.0)
        self.frame_locked = False

