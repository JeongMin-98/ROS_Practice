## 카메라

### ROS package

+ UVC 1.1 스펙을 지원하는 카메라 ROS 패키지 사용

+ 웹캠과 같은 범용 USB 카메라 제어용 

### 노드와 토픽

+ /usb_cam 노드에서 발행하는 /usb_cam/image_raw 토픽을 이용한다. 

```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
uint32 height
uint32 width
string encoding
uint8 is_bigendian
uint32 step
uint8[] data
```

## IMU 센서

+ 가속도 센서 또 접근하면 속도
+ 자이로 센서
  + 회전 속도인 각속도를 감지
+ 지자계 센서
  + 동서남북을 확인

### ROS Pakage

+ ros community 에서 많이 사용하는 제어용 ROS 패키지가 있음

+ 가속도계 /자이로/지자계의 정보를 수집하고 전송하는 일을 처리함

### 노드와 토픽

+ /xycar_imu노드에서 발행하는 /imu 토픽을 이용

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

## 라이다

### ROS Package

+ 라이다 제조사에서 제공하는 ROS 패키지 사용
+ 라이다로부터 장애물까지의 거리 값을 수집하고 전송하는 일을 처리함

### 노드와 토픽

+ /xycar_lidar 노드에서 발행하는 /scan 토픽을 이용



## 초음파 센서

+ HC-SR04 초음파 센서
+ 작동원리
  1. 송신부에서 초음파 발사
  2. 초음파가 물체에서 반사된다
  3. 반사된 초음파가 수신부에서 감지된다.
  4. 송신과 수신 사이의 시간 간격을 기준으로 물체까지의 거리를 계산한다. 

+ 자이카에는 모두 5개 설치
  + 후방 3개
  + 좌측 1개
  + 우측 1개
  + 아두이노에 초음파 센서 연결되어있고 USB를 통해 프로세서 보드와 연결되어있음

### ROS pakcage

+ 아두이노가 각각의 초음파 센서를 제어하여 거리정보를 수집한다. 
+ 전체 초음파 센서의 거리정보를 통합하여 관리한다. 
+ 이 아두이노와 토픽 발행과 구독을 하면서 정보를 가지고 온다. 

### 노드와 토픽

/xycar_ultrasonic 노드에서 발행하는 /xycar_ultrasonic 토픽을 이용한다. 

노드와 토픽의 이름은 같다. 



## Depth 카메라

+ 인텔 리얼센스 카메라

### ROS package

카메라 제조사가 제공하는 ROS 패키지를 사용

+ 모두 3개의 카메라를 제어하여 영상정보와 거리정보를 수집함
+ 다양한 토픽에 다양한 정보를 담아 제공함

### 노드와 토픽

/camera/realsense2_camera 노드에서 발행한다. 

1. /camera/color/image_raw => 평상시 보는 영상정보
2. /camera/depth/image_rect_raw => 흑백으로 보이는 데 가까운지 먼지 알 수 있는 영상정보



### 카메라 실행

```bash
$ roslaunch realsense2_camera demo_pointcloud.launch
```

