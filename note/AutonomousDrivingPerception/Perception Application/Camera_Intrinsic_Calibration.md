# Camera Calibration
카메라가 가지고 있는 고유한 특성을 파악하는 과정이다. 
![model](https://docs.opencv.org/2.4/_images/math/803e522ec37bc5bc609c0ef08373a350a819fc15.png)
> 카메라는 Camera Project Matrix에 의해 두가지 고유한 특성을 갖는다.
+ Intrinsic: 카메라의 내부적 특성
+ Extrinsic: 카메라가 대상을 촬영했을 당시의 위치와 자세에 관한 특성

> Calibration을 진행할 때 Vision에서는 초점거리를 Pixel 단위로 표현한다. 이는 디지털 카메라에서 
> 사용하는 초점단위와 단위가 다르다. <br> 그래서 이미지 해상도에 따라 초점거리가 달라진다.


## 왜 Intrinsic / Extrinsic로 구별할까?
동일한 위치에서 서로 다른 카메라로 동일한 피사체를 촬영하면 그 결과가 다르다. 
왜냐하면 카메라마다 내부적 특성인 Intrinsic을 가지고 있기 때문이다.

> Intrinsic을 계산하는 과정을 Intrinsic Calibration이라고 한다. 

또한 다른 위치에서 같은 카메라로 동일한 피사체를 촬영한다면 그 결과가 다르다.
<br> 이러한 과정을 통해서 Extrinsic Calibration 또한 가능하다.

> 두 가지 특성에 대해서 Calibration을 진행해야된다. 

## [Intrinsic Calibration](https://mphy0026.readthedocs.io/en/latest/calibration/camera_calibration.html)
![img](https://mcarletti.github.io/articles/blenderintrinsicparams/imgs/Kmat.png)
<br> 위 이미지에 대한 자세한 정보는 다음 링크를 참고 https://mcarletti.github.io/articles/blenderintrinsicparams/
<br><br>
초점거리와 주점을 의미한다.
+ 초점거리 : Pinhole부터 이미지가 맺히는 벽까지의 거리
+ 주점 : Pinhole이 이미지 센서에 직교하는 위치
+ 비댕칭 계수: 이미지 센서의 Cell Array의 y축이 기울어진 정도

> 이미지의 중심점과 주점은 서로 다른 개념을 가진다. 또한 주점이 이미지 중심점과 일치하지 않는 경우도 존재한다.

**더 자세한 정보는** https://darkpgmr.tistory.com/32 참고
