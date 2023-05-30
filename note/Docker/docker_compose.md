# Docker compose
여러 개의 container를 띄울 때 사용할 수 있다. 
config 파일을 만들어서 실행시킨다. 

+ config : Yaml file type
+ default filename : docker-compse.yml

+ 다른 파일 명을 사용하고 싶을 때는 -f 플래그를 사용한다. 

> Build or rebuilds, creates, starts 기능을 제공한다. 

특정 디렉터리를 만들어서 데이터 디렉터리를 만드는 것이 좋다. 
+ 서비스 특징, 명 디렉터리를 만드는 것이 편리하다. 

```bash
mkdir ~/docker-compose
cd ~/docker-compose
```
> yaml 파일 형식은 indentation, space에 주의해야한다. 

yaml을 만들어 놓은 해당 디렉터리에서 실행시키면 자동으로 yaml파일을 읽어들이면서 작동한다. 

```bash
docker-compose up
```

**detach mode**
```bash
docker-compose up -d
```

