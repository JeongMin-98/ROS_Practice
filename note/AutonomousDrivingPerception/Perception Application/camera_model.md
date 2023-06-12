> 자율주행 Perception에서는 주행환경을 인지하는 과정으로 유의미한 정보를 생성하는 단계가 필요하다.<br>
> Vision의 경우, 이미지 영역에서 객체를 인식하는 것이 아닌 객체와 차량의 관계를 파악하는 것이 중요하다. <br>
> 왜냐하면 차량은 객체를 단순히 인식하는 것이 아니라 객체와 차량의 위치 정보에 대한 관계를 알아야 충돌을 방지할 수 있기 때문이다.

이러한 이유로 3D POSE Estimation을 통한 기본적인 Vision 기반 기술을 알아보고자 한다.

+ 3D POSE Estimation
+ Vision Geometry

![3d_pose](https://docs.opencv.org/2.4/_images/pinhole_camera_model.png)

**카메라란**
<br> 카메라는 **3차원 공간**인 세상에 존재하는 **대상(객체)**을 **2차원 공간**인 이미지 **평면에 투영**하는 센서이다.
> 카메라 모델은 카메라의 투영 과정을 **수학적 모델**로 표현한 것이다.

+ 사람은 이미지를 보고 직관적으로 다양한 추론이 가능하다. 거리가 멀고, 가깝고를 직관적으로 안다. 
+ 이미지에서 표현되는 크기는 달라도 실제 크기는 동일하다는 것을 직관적으로 안다.

## [Pinhole Camera model](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html)
![Pinhole](https://docs.opencv.org/2.4/_images/math/803e522ec37bc5bc609c0ef08373a350a819fc15.png)
+ intrinsic parameters
+ [R|t]: extrinsic parameters.
  + 카메라와 대상과의 관계
+ Scaled vector