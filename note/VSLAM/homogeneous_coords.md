# Projective geometry (사영 기하학)

> 기찻길 사진에서 두 평행한 기차 선로는 절대 만나지 않는다. 이것을
> 수학적으로 표현하면 유클리드 기하학에서 평행하다. 무한의 거리에서 두선은 교차한다는 의미를 가진다.
> 무한의 의미를 숫자로 표현할 수 없다. 교차와 평행이라는 개념은 동시에 표현할 수 없다.

하지만 사진에서 기찻길은 한 점에서 교차하게 된다. 이러한 교차점을 소실점이라고 한다. 

<br> 이런 현상은 사진에서는 원근법이 적용되기 때문이다. 사진에서의 객체의 크기는 정확하게 특정 할 수 없다. 

+ 현실 세계에서 사진으로 표현되는 차원 변환에서 깊이 정보가 소실된다.
+ orthogonality도 잃는다.
+ scale도 잃는다.
+ parallelism도 잃는다.

이러한 이유로 사영기하학에서는 3D세계에서의 무한의 거리를 2D 이미지에서 소실점으로 표현할 수 있다. 
무한의 위치또한 특정 픽셀로 매핑할 수 있다는 것이다. 

> 이러한 연구들로 인해 기하에는 계층이 생겼고 다음과 같다.

각 계층이 존재하고 상위 계층으로 올라가면서 기능이 추가된다. 
+ Euclidean
  + Rotation + Translation 표현 가능
+ Similarity
  + Euclidean transformation에서 Uniform scaling을 표현할 수 있다. 
    + 모든 방향으로 scale의 변화를 가질 수 있다. 
  + 위와 같은 변환에서 length 정보가 소실된다.
+ Affine
  + Similarity transformation에서 Non-uniform scaling + shear 표현 가능
    + 방향에 따른 scale의 변화를 가질 수 있다.
  + 위와 같은 변환에서 Angle / Length-ratio 정보가 소실된다. 
+ Projective
  + Affine transformation에서 projection 표현 가능
    + 무한대에 있는 객체에 대해서 원근법을 유지한채 표현할 수 있다. 
  + 위와 같은 변환에서 incidence, cross-ratio 정보가 소실된다. 

> Projective geometry는 3차원에서 2차원으로의 차원 축소만 가능하지 않고 다른 N+1차원에서 N차원의 차원 축소도 가능해졌다.

# Homogeneous coordinates
0이 아닌 스칼라 람다를 곱해도 homogeneous coordinates의 x 객체들은 변하지 않는다. 그러므로 x와 lambda*x는 같은 x임을 나타낸다.

## Euclidean Space VS. Projective Space 

Euclidean space
+ Cartesian coord
+ 사영기하공간의 Scale이 1인 부분 집합이다.
+ Cartesian coordinates의 값을 Homogeneous coordinates의 값으로 나타내기 위해서는 scale값을 함께 표현하면 된다.
  
Projective space
+ Homogeneous coordinates
+ 동차좌표계의 값을 Cartiesian 좌표계의 값으로 변환하기 위해서는 scale 값으로 모두 나눠 scale 값이 1이 되도록 하면 된다.

RIGID의 SO(3), SE(3) 매트릭스 또한 1이라는 scale 정보를 추가하면된다.