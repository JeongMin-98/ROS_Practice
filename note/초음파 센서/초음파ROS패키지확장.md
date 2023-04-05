# 과제

> 초음파 센서 4개를 지원하는 ROS 패키지 제작하기
>
> 전력선은 동일한곳에 넣어도 된다
>
> 하지만 안전하게 하려면 다른 선을 이용해서 연결하면 좋다
>
> 그리고 입출력 신호를 연결하는 선은 모두 나눠서 연결하면 좋다.

각 센서의 Trig Echo는 (2,3), (4,5), (6, 7), (8, 9)로 연결한다.

Vcc, Gnd는 공용해서 사용해도 된다.

## ROS 패키지 

+ 초음파 센서 1개 + 아두이노 1개 + USB 케이블(PC와 연결)

## 디렉토리 구조

```
xycar_ws
	src
		ultrasonic
			launch
				# ultra.launch
				ultra4.launch
			src
				# ultrasonic_pub.py
				# ultrasonic_sub.py
				ultra4_pub.py
				ultra4_sub.py
				 
			
```

+ src아래 파일은 초음파 센서의 작동 유무를 확인하는 코드

## 노도, 토픽, 메시지 타입

+ 노드
  + ultrasonic4
+ 토픽
  + /ultra4
+ 메시지 타입
  + Int32MultiArray



## 펌웨어 코드 수정

기존 코드를 ultrasonic_4_fw.ino 파일로 복사하여 작성

초음파센서 개수 수정하고 1개 =>4개

4개의 초음파 센서의 거리 정보를 다음과 같은 문자열로 표시하도록 수정

```
300mm 121mm 186mm 67mm
```

USB 상에서 serial통신을 한다. PC의 터미널로 메시지를 발행하는 것으로 이해하면 된다.



## ultra4_pub.py

```python
#! /usr/bin/env python
# import module
# set port linked arduino
def read_sensor():
    # read serial data
    # extract digit data
    # return list 

if __name__ == '__main__':
    # rospy.init_node
    # publisher 
    while not rospy.is_shutdown():
        # load information from arduino
        # topic publish
        
   # close serial port
```

## ultra4_sub.py

```py
#! /usr/bin/env python

# import module

def callback(msg):
    # define callback
    
# ultra4_sub node
# Subscriber

# rospy.spin()
```

## Launch

```xml
<launch>
    <node ~ ultra4_pub.py />
    <node ~ ultra4_sub.py />
</launch>
```

