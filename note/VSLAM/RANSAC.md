# SLAM에서는 Outlier rejection이 필요하다. 

SLAM 에서 사용되는 데이터는 두가지이다.
+ Inlier data
  + 좋은 데이터
  + 예상한 데이터 분포에 포함된 데이터
+ Outlier data
  + 안 좋은 데이터
  + 예상한 데이터 분포에 포함되어있지 않은 데이터

Outlier Data 발생 조건
+ Illumination changes
+ Rotations
+ Heavy occlusions
+ Abrupt motions

Outlier Data는 한 알고리즘에서 발생되는 큰 문제를 야기시킨다.

Computer Vision Algorithms
+ Closed-form algorithms
  + minimum solve가 있다.
  + 정확한 기하학적 조건을 만족해야함.
+ Iterative Optimization
  + 훨씬 더 많은 데이터를 가지고 작동된다. 
  + 모든 데이터가 만족하는 결과를 얻어야한다. 
  + Inlier data 속에서 패턴을 찾아서 작동된다. 

이러한 알고리즘 패턴의 이유로 Outlier data가 없어야한다. 
<br>
깔끔한 Inlier data만 꼭 남겨야한다. 

## Linear regression case
2D plot에서 여러개의 Data가 있을 때 가로지르는 Line을 구하는 것이 목적 (Line Fitting이라고 함)

<br> 데이터 속에서 라인을 구하는 방법으로는 다음 두 가지 방법이 있다. 
+ SSE
+ SAE

Outlier data는 모델을 추정하는데 nosiy data임으로 불필요하다. 하나라도 Outlier가 있다면 정확하지 않은 data를 가진다.

> Outlier rejection은 필수적인 과정이다. RANSAC, M-Estimator, MAXCON등이 필요하다.

# RANSAC
Random sample consensus
+ Random: 무작위하게
+ Sample: 데이터 샘플을 뽑아 모델을 만들어
+ Consensus: 모델에 대한 데이터의 합의도를 알아본다. 

무작위하게 데이터 샘플을 뽑아 모델링을 하여 모델에 대한 데이터의 합의도를 알아본다.
<br>
**RANSAC은 Template algorithm 이다.** 
> 계산하는 알고리즘은 RANSAC안에서 다양하다. 모델을 추론하는 과정이라고 이해하면 된다. 

**Algorithm 순서**
1. Sampling하는 데 최소한의 데이터 셋을 랜덤하게 고른다. 
2. 샘플링된 데이터를 모델을 추정하는 데 사용한다. 
3. Model Score를 계산한다. 
4. 1번과정으로 돌아가 반복한다. 

반복해야하는 횟수에 대해서 계산하는 공식은 다음과 같다. <br>
![loop](img/BestLoop.jpg)<br>

## 장점
+ RANSAC이 성공된다면 성공적으로 Dataset에서 Outlier를 제거할 수 있다. 
+ Inlier만으로 추론한다음에 Outlier를 제거할 수 있다. 
+ 전체 프로세스 시간을 예측할 수 있다. 
+ 이해하기 쉬움

## 단점
+ 랜덤하게 이루어지기 때문에 결과가 매번 바뀔 수 있다. 
  + 랜덤 시드 기능이 필요하다. 
+ Inlier보다 Outlier가 더 많다면 실행 시간이 매우 길어진다. 
+ RANSAC을 하게되면 모든 가능성에 대해서 순회해야한다. 
+ 하나에 데이터셋에서 여러개의 모델을 추출할 수 없다. 

# Modern RANSACs
> 동시 다중 모델 추론은 불가능하다. 하지만 단점으로 뽑힌 사항들을 개선한 것이다. 

+ Early stop method
  + Set minimum iteration
  + Set maximum iteration
  + Success score
+ PROSAC
  + Uses descriptor distance as prior
    + Lower distance = Similar descriptors
    + Similar descriptors = Better match
    + Better match = More Likely to be inliers
  + Progrssively increase search pool
  + Converge to performance of Standard RANSACS it was worse

+ PROSACs algorithm
  1. Descriptor matching 실시
  2. descriptor distance를 계산 (1번을 실행하며)
  3. 오름차순으로 데이터를 정렬
  4. pool number n을 검색하는 초기 값을 설정한다. 
  5. 상위 n개의 data Sample한다. 
  6. Sample data를 통해 모델을 추정한다. 
  7. Score를 측정한다. 지금까지 나온 Best Score보다 좋으면 Score를 갱신, 좋지않으면 n의 범위를 늘려 Search를 진행한다. 
  8. 5번으로 돌아간다.

+ Lo-RANSACs
  + inlier data의 패턴은 굉장히 뭉쳐있고 Outlier는 산개되어있다. 
  + inlier data로만 모델을 추정하여 성공한다면 주변 데이터에 정답이 있다고 판단하는 것이다. 
  + Cost fine Approach
+ Lo-RANSACs algorithms
  1. 최소 데이터 셋을 샘플링함
  2. 모델을 추론하고 평가한다. 
  3. 모델의 스코어 보다 안좋으면 1번으로 돌아간다. 좋다면 inlier데이터 중에 다시 최소단위 데이터 샘플링을 진행한다. 
  4. 이 모델을 평가하고 3번의 방식대로 진행한다. 만일 최대 루프수에 도달했다면 다음 단계로 진행한다. 
  5. local optimization을 반복적으로 진행한다. 
  6. 1번으로 돌아간다. 
