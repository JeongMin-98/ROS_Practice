#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy, rospkg
import numpy as np
import cv2, random, math
from cv_bridge import CvBridge
# from xycar_msgs.msg import xycar_motor
from xycar_motor.msg import xycar_motor
from sensor_msgs.msg import Image
import ros_tool
import sys
import os
import signal

# signal handler
def signal_handler(sig, frame):
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def img_callback(img_raw_msg):
        """
            /usb_cam/image_raw 토픽 받는 callback 함수, 사용 안함
        """
        image = CvBridge.imgmsg_to_cv2(img_raw_msg, "bgr8")

class GetMotorMsgFromHoughDrive(ros_tool.RosSubscriber):

    def __init__(self, name, topic, msg_type, image=None):
        """
            Subscriber를 상속받아 전역변수로 선언하지 않아도 변수를 관리 할 수 있도록 함
        """
        # 상속
        super(GetMotorMsgFromHoughDrive, self).__init__(name, topic, msg_type)
        # 기본 init value
        self.image = image
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('/xycar_motor', xycar_motor, queue_size=1)
        self.Width = 640
        self.Height = 480
        self.Offset = 360
        self.Gap = 40
        self.low_slope_threshold = 0
        self.high_slope_threshold = 2
    # publish xycar_motor msg
    def drive(self, Angle, Speed): 
        global pub

        msg = xycar_motor()
        msg.angle = Angle
        msg.speed = Speed
        
        self.pub.publish(msg)

    def callback(self, msg):
        # callback override (상속받은 callback 함수 오버라이딩)
        self.image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

    # draw lines
    def draw_lines(self, img, lines):
        for line in lines:
            x1, y1, x2, y2 = line[0]
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # img = cv2.line(img, (x1, y1+self.Offset), (x2, y2+self.Offset), color, 2)
            img = cv2.line(img, (x1, y1+self.Offset), (x2, y2+self.Offset), color, 2)
        return img

    # draw rectangle
    def draw_rectangle(self, img, lpos, rpos, offset=0):
        center = (lpos + rpos) / 2

        cv2.rectangle(img, (lpos - 5, 15 + offset),
                        (lpos + 5, 25 + offset),
                        (0, 255, 0), 2)
        cv2.rectangle(img, (rpos - 5, 15 + offset),
                        (rpos + 5, 25 + offset),
                        (0, 255, 0), 2)
        cv2.rectangle(img, (center-5, 15 + offset),
                        (center+5, 25 + offset),
                        (0, 255, 0), 2)    
        cv2.rectangle(img, (315, 15 + offset),
                        (325, 25 + offset),
                        (0, 0, 255), 2)
        return img

    # left lines, right lines
    def divide_left_right(self, lines):

        low_slope_threshold = self.low_slope_threshold
        high_slope_threshold = self.high_slope_threshold

        # calculate slope & filtering with threshold
        slopes = []
        new_lines = []

        for line in lines:
            x1, y1, x2, y2 = line[0]

            if x2 - x1 == 0:
                slope = 0
            else:
                slope = float(y2-y1) / float(x2-x1)
            
            if abs(slope) > low_slope_threshold and abs(slope) < high_slope_threshold:
                slopes.append(slope)
                new_lines.append(line[0])

        # divide lines left to right
        left_lines = []
        right_lines = []

        for j in range(len(slopes)):
            Line = new_lines[j]
            slope = slopes[j]

            x1, y1, x2, y2 = Line

            if (slope < 0) and (x2 < self.Width/2 - 90):
                left_lines.append([Line.tolist()])
            elif (slope > 0) and (x1 > self.Width/2 + 90):
                right_lines.append([Line.tolist()])

        return left_lines, right_lines

    # get average m, b of lines
    def get_line_params(self, lines):
        # sum of x, y, m
        x_sum = 0.0
        y_sum = 0.0
        m_sum = 0.0

        size = len(lines)
        if size == 0:
            return 0, 0

        for line in lines:
            x1, y1, x2, y2 = line[0]

            x_sum += x1 + x2
            y_sum += y1 + y2
            m_sum += float(y2 - y1) / float(x2 - x1)

        x_avg = x_sum / (size * 2)
        y_avg = y_sum / (size * 2)
        m = m_sum / size
        b = y_avg - m * x_avg
        if m < 0:
            print('left lane avg slope' + str(abs(m)))
        else:
            print('right lane avg slope' + str(abs(m)))
        return m, b

    # get lpos, rpos
    def get_line_pos(self, img, lines, left=False, right=False):
        
        m, b = self.get_line_params(lines)

        if m == 0 and b == 0:
            if left:
                pos = 0
            if right:
                pos = self.Width
        else:
            y = self.Gap / 2
            pos = (y - b) / m

            b += self.Offset
            x1 = (self.Height - b) / float(m)
            x2 = ((self.Height/2) - b) / float(m)

            cv2.line(img, (int(x1), self.Height), (int(x2), (self.Height/2)), (255, 0,0), 3)

        return img, int(pos)

    # show image and return lpos, rpos
    def process_image(self, frame):
        
        # gray
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # Detect black lane(White lane) => hsv 채널 값 변경해서 검정색도 추출 가능
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 168], dtype = np.uint8)
        upper = np.array([172, 111, 255], dtype = np.uint8)
        
        mask = cv2.inRange(hsv, lower, upper)

        res = cv2.bitwise_and(self.image, self.image, mask=mask)

        img_hsv2bgr = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)

        img_gray = cv2.cvtColor(img_hsv2bgr, cv2.COLOR_BGR2GRAY)

        # blur
        kernel_size = 5
        blur_gray = cv2.GaussianBlur(img_gray,(kernel_size, kernel_size), 0)
        # blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

        # canny edge
        low_threshold = 60
        high_threshold = 70
        edge_img = cv2.Canny(np.uint8(blur_gray), low_threshold, high_threshold)
        cv2.imshow('canny', edge_img)
        
        # HoughLinesP
        roi = edge_img[self.Offset :self.Offset+20, self.Gap : self.Width - self.Gap]
        cv2.imshow('roi', roi)
        all_lines = cv2.HoughLinesP(roi,1,math.pi/180,30,30,10)

        # divide left, right lines
        if all_lines is None:
            return 0, 640
        left_lines, right_lines = self.divide_left_right(all_lines)

        # get center of lines
        frame, lpos = self.get_line_pos(frame, left_lines, left=True)
        frame, rpos = self.get_line_pos(frame, right_lines, right=True)
        # draw lines
        frame = self.draw_lines(frame, left_lines)
        frame = self.draw_lines(frame, right_lines)
        frame = cv2.line(frame, (230, 235), (410, 235), (255,255,255), 2)
                                    
        # draw rectangle
        frame = self.draw_rectangle(frame, lpos, rpos, offset=self.Offset)
        #roi2 = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
        #roi2 = draw_rectangle(roi2, lpos, rpos)

        # show image
        cv2.imshow('calibration(FINAL)', frame)

        return lpos, rpos
    
    def is_none_image(self):
        if self.image is None:
            return True
        
    def start(self):
        
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            if self.is_none_image():
                continue

            lpos, rpos = self.process_image(self.image)

            center = (lpos + rpos) / 2
            angle = -(self.Width/2 - center)
            # 주행은 생략
            # 위에 클래스 init함수에 pub 추가해서 start함수에서 토픽 발행하면 될듯
            self.drive(angle, 8)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            rate.sleep()
       
if __name__ == '__main__':
    
    hough_point = GetMotorMsgFromHoughDrive(name='hough_drive', topic='/usb_cam/image_raw', msg_type=Image, image=None)
    hough_point.start()
