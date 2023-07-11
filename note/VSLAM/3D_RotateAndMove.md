> 3D Rigid Body Motion과 다양한 회전 표현법과 Coordinate Transformation에 대해서 소개

# 3D Rigid Body Motion
> Rigid Body란 강체이다.

Rigid Body도 다른 물체의 위치 정보를 좌표로 표시하듯이 표시할 수 있다. 

+ Position
+ Orientation

위 두가지 방법으로 표현할 수 있다. 이 것을 **Pose** 라고 한다.

다양한 Coordinate 표현 방법이 있다. 
+ 예를 들어, 카메라 좌표계에서 표현되는 좌표가 실제 현실 세계의 좌표계에서 표현되기 위해서는 어떤 변화가 필요하다. 

Coordinate Transformation을 해주기 위해서는 각 좌표계 간의 **orientation** 변화와 **Position**의 변화를 알아야 한다.  

이러한 변화를 **Rigid body motion** 이라고 한다. 
+ 같은 말로 Euclidean trasformation이라고 한다. 

# 다양한 회전 표현법
## Euler Angle
+ 각각의 축에 Roll / Pitch / Yaw로 표현한다.
+ 3D rotation을 표현하기 위해서는 차례로 변환을 해줘야한다. 
+ 회전 각의 순서에 따라 서로 다른 좌표계를 나타낸다.

단점 
+ 미분에 어려움이 있다. 
+ 최적화를 하기위해서는 미분이 가능해야하다.
+ 즉 최적화에 어렵다.

## Axis-angle
물리학에서 Vector를 바라보는 관점으로 회전을 표현한 방법이다.
> Axis-angle <-> Rotation matrix 하는 공식인 Rodrigues formula가 있다. 


## Quaternion
Singularity 문제를 해결하기 위해서 사용
> 3D 공간에서 표현하면 Singularity 문제는 항상 발생함

4차원으로 표현하는 방법을 사용한다. 
Complex number를 사용한다. 
> 슬램에서 사용하기 좋으나 4차원 공간의 표현이기 때문에 바로 표현하기 어렵다.

## SO(3) Rotation Matrix
+ Orthogonality를 유지해야한다.
+ x,y,z의 unique vector의 길이가 바뀌면 안된다.
+ 각 매트릭스의 Determinant는 1이 되어야한다.
+ SO(3)의 행렬과 그 역행렬의 곱은 Indentity 매트릭스가 나온다. 즉 Transpose한것과 동일하다는 것.

## Metric Translation vector
이동치는 그냥 3차원 vector로 표현하면됨.

## SE(3) Transfromation matrix
Special Euclidean Group
> SO(3) rotation matrix와 Translation vector를 같이 표현하면 된다.
+ 4x4형태의 매트릭스이다.