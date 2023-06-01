# Object Detection
> 객체 분류, 측위, 감지 하는 것의 차이는 무엇일까?
+ classification(분류): 이미지의 객체가 무엇인지 알아내는 것.
  + 객체 분류단계에서는 이미지 데이터가 CNN 모델 레이어를 통과하고 결과 값으로 N개의 확률 분포가 나오는 것
+ localization(측위): 이미지의 하나의 객체가 어디에 있고, 무엇인지 알아내는 것
  + 분류 단계에서 CNN모델을 통과하여 결과치에 확률분포로 
  클래스 별로 나오는 것에 추가하여 객체 위치에 대한 정보를 받는 
  바운딩박스에 대한 정보를 같이 반환한다. 
+ detection(탐지): 이미지에서 여러개의 객체가 각각 어디에 있고, 
무엇인지 알아내는 것


> 이런 분류, 측위 방법에서 착안하여 다음과 같은 방식으로 여러개의 
객체 탐지를 하고자 했다. 

+ Sliding Window method
  + 다수의 객체 측위가 가능
  + 컴퓨터 연산량이 매우 높고, 비효율적이다. 
  + 하나의 이미지에서 너무 많은 연산을 하게 된다. 
  + 객체의 크기가 큰지 작은지 알 수 없기 때문에 Window의 크기를 특정 할 수 없었다. 

+ Classifier + Regressor
  + 측위에서 나오는 바운딩 박스 정보를 Regressor를 따로 분리하여 결과를 내놓고
  + 여러개의 객체에 대한 정보가 나온다면 그 정보를 Box형태의 자료구조로 같이 묶는다.

> 일반적인 분류 모델과 탐지 모델의 차이는 무엇일까?
+ 분류 모델
  + 모델이 점차 계층을 지나면서 resolution되면서 layer의 크기가 작아진다. 
  + 결국 말단에서 Fully Connected를 통하여 하나의 결과를 내놓게 된다. 
  + Fully Connected를 통한 2D feature layer를 1D feature map으로 바꾼다.
+ 탐지 모델 (YOLOv1)
  + 분류 모델과 같이 진행 과정은 비슷하지만 말단 부분에서 다르다.
  + 2D feature map의 형태를 그대로 가지고 결과를 내놓게 된다. 
    + 왜냐하면 측위정보를 알 수 있도록 해야된다.

## One stage Detection & Two stage Detection
Object Detection은 두가지 방법으로 나눠진다. 
+ 해당 모델의 아키텍체에 의해 분류된다. 

### One stage Detection
한번의 Feed-Fowarding을 거쳐 결과를 낸다. 

**architecture**
![architecture](https://pbs.twimg.com/media/FCtkDKvXIAQe1H0.jpg:large)
1. Backbone: 이미지의 특징을 추출하는 단계
2. Neck: 함축적인 이미지 특징을 뽑아낸 것을 다른 resolution feature map과 병합한다. 
   + Neck 단계에서 feature maps 들을 병합하는 방법에서는 resolution을 동등하게 만들어야한다.
   + 병합하는 방법은 두 가지가 있다. 
     1. Concat: 서로 다른 featuremap들이 서로 뒷단, 앞단에 붙는다.
     2. add: 채널 수도 동일한 경우 서로 다른 element값들을 더한다.
3. Dense Prediction: Bounding Box와 객체에 대한 score를 예측
> Dense Prediction의 마지막 결과에서 여러가지 feature map에서 결과가 나올 수 있음을 명심해야함.
### Many stage Detection
![two_architecture](https://pbs.twimg.com/media/FCtkDKvXIAQe1H0?format=jpg&name=small)
여러 단계의 Feed-Fowarding을 거쳐 결과를 낸다. 
+ Faster-RCNN
  + 먼저 첫 번째 단계에서 Feed-Fowarding을 거쳐 객체의 지역에 대한 정보를 추출한다. 
  + 두 번째 모델에서는 해당 객체의 지역 (ROI)에서 객체의 위치 정보를 재정의하고 분류한다. 
  
## Grid
> Obeject Dection에서는 grid cell에서 객체를 예측한다. 
+ feature map의 Pixel의 수이다. 

+ 한개의 그리드 안에서 3개의 BOX가 생긴다. 해당 박스안에는 다음과 같은 속성이 생긴다.
  + Box to coordinates
  + objectness score
  + class scores (C개의 class에 대한 정보)

## Anchor
![Anchor](https://machinethink.net/images/object-detection/anchors.png)
앵커는 또다른 제한요소를 추가함으로써 모델이 더욱 더 예측을 잘하게 만들고 예측하고자 하는 객체의 모양을 제한한다.
+ Feature map안에서 객체에 대한 정보를 예측을 할 때 사용한다. 
+ 한개의 객체 당 하나의 앵커가 할당된다. 
+ 박스 하나당 하나의 앵커가 할당됨.

> 어떤 객체에 대해서 크기를 예측할 수 없기 때문에 크기가 다양한 바운딩 박스를 만든다.
> 해당 바운딩 박스는 앵커라고 생각해도 좋다.

## How to find the object
Bounding box, objectness score and class score를 사용하여 객체를 탐지한다.
+ Objectness score: Bounding Box안에서 포함되어있는 객체에 대해서 확률을 나타내는 것이다. 
  + 이 값은 해당되는 모든 클래스에 대한 객체에 대한 확률이 들어가게 된다. 1과 0으로 나타난다. 
+ Class score: 클래스 별로 객체에 대한 확률 값


## Softmax
![softmax](https://miro.medium.com/v2/resize:fit:720/format:webp/1*ReYpdIZ3ZSAPb2W8cJpkBg.jpeg)
각 예측한 클래스에 대해서 합산 1로 만들고 그 안에 probability 값을 산출한다. 
+ 큰 값은 극대화 작은 값은 최소화 시켜준다. 

## [Cross-entropy loss](https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e)
![Cross-entorpy](https://miro.medium.com/v2/resize:fit:640/format:webp/1*rcvGMOuWLMpnNvJ3Oj7fPA.jpeg)
> cross-entropy에 대한 반응도라고 생각하면된다. 잘 검출된다면 작은 반응도를 잘 못 검출된다면 큰 반응도를 낸다.

## [Non-Max Suppression](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c)
이 과정을 거치지 않으면 바운딩 박스는 여러개 표시될것이다. 그렇기 때문에 이 과정을 적용하여 객체 형태에 가장 적절히 매치되는 바운딩 박스를 선택한다. 




