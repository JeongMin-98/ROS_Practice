# IMU 센서 활용

## 노드와 토픽

세방향의 축

Roll, 

Pitch 언덕 위로 올라가냐 내려가냐 

Yaw 왼쪽 오른쪽



### 패키지 생성

+ my_imu 패키지 만들기

  ```bash
  $ catkin_create_pkg my_imu std_msgs rospy
  $ mkdir launch
  $ vim launch/roll_pitch_yaw.launch
  $ vim src/roll_pitch_yaw.py
  ```

  

## 기울기 값 출력 프로그램 예제

IMU로부터 센싱값을 받아 ROLL, PITCH, YAW  값으로 변환하여 출력

```python
# -*- coding: utf-8 -*-
#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion

Imu_msg = None

def imu_callback(data):
    global Imu_msg
    Imu_msg = [data.orientation.x, data.orientation.y, 
               data.orientation.z,data.orientations.w]

rospy.init_node('Imu_print')
rospy.Subscriber('imu', Imu, imu_callback)

while not rospy.is_shutdown():
    if Imu_msg == None:
        continue
    (roll, pitch, yaw) = euler_from_quaternion(Imu_msg)
    
    print("Roll:%.4f, Pitch:%.4f ~")
    time.sleep(1.0)
    
```

## launch 파일 작성 

+ roll_pitch_yaw.launch

```xml
<launch>
	<node pkg="xycar_imu" type="9dof_imu_node.py" name="xycar_imu" output="screen">
    	<param name='rviz_mode' type='string' value='false'/>
    </node>
    <node pkg='my_imu' type='roll_pitch_yaw.py' name='Imu_Print' output='screen'/>
</launch>
```



# 실습

## 패키지 생성

### 소스코드작성

### 런치파일 작성





# IMU 센싱 데이터 시각화

## Plug-in 설치

+ rviz_imu_plugin.tgz 파일 복사

  ```bash
  $ mv rviz_imu_plugin.tgz ~/xycar_ws/src
  $ tar xzvf rviz_imu_plugin.tgz
  $ cm
  # cpp 파일이 컴파일되고 빌드된다. 별도의 설치작업을 할 필요는 없고 나중에 RVIZ를 실행시키면 자동으로 올라온다.
  
  ```

### 플러그인 추가

실행한 이후에 안 나올 경우 추가하면된다. 

+ RVIZ 우측 Displays 탭 하단에 ADD버튼을 클릭한다. 
+ RVIZ_imu_plugin 아래의 Imu 선택하고 OK버튼을 클릭

### Displays Tab 설정

여러가지 설정이 있다

+ Box Properties
  + 수신할 토픽 입력 란에는 /imu 토픽으로 선택
+ Axes Properties
  + 데이터를 시각화하기 위해 축을 Grid 위에 출력할 수 있음
  + Scale은 축의 크기
+ imu_3d.rviz 설정을 저장하기 위해서 창을 닫으면 된다. 

## 패키지 생성

+ rviz_imu 패키지 만들기

  ```bash
  $ catkin_create_pkg rviz_imu rospy tf geometry_msgs urdf rviz xacro
  ```

+ 런치 디렉토리 아래에 런치파일 만들기

  ```xml
  <launch>
  	<!-- rviz display -->
      <node name='rviz_visualizer' pkg='rviz' type='rviz'
            requried='true' args="-d $(find rviz_imu)
                                  /rviz/imu_3d.rviz"/>
      <node pkg='xycar_imu' type='9dof_imu_node.py' name='xycar_imu'
            output='screen'>
      	<param name='rviz_mode' type='string' value='false'/>
      </node>
  </launch>
  ```

## 실행

```bash
$roslaunch rviz_imu imu_3d.launch
```

## 결과 확인

뷰어를 설정한 이후에 다시 실행시키면 /Imu토픽이 시각화 그래프가 생긴다. 

빨간색 막대가 차량 전진 방향인지 아닌지 이런 것을 모두 확인

### rqt_graph



# RVIZ 기반 IMU 뷰어 제작

> 과제

## 목표

IMU 데이터로 뷰어의 박스를 움직이자

+ imu_generator.py

  + imu_data.txt(센서 하드웨어 대신 주어지는 데이터) 

    :arrow_right: 이 데이터는 실제로 IMU센서로부터 수집한 데이터

    + "roll : value, pitch : value, yaw : value"
    + value 값은 모두 라디안으로 기록

  + 데이터를 읽어서 /Imu 이름의 토픽을 발행한다. 

이 과정을 과제로 작성

### 토픽 구조

```python
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Quaternion orientation
  float64 x
  float64 y
  float64 z
  float64 w
float64[9] orientation_covariance
geometry_msgs/Vector3 angular_velocity
  float64 x
  float64 y
  float64 z
float64[9] angular_velocity_covariance
geometry_msgs/Vector3 linear_acceleration
  float64 x
  float64 y
  float64 z
float64[9] linear_acceleration_covariance
```

/imu 토픽의 구조는 위와 같다. 

위 구조 중 이번 과제에 사용될 부분은 아래와 같다. 

```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Quaternion orientation
  float64 x
  float64 y
  float64 z
  float64 w
```

+ roll, pitch, yaw를 x,y,z,w로 변환시키면된다. 

  + 사용 라이브러리

    ```python
    from tf.transformations import quaternion_from_euler
    ```

    

## 파일 구성

>  기존 rviz_imu 패키지에서 작업

+ Launch 파일 작성 :file_cabinet:imu_generator.launch
+ 파이썬 파일 작성 :file_cabinet:imu_generator.py
  + 텍스트 읽는 모듈을 이용
+ Rviz 파일 작성(복사):file_cabinet:imu_generator.gviz

### imu_data_maker.py

> 이 코드는 IMU가 보내는 토픽을 받아서 imu_data.txt파일을 만드는 파이썬 코드이다.

```python
#! /usr/bin/env python

import rospy, math, os
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion

degrees2rad = float(math.pi)/float(180.0)
rad2degrees = float(180.0)/float(math.pi)
name = " >> ./imu_data.txt"

def listener():
    rospy.init_node('imu_data_maker', anonymous=False)
    rospy.Subscriber('imu', Imu, call_back)
    
def call_back(data):
    global degrees2rad
    global rad2degrees
    
    euler = euler_from_quaternion((data~))
    euler = [euler[0], euler[1], euler[2]]
    
    save_str = 'roll : ' + str(euler[0]) + ~
    
    command = 'echo "'+save_str+'" >> ./imu_data.txt'
    print(command)
    os.system(command)
    
if __name__ == '__main__':
    listener()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
```

### imu_generator.py

```python
#! /usr/bin/env python

import rospy, math, os
from sensor_msgs.msg import Imu

from tf.transformaions import quaternion_from_euler

rospy.init_node(...)
rospy.Publisher(...)

# imu_data.txt read
# publihs
# end
```

### imu_generator.launch

```xml
<launch>
	<!-- rviz display -->
    <node name='rviz_visaulizer' pkg='rviz' type='rviz' required='true'
          args='-d $(find rviz_imu)/rviz/imu_generator.rviz'/>
    <node name='imu_generator' pkg='rviz_imu' type='imu_generator.py'/>

</launch>
```

## 결과

```bash
$ roslaunch rviz_imu imu_generator.launch
$ rostopic echo /imu
```

:heavy_check_mark:동영상 제출 : RVIZ 에서 3D 형상이 움직이는 것을 휴대폰으로 촬영해서 제출

:heavy_check_mark:파일 제출: Launch 파일과 imu_generator.py 파일 제출

:heavy_check_mark:문서 제출: imu_generator.py 파일 소스 코드를 상세히 설명하여 제출