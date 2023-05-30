# CNN
Convolutiion
+ Convolutioinal matrix 
+ matrix의 크기는 3X3, 5X5
+ 입력 이미지의 정보를 출력하는 역할을 함

Feature Map을 구해래면 sliding Window로 연산이 이루어짐
+ Padding : 원본 이미지에 경계선 외곽에 zero value를 넣어준다. 이 값은 따로 설정할 수 있다.
+ Stride : sliding을 할 때 Kernel이 움직이는 간격

**Output Shape**
+ H = (Input_Height - kernel_height + padding * 2) // stride + 1
+ W = (Input_Weight - kernel_Weight + padding * 2) // stride + 

> Convolution 연산에는 A, W, B shape가 있다. 

+ A shape
  + Batch: 한 Inference에 연산하고자하는 Batch의 수를 주어진다. 
  + Input_channel => 이미지들의 정보들
  + Input_height
  + Input_weight
+ W shape
  + Output_channel
  + kernel_channel : Input_channel의 값과 동일하다. 
  + kernel_height
  + kerenl_weight
+ B shape
  + Output_weight
  + Output_channel : 위 수식에 따라 정해진다. 
  + Output_height : 
  + batch : batch 수 

## Convolution operation
**MAC : Multiply Accumulation operation**
+ Kernel_weight * kernel_height * kernel_channel * output_channel * output_width * output_height * batch
+ MAC이라는 단위를 사용한다. 
+ Input size * kernel * size * batch를 구한다. 
+ 이러한 연산량은 모델의 성능을 판단하는 데 사용한다. 

> Convolutiion operation에서는 7번의 loop를 돈다.

+ 실제로는 효율적인 연산으로 연산을 할 수 있다.
+ 두가지 방법이 있다. 
  + IM2COL: n차원의 데이터를 2D matrix의 data로 변환을 해준다. 
    + kernel로 연산된 값을 1차원의 벡터값으로 구해준다. 그리고 이 연산은 Output Channel수 만큼 연산한다.
  + GEMM

# Pooling
feature map의 resolution을 줄일 수 있다. 
+ 이미지의 특징점을 요약할 수 있다. 

1. Max Pooling
2. Average Pooling

## Max Pooling
각 해당 위치에서의 최댓값을 특징값으로 뽑아내는 연산
> 해당 feature map의 최댓값을 구해내기 때문에 edge부분을 많이 추출되는 경향을 보인다. 

## Average Pooling
Pooling 방법과 메트릭은 동일하지만 각 해당 위치에 대해서 평균값을 특징값으로 뽑아내는 연산이다. 
> 해당 feature map의 평균값을 구해내기 때문에 smoothing된 형상을 나타난다. 자연스러운 모습

# Fully Connected Layer
입력영상의 기하학적인 정보를 담고있는 2D Feature map을 1D FC feature map으로 전환시켜주는 역할을 한다. 


# Activiaion Function
**활성함수**
+ Pooling, Conv 연산을 한 이후 값들 중에서 유의미한 값을 더 많은 특징을 주도록 하는 함수

> 활성 함수는 비선형 함수이다. 역전파를 할때 그래이디언트 값이 다르기때문에 weight값을 갱신할 수 있다. 

+ sigmoid
+ tanh
+ **ReLU**
+ LeakyReLU
