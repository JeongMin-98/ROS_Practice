#! /usr/bin/env python
#-*- coding:utf-8 -*-
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np

class RosPublisher(object):
    def __init__(self, topic, msg_type=None):
        """
            name : 노드 이름
            topic : 토픽 이름
            msg_type : 메세지 타입
        """
        self.topic = topic
        self.msgtype = msg_type
        if self.msgtype is None:
            return 
        self.pub = rospy.Publisher(self.topic, self.msgtype)

class RosSubscriber(object):

    def __init__(self, name, topic, msg_type=None):
        """ 
            name : 노드 이름
            topic : 토픽 이름
            msg_type : 메세지 타입
        """
        self.name = name
        self.topic = topic
        self.msgtype = msg_type
        if self.msgtype is None:
            return 
        rospy.init_node(self.name, anonymous=True)
        self.sub = rospy.Subscriber(self.topic, self.msgtype, self.callback)

    def callback(self, msg):
        pass

class LaneDetection(RosSubscriber):

    def __init__(self, name, topic, msg_type, image=None):
        super(LaneDetection, self).__init__(name, topic, msg_type)
        self.image = image
        self.bridge = CvBridge()
        # rospy.init_node('subscriber')
        # rospy.Subscriber("/usb_cam/image_raw", Image, self.img_callback)
    def callback(self, msg):
        self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

    def process_image(self):
        
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 168], dtype = np.uint8)
        upper = np.array([172, 111, 255], dtype = np.uint8)
        
        mask = cv2.inRange(hsv, lower, upper)

        res = cv2.bitwise_and(self.image, self.image, mask=mask)

        img_hsv2bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

        img_gray = cv2.cvtColor(img_hsv2bgr, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(img_gray, 100, 200)

        return edges
    
    def img_callback(self, img_raw_msg):
            """
                /usb_cam/image_raw 토픽 받는 callback 함수
            """
            self.image = self.bridge.imgmsg_to_cv2(img_raw_msg, "bgr8")
    def is_none_image(self):
        if self.image is None:
            return True
        
    def show_origin_img(self):
        cv2.imshow('origin', self.image)
    def run(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            if self.is_none_image():
                continue
            edge_img = self.process_image()
            self.show_origin_img()
            cv2.imshow('edge_img', edge_img)
            cv2.waitKey(1)
            rate.sleep()

if __name__ == '__main__':

    lane_dectection = LaneDetection(name='sub', topic='/usb_cam/image_raw', msg_type=Image, image=None)
    lane_dectection.run()
                