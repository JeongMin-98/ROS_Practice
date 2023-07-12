# Camera
컴퓨터 비전에서는 카메라란 빛을 측정하는 장치역할을 한다. 카메라로부터 받아온 데이터를 처리하는 것을 목적으로 하기 때문이다.

+ 컴퓨터 비전에 좋은 카메라란?
  + 물리적인 빛의 밝기를 측정하는 역할

> 정확하게 빛을 측정하는 방법은 무엇일까?

진짜 빛의 신호만을 가지고있는 이미지만이 컴퓨터 비전에서 중요하다.

## Camera Sensor
모든 카메라 센서는 Photodiode 센서를 통해서 빛을 받아들이고 전압을 받아들인 다음 아날로그디지털 컨버터를 통해서 디지털 신호로 변환을 한다.

+ 컬러 카메라
  + Bayer Pattern 광필터를 이용하여 색깔을 받아온다.
  + 디지털 신호를 받아오면 보통 픽셀마다 10bit 12bit 16bit로 데이터를 받아온다.
  + 8bit RGB 이미지보다 더 섬세하게 빛을 받아올 수 있다.

> Camera에서 RAW 이미지 데이터는 이미지 센서가 받아들인 빛의 정보이고 양자화를 통해 sRGB colorspace로 매핑하게 된다.

카메라에는 다양한 종류가 있다. 

### RGB Camera(컬러 카메라)
대부분의 카메라들이 컬러이미지를 받도록 설계되어있다. 
+ 딥러닝 네트워크 
  + 색상 정보를 받아와 사용하기 때문에

단점이 있다.
> 주변 픽셀값을 통해 추론하기 때문에 정확한 값이 아니다.
+ Bayer 패턴을 풀어주는 demosaicing 과정에서 보간 에러가 발생한다.
  + 해상도가 떨어진다.
  + 보간법을 진행할 때 추가적인 연산이 필요하다.
+ 이러한 필터 때문에 모든 빛에 스펙트럼을 받아들일 수 있음에도 불구하고 정해진 빛의 스펙트럼만 받는다.
  + 이러한 이유로 빛의 밝기를 잃는다.

### Monochrome camera(흑백카메라)
흑백카메라는 컬러카메라와 동일한 칩 센서를 가지고 있지만 Bayer 패턴이 없다.
+ Bayer 패턴이 없기 때문에 이미지의 품질이 좋아진다.
+ 모든 픽셀이 모든 빛의 스펙트럼을 전부 인식할 수 있으므로 광량이 많다.
+ 노이즈에 비해 광량이 많아지기 때문에 신호처리에 용이하다.
+ 깔끔한 이미지를 받을 수 있다.

### Multi-/Hyperspectral camera
RGB 카메라보다 더 많은 카메라 채널을 가진다. 사람 눈이 보지 못하는 빛의 스펙트럼을 담을 수 있다.

### Polarized camera
픽셀들에 편광 필터를 더함으로써 빛반사를 없앨 수 있는 카메라이다.
+ 빛반사를 막을 수 있는 방법은 하드웨어만 가진다.

### Event Cameras
이벤트가 있을 때만 픽셀에 정보가 담긴다.
> 기존에 카메라보다 훨씬 더 빨리 데이터를 수집할 수 있다.

VSLAM을 할 때 빠른 속도로 움직이는 경우 이벤트 카메라는 자세와 위치를 유지할 수 있도록 한다.

# 좋은 카메라 고르는 법

+ Camera
+ Lens
  + Camera Obsura 역할을 한다. 

두 가지의 요소는 매우 중요하다.
<br>
그리고 카메라는 다음과 같은 요소가 중요하다.
+ Sensor resolution
+ Sensitivity
+ FPS
+ Sensor Size
+ Noise
+ Dynamic Range
+ Sensor Type(CCD/CMOS)
+ Global shutter / Rolling shutter
+ Form factor
+ Power / Cooling requirement
+ Interface / Mount
+ Pre-processing / ISP
+ Shock resistance
+ Price


