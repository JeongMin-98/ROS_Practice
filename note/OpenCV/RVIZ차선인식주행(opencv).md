# 과제

> OpenCV 와 rosbag을 이용한 차선인식 주행이 목표

+ rosbag을 통해서 생긴 /usb_cam/image_raw 토픽을 line_follow 노드가 구독한다. 
+ /xycar_motor 토픽발행해 가상공간에서 모델링된 RVIZ 차량을 주행시킨다.

**차선 인식 운전**

+ 차선 추종 주행
  + 좌우 차선을 찾아내어 차선을 벗어나지 않게 주행하면 된다.

> 차선의 위치를 찾기 위해서 적절한 영역 찾기

## OpenCV 기반의 영상 처리

+ image Read
+ GrayScale
+ Gaussian Blur
+ HSV - Binary
+ ROI

+ 차선 위치를 파악
+ 핸들 꺾기

## 기존 패키지에서 작업

```bash
$ catkin_create_pkg line_drive rospy tf geometry_msgs rviz xacro
```

```
src
	line_drive
		src
			line_follow.py
			cam_topic.bag
        launch
        	line_follow.launch
        	line_follow.rosbag.launch
```

## ROS 노드와 토픽 구성도

+ rqt_graph

## cam_topic.bag 제작

:heavy_check_mark:필요한 카메라 토픽만 꺼내서 **cam_topic.bag** 제작하기

```bash
$ rosbag play full_topic.bag
$ rosbag record -O cam_topic /usb_cam/image_raw/
$ rosbag info cam_topic.bag
```

### 동영상 파일 제작

>  처음엔 토픽 대신에 동영상 파일을 사용하는 게 편하다.

```bash
$ roscore
$ rosrun image_view video_recorder image:='/usb_cam/image_raw' _filename:='track2.avi' _fps=30
$ rosbag play cam_topic.bag
```

### line_follow.py

+ 작업 흐름도
  + /usb_cam/image_raw 토픽을 구독
  + 토픽 데이터를 OpenCV 이미지 데이터로 변환
  + 영상처리
  + 차선 위치를 찾고 화면 중앙에서 어느쪽으로 치우쳤는지 파악
  + 핸들을 얼마나 꺾을지 결정
  + 모터 제어를 위한 토픽 발행
  + speed 고정

```python
#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 모듈 import
import rospy
import time
import cv2
import numpy as np
# from xycar_motor.msg import motor_msg
from xycar_motor.msg import xycar_motor
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from line_find import get_binary_of_color
from Queue import Queue

# subscriber 준비
class GetImage2Msg():
    def __init__(self):
        """
            is_comp : 압축 유무 0, 1
            0 => raw
            1 => compressed
        """
        self.pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)
        self.cv_image = None
        self.bridge = CvBridge()
        rospy.init_node('line_follow', anonymous=True)
        rospy.Subscriber('/usb_cam/image_raw', Image, self.callback, queue_size=1)
        
    def callback(self, image_msg):
        """
            /usb_cam/image_raw 토픽을 구독하고 
            토픽을 opencv 이미지 데이터로 변환
        """
        self.cv_image = self.bridge.imgmsg_to_cv2(image_msg, 'bgr8')

    def set_motor_msg(self):
        if self.cv_image is None:
            return 
        scan_width = 200
        scan_height = 20
        lmid = scan_width
        rmid = 640 - 200
        area_width = 20
        area_height = 10
        row_begin = (scan_height - area_height) // 2
        row_end = row_begin + area_height
        zero_pixel_threshold = 0.8 * area_width * area_height
        lower = [0, 0, 60]
        upper = [131, 255, 255]
        view = self.cv_image.copy()
        roi = self.cv_image[430:450, :]
        masked_roi = get_binary_of_color(roi, lower, upper)

        left, right = -1, -1

        for l in range(20, 200):
            area = masked_roi[row_begin: row_end, l - area_width : l]
            if cv2.countNonZero(area) > zero_pixel_threshold:
                left = l
                break
        
        for r in range(640-area_width, rmid, -1):
            area = masked_roi[row_begin: row_end, r: r+area_width]
            if cv2.countNonZero(area) > zero_pixel_threshold:
                right = r
                break
        if left != -1:
            lsquare = cv2.rectangle(view, (left, 430), 
                    (left - area_width, 450), (0,255,0), 3)

        else:
            print('lost left line')
        
        if right != -1:
            rsquare = cv2.rectangle(view, (right, 430), 
                    (right + area_width, 450), (0,255,0), 3)
        else:
            print("lost right line")


        speed = 20
        # 차선의 중앙
        mid = (left + right) / 2
        shift = mid - 320
        angle = shift/3
        if angle < -50:
            angle = -50
        elif angle > 50:
            angle = 50
        
        motor_msg = xycar_motor()
        motor_msg.speed = speed
        motor_msg.angle = angle

        self.pub.publish(motor_msg)

    def run(self):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            self.set_motor_msg()
            rate.sleep()
        
if __name__ == '__main__':
    
    node = GetImage2Msg()
    node.run()
```

### Launch 파일 작성

```xml
<launch>
    <param name="robot_description" textfile="$(find rviz_xycar)/urdf/xycar_3d.urdf"/>
    <param name="use_gui" value="true"/>

    <!-- rviz display -->
    <node name="rviz_visualizer" pkg="rviz" type="rviz" required="true" 
                args="-d $(find rviz_xycar)/rviz/rviz_odom.rviz"/>

    <node name="robot_state_publisher" pkg="robot_state_publisher" 
                type="robot_state_publisher"/>

    <node name="converter" pkg="rviz_xycar" type="converter.py" />
    <node name='odometry' pkg='rviz_xycar' type='rviz_odom.py'/>
    <node name="line_follow" pkg="line_drive" type="line_follow.py"/>
    <node name='player' pkg='rosbag' type='play' output='screen' 
                args='--clock $(find line_drive)/src/cam_topic.bag'/>
</launch>
```

+ 다른 터미널에서 별도로 bag을 실행한다. (영상으로 바꾼 경우는 제외)

## 결과

### rqt_graph

