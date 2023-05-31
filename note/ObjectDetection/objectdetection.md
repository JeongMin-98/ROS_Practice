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
3. Dense Prediction: Bounding Box와 객체에 대한 score를 예측
> Dense Prediction의 마지막 결과에서 여러가지 feature map에서 결과가 나올 수 있음을 명심해야함.
### Many stage Detection
여러 단계의 Feed-Fowarding을 거쳐 결과를 낸다. 
+ Faster-RCNN
  + 먼저 첫 번째 단계에서 Feed-Fowarding을 거쳐 객체의 지역에 대한 정보를 추출한다. 
  + 두 번째 모델에서는 해당 객체의 지역 (ROI)에서 객체의 위치 정보를 재정의하고 분류한다. 
  

