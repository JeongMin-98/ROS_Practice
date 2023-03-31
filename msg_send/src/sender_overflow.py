#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32


pub = rospy.Publisher('my_topic', Int32, queue_size=1, latch=True)
rospy.init_node('Sender')
rate = rospy.Rate(1000)
count = 0

while not rospy.is_shutdown():
   pub.publish(count)
   count += 1
   rate.sleep()
