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