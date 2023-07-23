# 딥러닝 모델 학습 프로젝트

## 제한 사항
1. 오픈 데이터를 만들었던 당시에 사용한 센서 구성과 현재 사용하는 센서의 다른 구성
   + 카메라 모델의 내적인 환경, 외적인 환경이 다른 경우
2. 목표에 부합하는 오픈 데이터가 없는 경우
3. 자체적으로 만든 데이터를 이용한 경우에 단발성으로 끝나는 문제 발생
4. 객체를 추가하는 상황에서도 문제가 생김
5. 변경된 목표가 존재하지만 레이블링이 안되는 경우 
6. 변경된 목표가 존재하지 않아서 데이터 자체가 없는 경우

> 데이터 생성을 추가로 해야되는 상황에서는 지속성을 지키도록 하는 방법은 여러가지가 있다. 

## 프로젝트 목표

### 제한사항
> KITTI 데이터 셋에서 "Pedestrian"과 "car" 클래스는 사용하지 않는다. 
> Transfer Learning vs Continual Learning
+ [Continual Learning](https://winnerus.medium.com/ai-%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0-continual-learning-on-deep-learning-16969792acc7)
+ [Transfer Learning](https://dacon.io/en/forum/405988)
