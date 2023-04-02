# 과제

## 과제 목표

RVIZ 가상공간에 있는 3D 자동차를 주행시켜 보자

+ 동작과정
  1. 8자 주행 프로그램이 모터 제어 메시지를 보낸다. 
  2. 변환프로그램이 받아서 변호나하여 /joint_states 토픽을 만들어 발행한다. 
  3. 2번에서 보낸 토픽을 odom 토픽으로 변환해서 발행시킨다. 

## 개념설명 

### 자이카 모터제어 토픽

+ /xycar_motor 토픽의 메시지 타입

### Joint_states 토픽

+ /joint_states 토픽의 메시지 타입
+ 바퀴의 각도와 움직임을 시각화 할 수 있다. 
+ sensor_msgs/JointState

### Odometry 토픽

+ /odom 토픽의 메시지 타입
+ nav_msgs/Odometry

## 파일 구성

기존의 rviz_xycar 패키지를 사용한다. 

+ launch 파일을 1개 작성
+ python 파일 2개 작성: odom_8_drive.py(시간 계산 추가)
+ RVIZ 파일을 자동 생성: rviz_odom.py

### rviz_odom.py

+ Converter 노드가 보내는 /joint_states 토픽을 받아서 바퀴의 방향과 회전 속도 정보를 획득
+ 해당 정보를 odometry 데이터로 만들어 /odom 토픽에 담아 발행한다. 

### 뷰어 설정 파일

3D 그림이 잘 표시되도록 설정하고 끝낼 때 설정내용을 잘 Save하면 된다. 그리고 저장 위치는 launch 파일에서 지정해서 할 수 있다. 

### rviz_odom.launch

```XML
<launch>
	<param name='robot_description' textfile="$(find rviz_xycar)/urdf/xycar_3d.urdf"/>
    <param name='use_gui' value='true'/>
    <! -- rviz display -->
    <node name='rviz_visualizer' pkg='rviz' type='rviz' required='true'
          args="-d $(find rviz_xycar)/rviz/rviz_odom.rviz"/>
    <node name='robot_state_publisher' pkg='robot_state_publisher'
          type='state_publihser'/>
    node odom_8_drive.py
    node rviz_odom.py
    node converter.py
</launch>
```

## 결과 확인

```bash
$ roslaunch rviz_xycar rviz_odom.launch
```

