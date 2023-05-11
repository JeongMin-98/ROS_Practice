# CUDA
> 그래픽 처리 장치에서 수행하는 알고리즘을 C프로그래밍 언어를 비롯한 산업 표준언어를 사용하여 작성할 수 있도록 하는 GPGPU 기술이다.

+ CUDA를 enalbe해서 Opencv 빌드하기
  1. CUDA Toolkit 설치
  2. CUDNN 설치
  3. OpenCV 소스 코드 다운로드
    + Contribute, 메인 모듈 둘 다 다운
  4. CMAKE 프로그램 설정
    + Opencv 메인 빌드 폴더 설정
    + Contribute는 OPENCV_EXTRA_MOBULES_PATH로 설정
      + cotrib/modules 로 폴더 설정
    + 옵션에서 WITH_CUDA를 추가
    + WITH_CUDNN 선택
  5. 전체 솔루션 빌드
  6. Install 프로젝트 빌드
  7. 릴리즈, 디버그 모드에 대해서 빌드 수행
  8. 환경 변수 설정=> 직접 빌드하고 나서는 install아래에서 설정
  9. 17\bin으로 설정
  10. opencv_version이 되었는 지 확인


# OpenCL
+ 여러 개의 CPU, GPU, DSP등의 프로세서로 이루어진 이종 플랫폼에서 동작하는 프로그램 코드 작성을 위한 개방형 범용 병렬 컴퓨팅 프레임워크이다.
+ 