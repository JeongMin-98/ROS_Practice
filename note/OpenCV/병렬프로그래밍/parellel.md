# Opencv 병렬 프로그래밍

## 병렬 처리
+ python에서 각 픽셀 값에서 실행되는 경우 많은 연산량과 시간이 걸린다. 
+ c++ 에서는 메모리 접근이 용이하기 때문에 사용함

> 일반적인 형태에서는 core cpu 사용이 1개만 있다. 

영상을 일정한 영역으로 나눠서 연산을 처리하는 방법

+ 코드 구현에서는 y좌표로 나누는 것이 더 용이함


**OpenCV에서 지원하는 병렬 프로그래밍 기법**
+ Intel TBB (Linux에서 사용해도 괜찮다. )
+ HPX
+ OpenMP
+ APPLE GCD
+ Windows RT concurrency
+ Windows concurrency
+ Pthreads (Linux)

### 병렬 처리용 for 루프
```cpp
void parallel_for_(const Range& range, const ParallelLoopBody& body, double nstripes=-1.);
```
+ range: 병렬 처리를 수행할 범위
  + start, end 정수값을 가지고 있는 class 
  + start 포함
  + end 포함하지 않음
+ body: 함수 객체. ParallelLoopBody 클래스를 상속받은 클래스 또는 C++11 람다 표현식

> 내부적으로 code를 따라가다보면 concurrency의 parellel_for를 이용하게 되는데 이것은 parellel_for의 wrapper 형태이다. 

#### ParallelLoopBody
ParallelContarst +> ParallelLoopBody 상속하는 직접 짜야한다. 

+ 생성자 => 멤버 변수 초기화
+ operator () 재정의
+ operator = 재정의
    ```cpp
    ParallelContrast& operator =(const ParallelContrast &){
        return *this;
    };

    ```

사용 예시
```cpp
int main()
{
    Mat src = imread("hongkong.jpg", IMREAD_GRAYSCAEL);
    Mat dst;

    parallel_for_(Range(0, src.rows), ParallelContrast(src, dst, 1.f));
}

```
#### lambda expression


# Lookup Table(LUT)
+ 특정 연산에 대해 미리 결과 값을 계싼하여 배열등으로 저장해 놓는것
+ 픽셀 값을 변경하는 경우 256 X 1크기의 uchar 행렬에 픽셀 값 변환 수식 결과 값을 미리 저장한다. 
+ 실제 모든 픽셀에 대해 실제 연산을 수행하는 대신 행렬 값을 참조하여 결과 영상 픽셀 값을 설정한다. 

```cpp
void LUT(InputArray src, InputArray lut, OutputArray dst);

```
+ src 입력영상
+ lut LUT 테이블
+ dst 출력 영상