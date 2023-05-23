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

