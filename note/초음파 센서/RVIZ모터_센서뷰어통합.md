# 과제 

> RVIZ에서 자이카의 모터와 센서를 모두 통합
>
> RVIZ 가상공간에서 8자 주행을 하는 자이카에 라이다센서와 IMU센서의 뷰어를 통합해 보자
>
> 주변 장애물까지의 거리값을 Range로 표시하고 IMU 센싱값에 따라 차체가 기울어지는 것도 표현하자

## 과제 필요 요소

1. RVIZ 3D 모델링 되어있고 8자 주행하는 자동차 모델이 필요하다.
2. lidar센서 대신 lidar_topic.bag을 이용해서 /scan 토픽을 발행한 것을 받아 파이썬 파일을 통해서 scan1~4를 발행해서 RVIZ에서 시각화하는 부분이 필요
3. Imu_data_genrator를 통해서 IMU정보를 전달 



## 패키지 생성

```bash
$ catkin_create_pkg rviz_all
```

```
xycar_ws
	src
		rviz_all
			launch
				rviz_all.launch
			urdf
				rviz_all.urdf
			rviz
				rviz_all.rviz
			src
				odom_imu.py
```

### rviz_all.urdf

+ xycar_3d.urdf + lidar_urdf.urdf

```xml
<?xml version="1.0" ?>
<robot name="xycar" xmlns:xacro="http://www.ros.org/wiki/xacro">
 <link name="base_link"/>
  <link name="baseplate">
    <visual>
      <material name="acrylic"/>
      <origin rpy="0 0 0" xyz="0 0 0"/>
      <geometry>
        <box size="0.5 0.2 0.07"/>
      </geometry>
    </visual>
  </link>
  <joint name="base_link_to_baseplate" type="fixed">
    <parent link="base_link"/>
    <child link="baseplate"/>
    <origin rpy="0 0 0" xyz="0 0 0"/>
  </joint>
  <link name="front_mount">
    <visual>
      <material name="blue"/>
      <origin rpy="0 0.0 0" xyz="-0.105 0 0"/>
      <geometry>
        <box size="0.50 0.12 0.01"/>
      </geometry>
    </visual>
  </link>
  <joint name="baseplate_to_front_mount" type="fixed">
    <parent link="baseplate"/>
    <child link="front_mount"/>
    <origin rpy="0 0 0" xyz="0.105 0 -0.059"/>
  </joint>

  <link name="front_shaft">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.285" radius="0.018"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_mount_to_front_shaft" type="fixed">
    <parent link="front_mount"/>
    <child link="front_shaft"/>
    <origin rpy="0 0 0" xyz="0.105 0 -0.059"/>
  </joint>
  <link name="rear_shaft">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.285" radius="0.018"/>
      </geometry>
    </visual>
  </link>
  <joint name="rear_mount_to_rear_shaft" type="fixed">
    <parent link="front_mount"/>
    <child link="rear_shaft"/>
    <origin rpy="0 0 0" xyz="-0.305 0 -0.059"/>
  </joint>
  <link name="front_right_hinge">
    <visual>
      <material name="white"/>
      <origin rpy="0 0 0" xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.015"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_right_hinge_joint" type="revolute">
    <parent link="front_shaft"/>
    <child link="front_right_hinge"/>
    <origin rpy="0 0 0" xyz="0 -0.1425 0"/>
    <axis xyz="0 0 1"/>
    <limit effort="10" lower="-0.34" 
                       upper="0.34" velocity="100"/>
  </joint>
  <link name="front_left_hinge">
    <visual>
      <material name="white"/>
      <origin rpy="0 0 0" xyz="0 0 0"/>
      <geometry>
        <sphere radius="0.015"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_left_hinge_joint" type="revolute">
    <parent link="front_shaft"/>
    <child link="front_left_hinge"/>
    <origin rpy="0 0 0" xyz="0 0.1425 0"/>
    <axis xyz="0 0 1"/>
    <limit effort="10" lower="-0.34" upper="0.34" velocity="100"/>
  </joint>
  <link name="front_right_wheel">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.064" radius="0.07"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_right_wheel_joint" type="continuous">
    <parent link="front_right_hinge"/>
    <child link="front_right_wheel"/>
    <origin rpy="0 0 0" xyz="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit effort="10" velocity="100"/>
  </joint>
  <link name="front_left_wheel">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.064" radius="0.07"/>
      </geometry>
    </visual>
  </link>
  <joint name="front_left_wheel_joint" type="continuous">
    <parent link="front_left_hinge"/>
    <child link="front_left_wheel"/>
    <origin rpy="0 0 0" xyz="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit effort="10" velocity="100"/>
  </joint>
  <link name="rear_right_wheel">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.064" radius="0.07"/>
      </geometry>
    </visual>
  </link>
  <joint name="rear_right_wheel_joint" type="continuous">
    <parent link="rear_shaft"/>
    <child link="rear_right_wheel"/>
    <origin rpy="0 0 0" xyz="0 -0.14 0"/>
    <axis xyz="0 1 0"/>
    <limit effort="10" velocity="100"/>
  </joint>
  <link name="rear_left_wheel">
    <visual>
      <material name="black"/>
      <origin rpy="1.57 0 0" xyz="0 0 0"/>
      <geometry>
        <cylinder length="0.064" radius="0.07"/>
      </geometry>
    </visual>
  </link>
  <joint name="rear_left_wheel_joint" type="continuous">
    <parent link="rear_shaft"/>
    <child link="rear_left_wheel"/>
    <origin rpy="0 0 0" xyz="0 0.14 0"/>
    <axis xyz="0 1 0"/>
    <limit effort="10" velocity="100"/>
  </joint>
    
    <!-- range_front -->
    <link name='front'/>
    <joint name='baseplate_to_front' type='fixed'>
        <parent link='baseplate'/>
        <child link='front'/>
        <origin rpy='0 0 0' xyz='0.1 0 0'/>
    </joint>
    <!-- range_back -->    
    <link name='back'/>
    <joint name='baseplate_to_back' type='fixed'>
        <parent link='baseplate'/>
        <child link='back'/>
        <origin rpy='0 0 3.14' xyz='-0.1 0 0'/>
    </joint>
        
    <!-- range_left -->    
    <link name='left'/>
    <joint name='baseplate_to_left' type='fixed'>
        <parent link='baseplate'/>
        <child link='left'/>
        <origin rpy='0 0 1.57' xyz='0 0.1 0'/>
    </joint>
    <!-- range_right -->   
    <link name='right'/>
    <joint name='baseplate_to_right' type='fixed'>
        <parent link='baseplate'/>
        <child link='right'/>
        <origin rpy='0 0 -1.57' xyz='0 -0.1 0'/>
    </joint>
  <!-- color -->
  <material name="black">
    <color rgba="0.0 0.0 0.0 1.0"/>
  </material>
  <material name="blue">
    <color rgba="0.0 0.0 0.8 1.0"/>
  </material>
  <material name="green">
    <color rgba="0.0 0.8 0.0 1.0"/>
  </material>
  <material name="grey">
    <color rgba="0.2 0.2 0.2 1.0"/>
  </material>
  <material name="orange">
    <color rgba="1.0 0.423529411765 0.0392156862745 1.0"/>
  </material>
  <material name="brown">
    <color rgba="0.870588235294 0.811764705882 0.764705882353 1.0"/>
  </material>
  <material name="red">
    <color rgba="0.8 0.0 0.0 1.0"/>
  </material>
  <material name="white">
    <color rgba="1.0 1.0 1.0 1.0"/>
  </material>
  <material name="acrylic">
    <color rgba="1.0 1.0 1.0 0.4"/>
  </material>
</robot>

```



### rviz_all.rviz

+ rviz_odom.rviz 파일을 복사해서 사용한다. 그리고 라이다 센서의 시각화에 쓰이는 Range가 없으므로 설정에서 추가한다. 그리고 설정을 다 하면 무조건 종료할 때 저장한다. 

+ 이동 궤적 표시를 위해 Odometry를 추가한다.
+ Odometry 속성 설정
  + Topic :arrow_right: /odom
  + keep  :arrow_right:100
  + sharft length :arrow_right: 0.05
  + head length :arrow_right: 0.1

### odom_imu.py

+ odometry 데이터를 생성하는 rviz_odom.py를 수정해서 제작한다. 
+ Imu 토픽을 구독하여 획득한 쿼터니언 값을 odometry데이터에 넣어준다.

```python
#! /usr/bin/env python
import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from sensor_msgs.msg import JointState, Imu

# imu orientations quaternion 받는 객체 생성
Imudata = [0.0] * 4
# Angle 객체 생성
global Angle

def joint_callback(msg):
    """ joint_state callback 함수 """
    global Angle
    idx = msg.name.index('front_left_hinge_joint')
    Angle = msg.position[idx]

    
def imu_callback(msg):
    """ imu msg callback 함수 """
    global Imudata
    Imudata[0] = msg.orientation.x
    Imudata[1] = msg.orientation.y
    Imudata[2] = msg.orientation.z
    Imudata[3] = msg.orientation.w

rospy.Subscriber('imu', Imu, imu_callback)
rospy.Subscriber('joint_states', JointState, joint_callback)

rospy.init_node('odometry_publisher')
odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

current_speed = 0.4
wheel_base = 0.2

x_ = 0
y_ = 0
yaw_ = 0
Angle = 0
current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(30)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    # compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).to_sec()
    current_steering_angle = Angle
    current_angular_velocity = current_speed * math.tan(current_steering_angle) / wheel_base

    x_dot = current_speed * cos(yaw_)
    y_dot = current_speed * sin(yaw_)
    x_ += x_dot * dt
    y_ += y_dot * dt
    yaw_ += current_angular_velocity * dt

    # since all odometry is 6DOF we'll need a quaternion created from yaw
    # 기존에 있던 부분 수정
    # odom_quat = tf.transformations.quaternion_from_euler(0, 0, yaw_)
    odom_quat = Imudata
    # first, we'll publish the transform over tf
    odom_broadcaster.sendTransform(
        (x_, y_, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # set the position
    odom.pose.pose = Pose(Point(x_, y_, 0.), Quaternion(*odom_quat))

    # set the velocity
    odom.child_frame_id = "base_link"

    # publish the message
    odom_pub.publish(odom)

    last_time = current_time
    r.sleep()

```

### Launch 파일 만들기

```xml
<launch>
	<param name='robot_description' 
           textfile = '$(find rviz_all)/urdf/rviz_all.urdf' />
    <param name='use_gui' value='true'/>
    <node name='rviz_visualizer' pkg='rviz' type='rviz' required='true'
          args='-d $(find rviz_all)/rviz/rviz_all.rviz'/>
    <node name='robot_state_publisher' pkg='robot_state_publisher' 
          type='robot_state_publisher' />
    <!-- 노드 실행 자동차 8자 주행 -->
    <node name='driver' pkg='rviz_xycar' type='odom_8_driver.py' />    
    <node name='odometry' pkg='rviz_all' type='odom_imu.py' />
    <node name='motor' pkg='rviz_xycar' type='converter.py' />
    <!-- 라이다 토픽 발행 -->
    <node name='rosbag_play' pkg='rosbag' type='play' output='screen' required='true'
            args ='$(find rviz_lidar)/src/lidar_topic.bag' />
    <node name='lidar' pkg='rviz_lidar' type='lidar_urdf.py' output='screen'/>
    <!-- IMU 토픽 발행 -->
    <node name='imu' pkg='rviz_imu' type='imu_generator.py'/>
</launch>
```

