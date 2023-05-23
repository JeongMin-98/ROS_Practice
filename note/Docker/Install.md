> 옛날 버전이 설치되어있다면 제거해야한다. 

```bash
su -
# 설치된 정보를 확인하고 있으면 다 지운다.
sudo apt-get remove docker docker-engine docker.io containerd runc
```

## 저장공간 설정
+ apt package 업데이트
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```

+ keyfile 추가
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
+ 저장소 설정
```bash
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
## install Docker Engine
```bash
sudo apt update
```

최신 버전 설치 방법
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

작동 확인 방법
```bash
sudo docker run hello-world
```


