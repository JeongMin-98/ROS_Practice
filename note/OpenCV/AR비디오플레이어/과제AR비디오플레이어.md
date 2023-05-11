# 과제

사용환경
+ Visual Studio 2019
+ OpenCV 4.5.5

## AR비디오 플레이어란?
카메라 프레임에 특정 영상이 나타나면 해당 위치에 동영상을 재생하는 기능
+ Camera Input + Video File = AR player

## 구현 기능

> 과제에서는 이 AR 비디오 플레이어의 기능을 구현할 것이다. 

+ 기준 영상과 카메라 프레임 사이의 특징점 검출 및 매칭
+ 호모그래피 계산
+ 동영상 프레임 투시 변환 & 합성 `copyTo()` 이용

## 구현 방법
1. Reference Image에 대해서 특징점과 기술자를 한번 만 계산
2. 카메라 프레임에 대해서 특징점 검출한다. 
3. 카메라 프레임과 Reference Image 특징점을 매칭해서 호모그래피를 계산한다. 
4. 호모 그래피를 적용한다. `WarpPerspective()`를 사용
5. Warped VideoFrame을 Camera Frame으로 합성
6. Mask를 지정해서 합성 1280 720


+ ORB, SHIFT 사용

### 호모그래피 정상 계산 확인 방법
findHomography() 함수가 반환하는 mask행렬이 정상치 매칭 결과를 가지고 있음
+ mask행렬에서 정상치 매칭 개수가 특정 임계값보다 크면 호모그래피 계산이 정상적으로 수행되었다고 간주할 수 있음

```cpp
Mat inliers;
Mat H = findHomography(ptsSrc, ptsDst, RANSAC, 3.0, inliers);

int inlier_cnt = countNonZero(inliers);

if (inlier_cnt > 30){
    // 호모그래피가 정상적으로 계산된 경우
}
```

