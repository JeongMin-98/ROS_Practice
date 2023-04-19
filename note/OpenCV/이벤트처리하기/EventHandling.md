# Ű���� �Է� ���
```c++
int waitKey(int delay = 0);
```

+ delay: �и��� ���� ��� �ð� delay <= 0 �̸� ������ ��ٸ�
+ return value: ���� Ű ��, Ű�� ������ ������ -1

> OpenCV â�� �ϳ��� �־�� ���� �����Ѵ�. 
> isshow() �Լ� ȣ�� �Ŀ� waitKey()�Լ��� ȣ���ؾ� ������ ȭ�鿡 ��Ÿ����.

## �ֿ� Ư�� Ű �ڵ�
+ ESC : 27
+ Enter : 13
+ TAB : 9

# ���콺 �̺�Ʈ ó��
```c++
void setMouseCallback(const  String& winname, MouseCallback onMouse, void* userdate = 0);

```
+ winname : â�̸�
+ onMouse : ���콺 �ݹ� �Լ��� ������ (�Լ� �̸��� �����ϸ� �ȴ�.)
+ userdata �ݹ� �Լ��� ������ ����� ���� ������
```c++
typedef void(*MouseCallback)(int event, int x, int y, int flags, 
                               void* userdata*);

```
+ event: ���콺 �̺�Ʈ ���� MouseEventTypes ���
  + [MouseEventTypes](https://docs.opencv.org/4.x/d0/d90/group__highgui__window__flags.html#ga927593befdddc7e7013602bca9b079b0)
+ x, y: ���콺 �̺�Ʈ �߻� ��ǥ
+ flags: ���콺 �̺�Ʈ �÷���, MouseEventFlags ���,
  + [MouseEventFlags](https://docs.opencv.org/4.x/d0/d90/group__highgui__window__flags.html#gaab4dc057947f70058c80626c9f1c25ce)
+ userdata: setMouseCallback() �Լ����� ������ ����� ���� ������
