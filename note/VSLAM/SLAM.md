# SLAM
Simultaneous Localization and Mapping
+ Simultaneous: 동시적
+ Localization: 위치추정
+ Mapping: 지도 작성

> SLAM은 로보틱스 기술에 제일 먼저 적용되었다.

### 로보틱스 기술의 진화
+ 고정된 로봇의 WorkSpace가 점점 확장되고 있고
+ Mobile Robotics에 대한 연구가 진행되고 있다.
+ 로봇의 이동은 쉽다. 

> 위와 같은 사항은 Mobile Robotics의 조건엔 부합하지 않는다.

+ 로봇은 인지하고 인지한 상황에 대해서 판단하여 행동을 결정하는 것이 목표이다.

### Perception for mobility
+ 이동 가능한 공간과 이동 불가능한 공간을 인지하는 것이 중요하다.
+ 로봇이 외부공간을 인지할 수 있도록 도와주는 센서는 **Exteroceptive Sensing**이라고 한다. 

> Sensor는 물리적인 모델을 수치적인 모델로 변환해주는 역할을 해주고, 수치모델이 실제 정보를 모두 담지 못해서 생기는 문제, 측량 단계에서 오차가 발생하기도 한다.

이러한 오차는 **Noise**라고 하고 세상에는 Noise가 없는 센서가 없다.
+ 이러한 Noise는 Error라고 표현하지않는 이유는 확률분포에 따라 발생하는 경향이 있기 때문이다.
+ 또한 이러한 Noise를 완벽하게 없애는 것은 어렵다. 하지만 실제와 같은 값을 갖도록 하는 추정을 하는 것이 목표이다

### Mobile robotics는 Ego Motion을 확실히 파악해야한다. 

자기 자신의 위치를 측정하고 자기 자신의 움직임을 인지할 수 있는 센서가 필요하다. 이러한 센서의 이름은 다음과 같다. 
+ Proprioceptive Sensing

### Perception & Control feedback loop
단점
+ Proprioceptive Sensing의 안정성 확보가 어려움
+ Exteroceptive sensing / Proprioceptive sensing의 신뢰도 
+ 노이즈 분석을 하는 동안 이동 불가

> 확률 분포를 조합할 때 주의해야한다. 
+ 둘 중 하나의 센서가 정확하다면 다른 센서를 보정할 수 있다.

**mapping** <br>
+ 정확한 Proprioceptive sensing이 있고 그 에따른 exteroceptive sensing이 있다면 정확한 Mapping을 만들 수 있다. 

**Localization** <br>
+ 정확한 exteroceptive sensing한 결과인 지도가 있고 부정확한 Proprioceptive 정보를 보정하여 위치를 찾을 수 있다. 

> 자율주행에서는 정확한 지도가 있는 것이 중요하다. 지도가 있다는 것은 앞으로 갈 곳과 가지말아야하는 곳을 판단할 수 있는 근거가 된다. 
+ 힌트가 주어졌을 때 정확하지 않으면 문제가 발생할 수 있다. 

**Monte Carlo Localization**
[link](http://jinyongjeong.github.io/2017/02/22/lec11_Particle_filter/)

## SLAM에서 사용할 수 있는 센서

+ Proprioceptive Sensing: 자기 자신의 움직임과 위치를 인지할 수 있는 센서
  + IMU: 선형 가속도 측정 센서와 각속도 측정 센서가 혼합되어있는 센서
    + 관성을 측정하는 센서
    + Spring-damper system의 원리를 이용한다. 
    + IMU의 Prior 정보를 통해서 더 빠른 계산을 한다.
    + Wheel encoder에 비해서 자동차에 일반적으로 설치되어있지 않는다.
    + 장점
      + 센서제품 자체에 저렴하다. 
      + 높은 민감성
      + 높은 FPS (Hz가 높음)
    + 단점
      + 엄청나게 빠른 drift 누적
      + 기준값이 시간이 지나면서 점차 바뀐다.
      + 날라가는 IMU 값을 잡기 위해서는 보정이 필요하다. 
        + GNSS/VSLAM+Inertial
  + Wheel encoder: 바퀴의 회전량과 이동량을 측정하는 센서
    + 측정하는 방식은 다양하다. 
    + 기본적으로 탑재
    + Odometry를 할 시 drift에 약함
    + 계속 사용하는 경우에 문제가 생긴다. 
    + 다양한 이유로 에러가 생길 수 있다. 
    + 센서의 노이즈 값이 생김
+ Exteroceptive sensing: 외부 정보를 감지하는 센서
  + 굉장히 다행한 센서가 사용된다. 
  + GNSS
    + 다수의 비콘에 대한 통신시간 차이를 이용해 비콘-로봇의 거리를 구하고 삼각 측량을 통해 localization 수행
    + Ego-motion을 추정하기 때문에 Proprioceptive sensor 같지만, 외부 비콘을 이용하기 때문에 외부 센서임
      + 인공위성 시스템에 기반에 센서
      + 나라마다 시스템이 다름
      + 장점
        + 싸고 사용하기 쉬움
      + 단점
        + 부정확함 (10~20m 오차)
        + RTK-GPS, DGPS를 사용할 경우 오차는 cm 단위로 내려옴.
        + 실내/지하는 사용 불가능
  + LiDAR: Light Detection and Ranging Sensors
    + 적외선 레이저를 쏘고 반사 시간을 측정하여 거리를 추정하는 센서
    + 주변환경 3D point cloud 형태로 바로 알 수 있음
      + 장점
        + Exteroceptive 센서 중 가장 정확한 편
        + 자율주행용 라이다는 100m 유효거리
        + 빛의 파장이 일어나지 않기 때문에 낮/밤 사용가능
        + 동일한 device로 인한 간섭이 존재한다. 
      + 단점
        + 비싼 가격
        + 카메라에 비해 resolution이 낮음
        + 눈/비/안개에 영향을 받음
        + 거리에 따라 정확도가 달라질 수 있다.
        + Multi-path 문제
          + 라이다에서 차에 반사되고 고인 물에 다시 반사되는 경우 물체의 위치나 거리를 잘못 추정할 수 있다. 
        + Solid-state LiDAR의 경우 여러 방향으로 탑재가 필요함
  + RADAR: Radio detection and ranging sensor
    + 반사되어 돌아오는 전파를 측정하여 radial 거리를 재는 센서
    + Doppler 효과를 이요해서 이동중인 물체의 속도를 추정 가능
    + 전파의 종류를 바꿈으로써 near-range와 far-range 선택 가능하다.
      + 장점
        + 날씨의 영향이 없음
        + 속도를 추정할 수 있음
        + 빛에 영향을 안 받음
      + 단점
        + 작은 물체들은 탐지가 어렵다.
        + LiDAR보다 낮은 resolution
        + Multi-path 문제
        + Doppler 효과가 없는 경우에서는 사용되지 않아 다른 센서로 커버해야한다.
  + UltraSound
    + 초음파를 이용하고 RADAR와 작동 방식이 동일
      + 장점
        + 저렴함
        + Near-range에서 잘 작동
      + 단점
        + 물체 형태를 잘 추정하지 못함
        + 많은 Distance센서로 사용
        + 노이즈가 있음
  + Camera
    + 광센서를 이용해 빛 신호를 받고 debayering 프로세스를 통해 RGB색으로 재구성한다. 
      + 장점
        + 저렴함, 
        + 좋은 성능
          + Dense data를 가지고 있기 때문에 추론이 쉽게 가능함
          + Texture
        + 렌즈 교환을 통해 시야각 변경 가능
        + 사람이 보는 시야와 가장 유사함
      + 단점
        + Depth 정보가 소실
        + 조명에 영향을 받음

## SLAM의 종류
+ Visual SLAM
  + Visual 정보를 이용한 SLAM
+ LiDAR SLAM 
  + LiDAR 정보를 이용하는 SLAM
+ RADAR SLAM
  + RADAR 정보를 이용하는 SLAM

## Visual SLAM
장점 
+ 저렴한 센서를 사용
+ 센서의 성능을 조절하기 쉬움
+ 센서 속도가 빠른 편
+ 이미지 기반 딥러닝을 적용 가능하다. 
+ 이미지로 사람이 이해하기 쉬운 시각화가 가능
단점
+ 갑작스러운 빛 변화에 대응 불가능
+ 시야가 가려지거나 어두운 곳에서 사용이 불가능하다.

### VSLAM Sensors
Camera configuration
+ RGB camera
+ Grayscale camera

3D에서 2D로 변환하는 과정에서 수학적 모델이 에러가 발생할 수 있다. 
<br>
**Type of camera configuration**
+ Monocular camera
+ Stereo camera
+ RGB-D camera

### Monocular VSLAM
1대의 카메라에서만 이미지를 받음 다른 VSLAM보다 훨씬 저렴하다. 
+ 치명적인 단점
  + 1장의 이미지로부터는 Depth 정보를 불러올 수 없다. 
  + 3D공간을 실제 스케일로 추정할 수 없다. (Scale ambiguity)
    + up-to-scale로만 추정 가능
  + IMU 센서가 metric scale를 더하기 때문에 monoculdar depth 추정을 유도할 수 있다. 
  + 딥러닝 기반 depth estimation으로 문제를 해결하는 것을 목표로 하고 있다.

### Stereo / Multi camera VSLAM
2대 이상의 카메라를 사용 <br>
인접한 카메라들간의 baseline 거리값을 metric scale로 알아야 하고, calibration으로 알 수 있고 사전에 세팅할 수 있다. 
+ 인접한 카메라들간의 baseline 거리를 기반으로 삼각 측량을 통해 거리/깊이를 추정할 수 있다. 

장점
+ 두 이미지간의 disparity 정보를 이용해서 픽셀마다 depth를 추정할 수 있다. 
+ Metric scale의 3D 공간을 복원 가능하다.
단점
+ 카메라 설정 및 캘리브레이션이 어렵다. 
+ 이러한 캘리브레이션은 상용화에 어렵게 한다. 자동차 업계에서는 자동차 캘리브레이션을 한대 한대마다 실행하기 때문에 한대 당 제조 단가가 높아진다. 
+ 이러한 캘리브레이션은 정확한 위치 추정을 위해서 하는 것임으로 대충 계산할 수는 없다. 
+ 모든 카메라는 동시에 이미지를 취득해야한다. 
+ 카메라들마다 Instric/Extrinsic 캘리브레이션을 정확하게 해야한다. 
+ 모든 픽셀 마다 disparity 정보로 depth를 계산하는 데에는 많은 계산량이 필요하다. 

### RGB-D VSLAM
센서가 Depth 값을 직접 얻어주기 때문에 계산이 필요하지 않는다. 
<br> Dense mapping을 많이 하는 편이ㅏㄷ. 
장점: Depth 데이터를 통해 3D 공간을 metric sacle로 실 시간 복원이 가능하다.
단점: ~10m 정도에서만 depth 데이터가 정확함