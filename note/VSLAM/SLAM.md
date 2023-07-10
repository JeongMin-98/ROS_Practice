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
