#!/usr/bin/env python3

import rospy
import rosbag
import yaml
import sys


def print_info(rosbag_file='../2020-08-31-00-01-17.bag'):
    bag = rosbag.Bag(rosbag_file)
    info_dict = yaml.load(bag._get_yaml_info())
    duration = info_dict['duration']
    start = info_dict['start']
    # print(info)
    topics_info = []
    for tuple in info_dict['topics']:
        topics_info.append((tuple['topic'], tuple['type']))

    pub_sub_dict = {
        "/Accelx" : "publisher",
        "/Accely" : "publisher",
        "/Accelz" : "publisher",
        "/Blspeed" : "publisher",
        "/Brspeed" : "publisher",
        "/Flspeed" : "publisher",
        "/Frspeed" : "publisher",
        "/Gyro_pitch" : "publisher",
        "/Gyro_roll" : "publisher",
        "/Gyro_yaw" : "publisher",
        "/Timestamp" : "publisher",
        "/clock" : "publisher",
        "/latitude" : "publisher",
        "/longitude" : "publisher",
        "/rosout" : "publisher",
        "/rosout_agg" : "publisher"
    }

    return topics_info, pub_sub_dict

    

# Technically there is a publisher (rosbag) and subscriber (rosout)
# and two publishers for rosout_agg (rosout and the rosbag) but
# I chose not to include them in the dictionary because they are
# just rosmaster and not technically part of the rosbag

if __name__ == "__main__":
    original_stdout = sys.stdout
    output = 'output.txt'
    with open(output, 'w') as f:
        sys.stdout = f
        topics_info, pub_sub_dict = print_info()
        topics_info.append(('/clock', 'rosgraph_msgs/Clock'))
        print("Number of topics:", len(topics_info), "\n")
        print("The following list has pairs of topic name and msg type")
        print(topics_info, "\n")
        print("The following dictionary provides whether they are being pubbed or subbed.\n"+
        "Note that it makes no sense for rostopics to be publishers or subscribers, as\n"+
        "that is more about nodes. Here, all topics in the rosbag are being published to\n"+
        "by the rosbag play itself. The only things that are different are technically rosout\n"+
        "because it is for rosmaster. The question only asks for the rosbag so I have only\n"+
        "included those topic informations here.")
        print(len(pub_sub_dict))
        print(pub_sub_dict)
        sys.stdout = original_stdout