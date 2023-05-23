# chroot 
+ root dir.를 특정 디렉터리로 변경
+ UNIX command 및 system call로 존재

> root directory를 변경하는 기능을 활용하여 프로세스마다 다른 mount 구조를 가지게 한다. 

## 보안적 측면의 격리
> sandbox의 개념
+ chroot로 격리된 directory hierarachy를 통해 경로를 속일 수 있음
+ 동일한 프로그램을 쉽게 다른 환경으로 복제할 수 도 있다. 

```bash
sudo apt -y install vsftpd

# 시스템 서비스 running확인 
sudo systemctl is-active vsftpd
sudo systemctl start vsftpd

# filezilla 설치 
sudo apt -y install filezilla
```


### practice : chroot : vsftpd

+ ftpd의 설정 변경
```bash
sudo vim /etc/vsftpd.conf

/chroot
# add
chroot_local_user=YES
allow_writeable_chroot=YES
```
+ 설정 저장한 뒤에 vsftpd를 재시작
```bash
sudo systemctl restart vsftpd
sudo systemctl status vsftpd
```

> rescue 모드 부팅에서 사용된다. chroot가 성공하면 /mnt가 새로운 root가 되므로 B로 부팅했지만, A시스템이 된다. 설치과정과 비슷하다. 

# Isolation
+ 격리의 필요성
  + 시스템 내에 존재하는 자원은 한정적이다. 

+ Process의 scope를 생각
  + 현대적인 OS는 프로세스가 독립적 공간을 가지게 해준다. 
  + 프로세스가 고유한 공간을 받을 수 있지만 외부 통신을 위해서 IPC를 사용해 I/O 비용이 높아진다. 

> 이러한 경우에 여러 프로세스가 협동해야 하는 프로그램에서는 단점이 더 커진다. 

## 보안,자원 관리적 측면
+ 특정 파일 경로의 접근을 제한
  + ftp 프로세스가 /home/ftp 디렉터리 이하에서만 이동할 수 있도록 한다. 이것은 chroot를 사용
  + 호스팅 업체라면 고성능 컴퓨터 1대로 여러 사업자에게 DB나 웹을 제공 가능하다. 

## 호환, 충돌 측면
+ 동일한 디렉터리를 사용하는 프로세스는 독립된 실행을 어떻게 가능한지
+ 서로 다른 버전의 파일을 사용하는 프로세스가 있다면? 이때 Isolation을 활용한다. 

## Namespace
+ 분산 컴퓨팅 시스템으로서 local, remote를 hieracachical file system으로 표현 가능
+ 디렉터리가 계층 구조로 이뤄어져 있어서 isolation이 가능하다. 



+ mount, UTS, IPC, network, PID, user, cgroup
+ binary
  + unshare, lsns

### practice
```bash
unshare -pf --mount-proc /bin/bash
ps
exit
```

### Cgroup
OS level abstraction을 가지고 있고 group별로 가상화된 공간을 만들고 자원을 제약할 수 있게 된다. 

> docker, hadoop, systemd 등 수많은 프로젝트가 cgroup 기반으로 만들어진다. 

### LXC
+ Linux Contatiner
  + 초창기 리눅스 컨테이너 기술의 발판
  + docker도 초창기에는 lxc를 사용 지금은 다른걸 사용

### docker
+ container runtime
+ OCI 표준화를 잘 따르고 있다. 
+ Contatiner를 세련된 방식으로 구현한 제품의 일종
+ 격리된 자원의 묶음과 런타임으로 구성되어있음
+ 기본적으로 C/S 구조를 가지므로 daemon이 작동한다. 
+ HOST OS위에서 작동하는 격리된 프로세스의 일종이기 때문에 Memory, File System의 I/O에서 발생되는 심각한 overhead가 없다. 

> 단점으로 daemon으로 작동하면서 child process로 수직관리가 되고 관리자 권한을 사용하기때문에 보안 측면에서 좋지않을 수 있지만 사용은 많이 되고 있다. 

> 안정성 문제


### podman
> alternative of linux contaainer
+ docker의 단점과 상용화 문제로 인해 대체제로 사용
+ no daemon service, no admin account
+ systemd unit support

### Virtualization
+ Full virtualization 사용
  + 소프트웨어로 가상화된 하드웨어를 구현
  + 완전히 격리된 공간을 제공한다. 
  + 격리의 일종이다. 
  + 보안 문제, 호환성 문제를 거의 대부분 해결할 수 있음

+ 단점
  + 낮은 성능
  + 독점적인 자원 점유
  + Host-Guest 간의 자원 교환의 어려움 및 비효율

### Sandbox
+ 다양한 방법으로 구현이 가능하다. 
+ 테스트 유닛으로서 격리된 공간, 보안 공간, 복제된 서비스 공간을 제공한다. 
+ vm머신을 설치했다가 통채로 지우는게 더 깔끔하지 않을까?

> 위와 같은 단점을 해결하기 위해서 Container를 사용한다. 