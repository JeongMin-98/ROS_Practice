# Docker CLI

+ docker daemon과 통신하여 기능ㄹ을 수행
+ docker group이 supplementary group에 포함시켜야 사용이 가능
+ usermod로 유저를 그룹에 추가할 수 있다. 

```bash
whoami
sudo usermod -aG docker userid
id # runtime
id userid # configured
```
+ 그룹 추가 후에는 session을 재생성해야 groups 정보를 다시 읽는다. 
+ ubuntu는 재로그인으로는 groups가 반영되지 않는다. 그룹 반영은 gdm을 재실행하므로 다음과 같이 실행한다. 

1. X window에서 로그아웃
2. CTRL-ALT-F4를 눌러서 tty4로 이동한 뒤에 console에 root로 로그인한다. 
3. systemctl restart gdm
4. X window 로그인 CTRL-ALT-F1

## ps
```bash
docker ps
docker ps -a
```

ps는 기본적으로 작동중인 docker process를 출력한다. 
> -a 옵션을 추가해서 종료된 process 상태로 확인이 가능하다. 

## run 
run은 새롭게 container를 실행하는 명령어

```bash
docker ps -a --format '{{.ID}}' | xargs docker rm

# 서로 다른 터미널에서 docker run을 실행해보자
docker run -it --name ubuntu_top ubuntu "top" "-d 1"

# 이미 생성된 container이기 때문에 명령 실패
docker run -it --name ubuntu_top ubuntu "top" "-d 1"

# 이름은 항상 다르게 생성한다. 
docker run -it --name ubuntu_top2 ubuntu "top" "-d 1" 
# 하지만 서로 다른 컨테이너에서 실행되고 있다. 
```

## exec
기존에 존재하는 container에서 top을 실행하는 명령

```bash
docker exec -it ubuntu_top top "-d 0.2"
```
> 같은 container에 새로운 top을 추가할 수 있다. 

> container에 있는 process들을 종료할 때 1번 프로세스를 종료하면 자동으로 같은 container에 있는 프로세스는 쫒겨난다. 

## binding
container의 자원을 외부와 연결해준다. 
+ 일반적으로 I/O와 storage관련을 연결한다. 

### network
1. port binding: host OS의 port와 container의 port를 바인딩한다. 
2. network: docker network를 사용한다. 





### directory, file, block device

**mounting**
+ nginx에 외부 디렉터리를 mount
+ 웹서버가 사용하는 디렉터리 구조를 알아야 한다. 

```bash
# example nginx docker container 내부 구조 확인하기 
docker run --rm -it nginx bash

# link를 확인하기 위해서는 색깔이 보이는 것이 좋음
[nginx bash]# alias ls='ls --color'

[nginx bash]# ls
conf.d ...

[nginx bash]# cd conf.d/

[nginx bash]# ls
default.conf

[nginx bash]# more default.conf
...

```
+ nginx의 루트 디렉터리를 확인한 다음에 Host OS에 있는 폴더를 containier root directory위치에 Binding할 것이다. 
    ```bash
    docker run --rm -d -p 8080:80/tcp \
    -v [home directory]:[root container]\
    --name nginx_8080 nginx
    ```
> -v 대신 --mount 사용방법을 더 권장하고 있음

```bash
docker run --rm -d -p 8080:80/tcp\
--mount type=bind,src=[home directory],dst=[root container]\
--name nginx_8080 nginx
```

1. mount binding: host OS의 directory를 바인딩한다. 
2. volume: docker volume 저장소를 사용한다. 
3. device: host OS의 device, GPU를 바인딩한다. 

### environment
shell의 환경 변수를 지정한다. 

**Practice**
+ environment variables
  + --env KEY=value
  + --env-file env_file

```bash
docker run --rm -it -e LANG=en_US.utf8 --name ubuntu_bash ubuntu 
```


nginx web server를 실행하기 위해서 80/tcp를 사용한다. 
> ssh => 22
> https => 443

+ nginx contatiner가 사용할 port는 config 에서 확인해볼 수 있다. 
```bash
docker inspect nginx
```
+ config 내용 중에 "Attach stdin ~ stderr"부분은 모두 false로 되어있다. 이렇게 설정되어 있는 이유는 daemon에서 SIGTTIN, SIGTTOUT을 발생시키지 않게 하기 위해서이다. 


**실습**
```bash
# 1번 터미널에서
docker run --rm -p 8080:80/tcp --name nginx_8080 nginx

# --rm Automatically remove the contatiner when it exits
# -p bind port

# 2번 터미널에서
curl 127.0.0.1:8080
```

### detach mode(백그라운드모드에서 실행)
```bash
docker run --rm -d -p 8080:80/tcp --name nginx_8080 nginx
```

## attach, detach
+ docker run -it를 사용하는 경우 (interactive mode, terminal)

> container를 running 상태로 두고 잠시 빠져나올때는 detach를 할 수 있다. 

**detach(escape key sequence)**
  + ^P^Q

**attach**
```bash
docker attach "Name"
```