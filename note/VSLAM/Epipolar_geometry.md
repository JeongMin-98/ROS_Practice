# Epipolar Geometry
**2 - View Geometry**
<br> 2 View Geometry란 바라보는 시점은 다르고 같은 3D point(객체)들을 바라보고 있는 두개의 이미지를 보고 있는 것이다. 

+ Epipolar Geometry
+ Epipolar Line

## Epipolar line
![img](img/epipoloar.jpg)<br>
> Epipolar Geometry에서 굉장히 중요한 개념이다.

+ ray : 빛이 이동한 직선

ray가 다른 시점에서 찍은 Image Plane에 맺히게 되는 데 이를 재투영이라고 한다.<br>
ray를 재투영한 직선을 **Epipolar Line**이라고 한다.

+ 왼쪽 시점에서 3D point는 무조건 Epipolar Line에 나타난다.


## Epipole
![epipole](img/epipole.jpg)
<br>
왼쪽 시점에 image plane1에 잡힌 3D point들의 각각의 **ray들**을 오른쪽 시점에 image plane2에 재투영하였을 때
종종 교차점이 생기는 이를 **epipole**라고 한다. 
<br>
이 epiploe의 기하학적 의미는 시점이 시작하고 ray들의 시작점인 optical center를 의미한다. 그리고 이 의미는 optical center 1이 image plane2에 재투영된다는 의미이다.

## special cases
### Stereo Camera configuration을 사용하는 경우
![img](img/special_stereo.jpg)
이미지 두개가 epipolar line이 완전히 평행하게 나타난다. <br>
이 때문에 epipole가 나타나지 않는다.

> epipolar line이 모두 가로로 나타나고 평행하다. 

가로에 나타난 row는 구하기 쉽다. 픽셀에 access가 빠르다.

### Monocular Camera forward motion
![img](img/moncular_forward.jpg)
epipolar line이 방사형 형태로 나타난다.

## Epipolar geometry
![plane](img/epipolar_plane.jpg)<br>
Epipolar line, Epipole의 정보가 함께 담겨 있다. 

+ Baseline
  + 2개의 2 optical centers를 연결한 점. 
  + Epipolar plane에 Baseline이 optical center를 연결한 점이다. 

Baseline과 ray는 교차하게 된다.
<br>
3D point X의 위치를 조정하면 각각의 epipolar plane들이 생기는 데 이에 생기는 X는 Baseline을 기점으로 생기는 윈기둥 상에 나타난다. 
<br>
**Correspondence의 3가지 조건**
+ 3D point X는 Epipolar plane에 놓여야한다. 
+ 모든 epipolar lines들은 baseline과 epipoles에서 교차해야한다.
+ 모든 epipolar planes는 baselines들을 모두 포함하고 있어야한다. 

# Essential Matrix
epipolar constraint를 담고있는 Matrix이다. Correspondence를 담고 있는 과정이다. 

# Fundamental Matrix
Intrinsic Matrix(K)를 이용하여 Essential Matrix를 보충하여 Fundamental Matrix를 정의한다. 
<br>![Fundamental](img/FM.jpg)<br>

Fundamental Matrix를 사용하면 반대편 Plane에 있는 Epipolar line을 구할 수 있다. 
[8pointAlgorithms](https://www.youtube.com/watch?v=z92eUJjIJeY)

+ OpenCV에서 쉽게 사용할 수 있다. 
+ findFundamentalMat()
+ recoverPose()

> correspondence는 feature descriptor간의 match 정보이다.




