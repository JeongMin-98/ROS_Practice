# OpenCV

+ 오픈소스
  + BSD라이선스
+ 프로그래밍 편리
  + 대부분의 운영체제 지원
  + C, C++, Java, Python 지원
  + 다양한 CPU와 GPU 하드웨어를 지원
+ 많은 응용분야에서 사용

## 버전

+ 1.x : C언어로 작성
+ 2.x : C++언어로 재작성
+ 3.x
  + 모듈별로 라이브러리가 분리되어 있으나 버전에서 통합됨
  + OpenCL 지원을 통해 실행속도가 개선됨
  + 특징점 추출 알고리즘과 관련 기능이 보강되고 추가됨
+ 4.x
  + 딥러닝 패키지가 추가됨(Yolo 등의 딥러닝 기능의 사용이 용이해짐)

## OpenCV 이미지 표현 방식

680 X 480 해상도에서는 한 행에 640개씩 들어있고 480개의 열이 있음

점 하나를 표현하는 [B, G, R] 형태의 배열이 있음

배열의 형태는 480 * 640 * 3 이며, 

데이터 타입은 numpy.ndarray 이며 다차원 배열을 표현하는 구조이다.

+ 1픽셀 표현을 위해서 3채널 (B, G, R) 3바이트를 사용
+ 컬러는 B,G,R 순서로 배열되며 3채널 구조이다.

## 좌표계

이미지의 0, 0은 항상 좌상단에 있음. 오른쪽으로는 x가 증가 아래쪽으로는 y값이 증가.

좌표값 표시에 순서쌍(tuple)을 이용



## 기본적인 도형 그리기

### 선

line(img, start, end, color, thickness)

img = cv2.line(img, (0, 0), (511, 511) , (255, 0, 0), 5)

### 사각형

rectangle(img, start, end, color, thickness)

### 원

circle(img, center, radius, color, thickness)

### 텍스트

putText(img, txt, org, font, fontScale, color)

## 이미지 파일 다루기

### 이미지 파일 읽기

+ imread(filename, flags)
+ cv2.imread(img, cv2.IMREAD_GARYSCALE)

### 화면에 이미지 표시하기

+ imshow(window_title, image)
+ cv2.imshow('color', img)

### 이미지를 파일 저장

+ imwrite(filename, image)



## 관심영역 - ROI

이미지 화면 내에서 관심영역은 numpy.ndarray의 다차원 배열에서 특정 영역을 잘라낸 구역이다.

```
img[120:270, 270:460]

img[y축, x축]
```



## 색상 표현

### HSV 색상 표현

색상 또는 명도를 기준으로 이미지를 표현하는 방법

객체를 분할하기에 용이하며 이미지 처리에 많이 사용하는 표현 방법이다.

+ 색상(hue) : 색의 질, 노란색, 빨간색, 파란색... 0-180
+ 채도(saturation): 선명도, 원색에 가까울수록 채도가 높음 0-255
+ 명도(value): 밝기, 명도가 높을수록 백색에 낮을수록 흑색에 가까워짐 0 -255

선의 명도 차이로 선과 선이 아닌 부분을 구분하는 것이 좋다.

```python
import cv2
import numpy as np

img = cv2.imread('cars.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,150])
upper_white = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_white, upper_white)

cv2.imshow('line', mask)

cv2.waitKey(10000)
```

HSV 색상 범위 중 찾고자하는 범위를 지정할 수 있다. 그리고 inRange함수를 통해서 해당 범위에 포함되는 픽셀들은 흰색으로 표현할 수 있고 그 외의 픽셀들은 검은색으로 이진화한 grayscale이미지를 만들 수 있다.



## 명도 범위의 조정

HSV중 V 범위를 조정해서 차선을 분리할 수 있다. 차선의 색상 또는 주변 밝기에 따라 범위 지정값은 달라져야한다.

영상처리할때 빛 반사를 중요하게 생각해야한다.



## 동영상

+ 동영상 : 정지 이미지가 시간에 따라 바뀌며 나타나는 것
  + 빠르게 이미지를 보여주면 사람 눈은 이것을 움직이는 그림으로 인식한다.

### 프레임

+ 동영상 내에서 한 장 한 장의 그림을 프레임이라고 부름
+ 얼마나 빠르게 다음 그림을 보여줄 수 있는 표현
+ fps(frames per second)
+ 자이카 => 1초에 30장

> 자율주행 알고리즘에서는 프레임 단위의 이미지를 분석하여 주행 제어를 결정하게 된다.



## 동영상 재생 VS 카메라 입력 처리

+ 동영상 = 사진을 연속적으로 표시하는 것
+ 카메라 = 영상정보를 받아 표시하는 것인데 이것은 동영상 파일을 열어 재생하는 것과 동일하다.
+ 숫자 0은 default camera이다.
