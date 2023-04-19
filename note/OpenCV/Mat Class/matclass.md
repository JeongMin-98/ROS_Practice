# Mat Class  기초 사용법

## Mat::ptr() 함수 사용방법
> 주어진 행렬의 범위를 벗어나지 않도록 주의하도록 하자
```c++
template<typename _Tp> _Tp* Mat::ptr(int y)
```
+ y: 참조할 행 번호
+ return value (_Tp* 타입으로 캐스팅된) y번 행의 시작 주소

### 사용 예제
```c++
	for (int y = 0; y < mat1.rows; y++){
		uchar* p = mat1.ptr<uchar> y;

		for (int x = 0; x < mat1.cols; x++){
			p[x]++;
		}
	}

```

## 영상의 픽셀 값 참조
+ MatIterator \<T\> 반복자 사용 방법
  + OpenCV는 Mat 클래스와 함께 사용할 수 있는 반복자 클래스 템플릿 Matiterator_를 제공한다. 
  + `Mat::begin() ` 함수는 행렬의 첫 번째 원소 위치를 반환
  + `Mat::end()  ` 함수는 행렬의 마지막 원소 바로 다음 위치를 반환