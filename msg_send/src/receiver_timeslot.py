#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32 

def callback(msg):
    print msg.data

rospy.init_node('Receiver')

sub = rospy.Subscriber('msg_to_student', Int32, callback)

rospy.spin()
