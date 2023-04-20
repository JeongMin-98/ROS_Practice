# Opencv 기능

## 연산 시간 측정 방법
+ TickMeter 클래스
	+ 연산 시간 측정을 위한 직관적인 인터페이스 제공
```cpp
class TickMeter
{
public:
	TickMeter(); // generator

	void start();
	void stop();
	void reset();

	double getTimeMicro() const; //micro sec
	double getTimeMilli() const; // milli sec
	double getTimeSec() const; // sec
}
```

사용 예제

```cpp
TickMeter tm;
tm.strat();

func1();

tm.stop();

cout << "func1(): " << tm.getTimeMilli() << "ms." << endl;

tm.reset();
tm.start();

func2();
tm.stop();

cout << "func2(): " << tm.getTimeMilli() << "ms. " << endl;
```

## Mask 연산과 ROI(Region of Interest)
+ 마스크 연산을 지원하는 픽셀 값 복사 함수
```cpp
void Mat::copyTo(InputArray m, InputArray mask) const;
```

+ m: 출력영상 => 크기 밎 타입이 같은 m을 입력으로 지정하면 새로 생성하지 않고 연산을 수행한다. 
+ mask: 마스크 연산 0이 아닌 픽셀에 대해서만 복사 연산을 수행한다. 

+ 전역함수 형식
```cpp
void copyTo(InputArray src, OutputArray dst, InputArray mask);
```
### 관심영역(ROI)
영상에서 특정 연산을 수행하고자 하는 임의의 부분 영역

### 마스크 연산
일부 함수에 대해 ROI연산을 지원한다. 이때 마스크 영상을 인자로 함꼐 전달해야한다. 
> 마스크 영상은 CV_8UC1타입의 영상이다. 

> 마스크 영상은 픽셀값이 0이 아닌 위치에서만 영상이 수행된다. 
+ 보통 마스크 영상으로는 0또는 255로 구성된 이진 영상을 사용한다. 


