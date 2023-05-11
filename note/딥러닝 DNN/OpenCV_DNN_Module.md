# 딥러닝

+ 딥러닝 vs 머신러닝
  + 머신러닝
    + 머신러닝은 수동적으로 특징들을 추출한다. 
    + 색깔, 엣지등 정보를 추출한다. 
    + SVM 사용
    + 변별력이 떨어지는 경우엔 SVM가 잘 작동해도 모델의 분류가 어렵다.
  + 딥러닝
    + 사람이 수동적으로 특징을 정해서 입력하는 것과 다르다
    + 사진과 레이블의 정보에 대해서 모델에 입력
    + 신경망이 특징을 추출하고 분류한다. 

# 컴퓨터 비전 분야에서의 딥러닝 활용
+ Image Recognition
+ Object Detection
+ Object Segmentations


## 신경망 기초

+ 퍼셉트론
  + 다수의 입력으로부터 가중합을 계산하고 이를 이용하여 하나의 출력을 만들어 내는 구조
+ ![perceptron](https://www.saedsayad.com/images/Perceptron_1.png)

+ 은닉층이 한개 이상이면 **다층 퍼셉트론**이라고 한다. 
+ 은닉층이 두개이상이면 **심층 신경망**이라고 한다. 

## 컨볼루션 신경망 CNN

+ 영상 인식 등의 딥러닝 분야에 특화된 네트워크 구조
+ Convolution + Pooling + fully connected layer

# DNN 모듈
+ 미리 학습된 딥러닝 모델을 이용해 실행하는 기능
+ 학습은 지원하지않음
+ 3.3버전부터는 기본 기능으로 제공됨
+ 4.3버전부터는 GPU 지원 소스코드를 직접 빌드해야함

+ ONNX 형식으로 저장하고 해당 모델을 사용할 수 있음

## 네트워크 불러오기

```cpp
Net readNet(...);
```
+ model: 훈련된 가중치를 저장하고 있는 이진 파일 이름
+ config: 네트워크 구성을 저장하고 있는 텍스트 파일 이름
+ framework: 명시적인 딥러닝 프레임 워크 이름
+ return value: dnn::Net 객체

## 네트워크 입력 블롭 만들기 (다차원 행렬)
```cpp
Mat blobFromImage(...);
```
+ image: 입력 영상
+ scalefactor: 입력 영상 픽셀 갑셍 곱할 값
+ size: 출력 영상의 크기(**모델에서 사용하는 영상의 크기로 resize**)
+ mean: 입력 영상 각 채널에서 뺄 평균 값
+ swapRB: R과 B채널을 서로 바꿀것인지 결정하는 플래그
+ crop: 크롭 수행 여부
+ ddepth: 출력 블롭의 깊이
+ return: 영상으로 구한 블롭 객체. NCHW 행렬

## 네트워크 입력 설정하기
```cpp
void Net::setInput(...);
```

+ blob: 블롭 객체
+ name: 입력 레이어 이름

## 네트워크 순방향 실행

```cpp
Mat Net::forward(...);
```
+ outputName: 출력 레이어 이름
+ 반환 값


# MNIST  학습하기
+ tensroflow, pytorch를 이용해서 MNIST 필게체 숫자 인식을 학습하기
+ 학습된 모델을 파일로 저장하기
+ OpenCV에서 학습된 모델을 불러와서 필기체 인식 프로그램을 실행

+ 저장방법은 인터넷에서 추가 정리

