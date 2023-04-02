# Odometry

+ Odometer (오도미터)
  + 차량이나 로봇이 주행하며 이동한 거리를 측정하는 기기
  + 바퀴의 회전수로 이동 거리를 계산
  + 원의 둘레의 길이 (원주)

+ Odometry (오도메트리)
  + 오도미터 등의 기기의 측정값으로 움직이는 사물의 위치를 측정하는 방법



## 자동차 핸들과 앞 바퀴

+ 앞 바퀴 2개
  + 회전 시 꺾이는 각도가 다르다
  + 안쪽과 바깥쪽 회전 원의 중심이 일치해야한다.  (동심원이 같아야한다.)
  + 뒤에 바퀴의 축을 기준으로 직선으로 긋고 앞바퀴 두개의 직각으로 한 선을 만나도록 해야지 그자리를 돌 수 있다. 
  + 정밀하게 맞춰야한다. 

#### Ackermann Steering

+ 간단한 기계식 구조를 가진다. 
+ 회전시 꺾이는 각도가 다르도록
+ 안쪽과 바깥쪽 회전 원의 중심이 일치한다. 

## 자동차의 위치 정보

+  현재 위치 : (x, y) 좌표 + 세타
+ 이동속도: 선속도 + 각속도
+ 조향각 델타

# 토픽

## odometry 토픽

+ /odom

+ 메시지 타입
  + nav_msgs/Odometry
  + rosmsg show nav_msgs/Odometry

### /odom 발행 예제 코드

+ 파이썬 코드

+ [ros_odometry_publihser_example.py]:https://gist.github.com/atotto/f2754f75bedb6ea56e3e0264ec405dcf

+ 하는 일

  + odometry_publisher 노드를 생성하고 odom토픽을 생성한다. 
  + 1초에 한번 씩 발행
  

#### 실행과 확인

```bash
$ roscore
$ rosrun ex_urdf odom_publisher_ex.py
$ rostopic list
$ rostopic info odom
$ rqt_graph
```

odom토픽의 대한 정보와 타입이 다 나오며 아직 Subscriber가 없기때문에 rqt_graph에서는 publisher노드만 있다. 



+ 실습을 진행하면 됨.