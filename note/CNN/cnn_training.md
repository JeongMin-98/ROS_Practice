# Training
Feed Forward & backward를 통해서 학습 데이터에 맞는 가중치 값을 찾는다. 
> 주로 경사하강법(Gradient descent method)를 사용한다. 

## Optimizer
경사하강법은 loss function을 최소화하는 것이 목적이다. 

+ loss값을 줄이는 개념을 나타나는 방식을 여러가지로 나타낼 수 있다. 
  + SGD: 한개의 데이터바다 그래디언트를 업데이트를 한다. 
    + MGSD: 이상치에 대해서 보완한 학습 방법
    + learning rate에 따라 학습률이 정해진다. 
  + Momentum
    + velocity term: 이전 단계의 그래디언트 방향을 저장한 변수
      + 이를 통해서 지속적으로 그래디언트 방향을 유지할 수 있다. 
    + local minima에 빠지지 않도록 할 수 있다. 
  + AdaGrad
    ![adagrad](https://t1.daumcdn.net/cfile/tistory/9977C44C5D11FAE52A)
    + 미분값을 제곱한 값들을 이용함.
    + 수렴이 느리다. 
  + RMS-prop
    + Adagrad의 단점을 보완하고자 지수이동평균를 추가하여 이용 
  + Adam
    + RMS-prop + Momentum


> SGD is better than ADAM?
1. 결과적으로 non-adaptive method가 일반화가 잘되고 수렴이 잘된다. 
2. 수렴의 속도는 느리지만 Generalization이 잘된다. 

## Overfitting & Underfitting

**Overfitting**
+ 훈련데이터로 훈련하고 모델에 적합하게 fit되지만 새로운 도메인에는 낮은 성능이 있다 
+ 훈련데이터에 대해서만 낮은 loss를 보여준다. 

**Underfitting**
+ 훈련데이터에 훈련이 잘 되지않는 경우
+ 적은 데이터 셋, 적절하지 못한 파라미터 값

## Regularization
오버피팅된 모델은 큰 value의 가중치를 가진다. 
> 그래서 정규화 term을 loss function에 사용한다. 작은 값의 weight model을 가지게 된다. 
### L1 Regularization
가중치의 절댓값의 합을 패널티 값으로 사용하고 그 값을 error값에 더한다. 

### L2 Regularization
가중치의 제곱값의 합을 패널티 값으로 사용한다. L1에 비해 더 스무스한 값을 가진다. 

## Dropout
모델의 구조를 짜고나서 Forward-Feeding을 진행한다. 특정한 값이 큰 값을 가지고 있는 경향이 있을 수 있다. 

그 때 layout 안에서 뉴런들을 없애는 것을 사용하여 bias가 생기는 것을 방지하고, 그리고 과적합된 모델의 성능을 향상시킨다. 

> 학습 시킬 때만 사용한다. 

## Batch normalization
활성 함수를 사용하기 이전에 stable한 입력 값을 가지도록 한다. 

+ batch data의 평균값, 분산을 사용하여 분산된 값을 사용한다. 

