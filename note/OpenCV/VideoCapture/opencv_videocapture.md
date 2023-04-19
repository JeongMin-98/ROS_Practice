# 카메라 열기
```c++
videoCapture::VideoCapture(int index, int apiPreference = CAP_ANY);
```

+ carmera_id => 0을 지정
+ 여러 대의 카메라가 연결되어 있으면 0, 1, ... 순서로 지정
+ apiPreference => default로 지정한다. 
  + 보통의 경우 default값으로 지정하여 사용한다. 

+ return value => VideoCapture 생성자는 videocapture 객체를 반환 
+ Open함수의 경우 작업이 성공하면 true, 실패하면 false반환

# 동영상 파일 열기
```c++
videoCapture::VideoCapture(const String& filename, int apiPreference = CAP_ANY);

```
+ 비디오 파일 => video.avi
+ 정지 영상 시퀀스 => img_%02d.jpeg
+ 비디오 스트림 URL

+ 반환값은 위 카메라 열기 객체와 동일

# VideoCapture Open method
+ Open을 성공하면 read method를 통해서 읽을 수 있음
+ operator >> 연산자를 사용하여 가능

> 성능 면에서는 큰 차이 없음 인터페이스만 변경

# 동영상 저장하기

## VideoWriter
```c++
VideoWriter::VideoWriter(const String& filename, int fourcc, double fps, Size frameSize,
                        bool isColor = true)

```
+ filename: 저장할 동영상 파일 이름
+ fourcc => 압축할 방식을 나타내는 4개의 문자 (http://www.fourcc.org/codes.php)
+ fpg: 초당 프레임 수
+ frameSize: 비디오 프레임 크기
+ isColor: 컬러 동영상 플래그, false로 지정하면 GrayScale형태의 동영사으로 저장됨