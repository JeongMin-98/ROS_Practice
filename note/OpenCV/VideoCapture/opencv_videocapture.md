# ī�޶� ����
```c++
videoCapture::VideoCapture(int index, int apiPreference = CAP_ANY);
```

+ carmera_id => 0�� ����
+ ���� ���� ī�޶� ����Ǿ� ������ 0, 1, ... ������ ����
+ apiPreference => default�� �����Ѵ�. 
  + ������ ��� default������ �����Ͽ� ����Ѵ�. 

+ return value => VideoCapture �����ڴ� videocapture ��ü�� ��ȯ 
+ Open�Լ��� ��� �۾��� �����ϸ� true, �����ϸ� false��ȯ

# ������ ���� ����
```c++
videoCapture::VideoCapture(const String& filename, int apiPreference = CAP_ANY);

```
+ ���� ���� => video.avi
+ ���� ���� ������ => img_%02d.jpeg
+ ���� ��Ʈ�� URL

+ ��ȯ���� �� ī�޶� ���� ��ü�� ����

# VideoCapture Open method
+ Open�� �����ϸ� read method�� ���ؼ� ���� �� ����
+ operator >> �����ڸ� ����Ͽ� ����

> ���� �鿡���� ū ���� ���� �������̽��� ����

# ������ �����ϱ�

## VideoWriter
```c++
VideoWriter::VideoWriter(const String& filename, int fourcc, double fps, Size frameSize,
                        bool isColor = true)

```
+ filename: ������ ������ ���� �̸�
+ fourcc => ������ ����� ��Ÿ���� 4���� ���� (http://www.fourcc.org/codes.php)
+ fpg: �ʴ� ������ ��
+ frameSize: ���� ������ ũ��
+ isColor: �÷� ������ �÷���, false�� �����ϸ� GrayScale������ ���������� �����