# image classification
어떤 이미지에 대해서 사전에 정의된 레이블에 맞는 클래스를 내놓는 것

CNN 모델이 이미지 분류 모델에 주로 사용된다. 

+ CNN 모델의 특징
  + Convolution
  + Pooling
  + Fully Connected
  + A clkass of Artificial NN
  + Multi-layers


## MNIST

**Prepare coding environment**

**Ubuntu**
1. Install Docker on Ubuntu(19.03 이상)
2. Install nvidia-container toolkit to use NGC
   + [NGC install guide 참고](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installation-guide)
3. Pull the docker image
   ```bash
   docker pull nvcr.io/nvidia/pytorch:21.12-py3
   ```
4. Make docker container
   ```bash
   docker run -it --gpus "device-0" -v /media/hdd/dmin:/damin --name "damin_torch" nvcr.io/nvidia/pytorch:21.12-py3 /bin/bash
   ```

**Windows**
Docker 대신 anaconda 사용
1. Create Virtual environment
   ```bash
   conda create -n pytortch_py38 python=3.8
   ```
2. Activate environment
   ```bash
   activate python_py38
   ```
3. Install PyTorch

