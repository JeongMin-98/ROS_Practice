# 키보드 입력 대기
```c++
int waitKey(int delay = 0);
```

+ delay: 밀리초 단위 대기 시간 delay <= 0 이면 무한히 기다림
+ return value: 눌린 키 값, 키가 눌리지 않으면 -1

> OpenCV 창이 하나라도 있어야 정상 동작한다. 
> isshow() 함수 호출 후에 waitKey()함수를 호출해야 영상이 화면에 나타난다.

## 주요 특수 키 코드
+ ESC : 27
+ Enter : 13
+ TAB : 9

# 마우스 이벤트 처리
```c++
void setMouseCallback(const  String& winname, MouseCallback onMouse, void* userdate = 0);

```
+ winname : 창이름
+ onMouse : 마우스 콜백 함수의 포인터 (함수 이름을 지정하면 된다.)
+ userdata 콜백 함수에 전달할 사용자 지정 데이터
```c++
typedef void(*MouseCallback)(int event, int x, int y, int flags, 
                               void* userdata*);

```
+ event: 마우스 이벤트 종류 MouseEventTypes 상수
  + [MouseEventTypes](https://docs.opencv.org/4.x/d0/d90/group__highgui__window__flags.html#ga927593befdddc7e7013602bca9b079b0)
+ x, y: 마우스 이벤트 발생 좌표
+ flags: 마우스 이벤트 플래그, MouseEventFlags 상수,
  + [MouseEventFlags](https://docs.opencv.org/4.x/d0/d90/group__highgui__window__flags.html#gaab4dc057947f70058c80626c9f1c25ce)
+ userdata: setMouseCallback() 함수에서 지정한 사용자 지정 데이터
