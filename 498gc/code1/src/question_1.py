#!/usr/bin/env python3

import rospy
import rosbag
import yaml

# bag = rosbag.Bag('../2020-08-31-00-01-17.bag')
# topics = []
# for topic, msg, t in bag.read_messages():
#     if not topic in topics:
#         topics.append(topic)
# print(topics)
# print(len(topics))
# bag.close()

bag = rosbag.Bag('../2020-08-31-00-01-17.bag')
info_dict = yaml.load(bag._get_yaml_info())
duration = info_dict['duration']
start = info_dict['start']
# print(info)
topics_info = []
for tuple in info_dict['topics']:
    topics_info.append((tuple['topic'], tuple['type']))
print(topics_info)
print(len(topics_info))