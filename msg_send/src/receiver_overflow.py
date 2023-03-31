#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    k = 0
    for i in range(1, 10000000):
        k += 1
    print msg.data

rospy.init_node('Recevier')
sub = rospy.Subscriber('my_topic', Int32, callback, queue_size=1)

rospy.spin()
