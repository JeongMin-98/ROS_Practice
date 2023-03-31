#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int32

def print_time(job_times, work_time, sleep_time, slot_time):
    print("job_times: "+str(job_times))
    print("===========================================")
    for work, sleep in zip(work_time, sleep_time):
        print('work_time: ' + str(round(work,4)))
        print('sleep_time: '+ str(round(sleep,4)))

    print("total_time: "+str(slot_time))

def job(pub, t):
    for i in range(0, t):
        i += 1
        pub.publish(i)

def talker():
    rospy.init_node('Sender')
    pub = rospy.Publisher('msg_to_student', Int32, latch=True, queue_size=0)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        work_times = []
        sleep_times = []
        t = int(input('Input time:'))
        rate.sleep()
        start = time.time()
        for i in range(5):
            work_start = time.time()
            job(pub, t)
            work_end=time.time()

            rate.sleep()
            sleep = time.time()

            work_time = work_end - work_start
            sleep_time = sleep - work_end 
            work_times.append(work_time)
            sleep_times.append(sleep_time)
        end = time.time()
        slot_time = end - start
        print_time(t, work_times, sleep_times, slot_time)

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
