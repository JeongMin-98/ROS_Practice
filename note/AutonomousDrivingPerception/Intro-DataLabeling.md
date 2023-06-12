# Data Labeling

**데이터 처리 과정**
<br>
1. Raw Data 
2. Labeling Raw Data
3. Labeled Data
4. DataSet

+ Labeling은 확보한 원시 데이터를 유의미한 작업에 사용하도록 데이터를 만드는 작업이다.
+ Labeling은 Annotation, Tagging이라고도 부른다.
+ 학습에 필요한 데이터를 생성하는 과정이라고 생각하면된다.

> 컴퓨터 비전에서는 사람들이 주로 이미지에 필요한 작업에대해서 결과를 미리 입력하고 이를 바탕으로 모델이 학습한다.

+ classification은 이미지에 해당하는 클래스 정볼를 미리 입력한다. 
+ Detection도 이미지에 대해 객체의 BBox와 클래스 정보를 입력한다. 

> Annotation 툴은 다룰 줄 알아야한다.

이러한 과정에 따라 생성된 데이터는 최대 검출(또는 분류) 성능이 될 수 있고, 또 다른 데이터를 만들어 내는 재료가 된다.
<br>
따라서 데이터를 잘 생성하는 것은 매우 중요하고 잘못된 모델을 사용하는 것은 모델 성능에 많은 영향을 미친다.

> 현실 상에 데이터는 여러가지 환경에 따라 데이터가 모두 다를 수 있다. 따라서 학습 데이터를 직접 만드는 것이 중요하다.


데이터 레이블링 툴은 많다. 
+ 공개 툴로는 CVAT, labelme, labelmg

## CVAT
> Labeling 데이터 배포 시 다양한 포맷의 데이터로 변환이 가능하다. 

docker를 통해서도 설치가 가능하다.
[CVAT 설치 링크](https://opencv.github.io/cvat/docs/administration/basics/installation/#windows-10)
> 설치과정은 위 링크를 참고하여 진행하면 된다.

### Install
**Windows**환경에서 진행할 때 <br>
1. WSL2 설치한다. (자신의 Windows환경이 요구사항에 맞는 지 확인)
2. [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)을 설치
3. Docker Desktop에서 WSL환경이 모두 잘 설정되어있는 지 확인
4. Git, Chrome이 설치되어있지 않으면 설치
5. Windows메뉴에 WSL2 설치 이후에 설치되어있는 리눅스 배포판을 클릭
6. Linux 배포판 cmd창에서 다음과 같은 명령어 입력
    ```commandline
    git clone https://github.com/opencv/cvat
    cd cvat
    ```
7. Docker container를 실행
    ```commandline
    docker compose up -d
    ```
    ```commandline
    (optional) CVAT_VERSION=dev docker compose up -d
    ```
8. 최종 권한 설정
    ```commandline
    sudo docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
    ```
9.  localhost:8080 실행

### 작업 단위
보통 작업 단위는 3단계로 나눠져있다. 
+ Projects
  + tasks
    + job

### 작업 방법
+ Task를 만들 때 다양한 옵션을 지정할 수 있다. 
+ Labels: 원하는 클래스를 원하는 색상으로 추가 가능
+ select files: 이미지를 업로드하여 labeling 작업이 가능
+ Advanced configuration: 이미지 압축등 세부 설정 가능

> Task는 여러개의 Job을 가지고 있는데, Job은 Task 생성 시 설정한 이미지 개수로 생성된다.
