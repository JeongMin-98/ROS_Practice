# Distortion(왜곡)
왜곡은 렌즈 형상이 곡률을 가지는 구면 형태이기 때문에 발생한다. 따라서 이미지 중심부에서 멀어질수록 표현의
비율이 달라지기 때문에 발생한다.

+ 왜곡에는 방사/접선 왜곡 외에에도 다양한 형태의 왜곡이 존재한다. 
+ 이러한 왜곡들은 수학적 모델로 해결할 수 있다. 

투영되는 기하하적 정의에 따라 부가적인 정보, 조건 없이 이미지에서 출력된 정보만으로 3차원 공간 정보로 복원하는 것은 어렵다.
<br>
이러한 문제를 해결하기 위해서는 다수의 카메라를 사용하거나 2장 이상의 이미지를 사용하는 방법이 있다. 
+ 다수의 카메라를 사용하는 방법
  + 2개 이상의 카메라로 동일한 시점에 촬영한 각 1장의 이미지 만으로 3차원 위치 정보를 추정할 수 있다. 
  + 이러한 경우 각각의 카메라의 Extrinsic Parameter를 알아야 정확한 정보를 얻을 수 있다. 
+ 2장 이상의 이미지를 사용하는 방법
  + 같은 카메라로 움직이는 환경이나 연속된 이미지 정보를 활용하여 3차원 위치 정보를 추정할 수 있다. 
  + 이는 카메라의 움직임 정보를 정밀하게 측정하고 추정해야 정확환 정보를 얻을 수 있다. 
> 이러한 이유로 Multiple View Geometry에 대한 이해가 필요하다.



## 방사 왜곡
> 방사 왜곡은 이미지의 중심으로 부터 멀어질수록 왜곡의 정도가 심해진다.

렌즈 왜곡의 대표적인 예이다. 두가지 형태로 표현된다.
+ Barrel Distortion(Positive radial): 중심부가 외각부보다 큰 형태로 발생
+ Pincushion Distortion(Negative radial): 중심부가 외각부보다 작은 형태로 발생

## 접선 왜곡
카메라 제조 공정에서 발생하는 왜곡으로 렌즈와 이미지 센서와의 수평이 맞지 않은 경우에 발생한다.
> 타원 형태로 발생하는 왜곡으로 방사 왜곡과는 다르게 발생한다. 

