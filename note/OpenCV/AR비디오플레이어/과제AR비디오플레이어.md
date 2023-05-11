# ����

���ȯ��
+ Visual Studio 2019
+ OpenCV 4.5.5

## AR���� �÷��̾��?
ī�޶� �����ӿ� Ư�� ������ ��Ÿ���� �ش� ��ġ�� �������� ����ϴ� ���
+ Camera Input + Video File = AR player

## ���� ���

> ���������� �� AR ���� �÷��̾��� ����� ������ ���̴�. 

+ ���� ����� ī�޶� ������ ������ Ư¡�� ���� �� ��Ī
+ ȣ��׷��� ���
+ ������ ������ ���� ��ȯ & �ռ� `copyTo()` �̿�

## ���� ���
1. Reference Image�� ���ؼ� Ư¡���� ����ڸ� �ѹ� �� ���
2. ī�޶� �����ӿ� ���ؼ� Ư¡�� �����Ѵ�. 
3. ī�޶� �����Ӱ� Reference Image Ư¡���� ��Ī�ؼ� ȣ��׷��Ǹ� ����Ѵ�. 
4. ȣ�� �׷��Ǹ� �����Ѵ�. `WarpPerspective()`�� ���
5. Warped VideoFrame�� Camera Frame���� �ռ�
6. Mask�� �����ؼ� �ռ� 1280 720


+ ORB, SHIFT ���

### ȣ��׷��� ���� ��� Ȯ�� ���
findHomography() �Լ��� ��ȯ�ϴ� mask����� ����ġ ��Ī ����� ������ ����
+ mask��Ŀ��� ����ġ ��Ī ������ Ư�� �Ӱ谪���� ũ�� ȣ��׷��� ����� ���������� ����Ǿ��ٰ� ������ �� ����

```cpp
Mat inliers;
Mat H = findHomography(ptsSrc, ptsDst, RANSAC, 3.0, inliers);

int inlier_cnt = countNonZero(inliers);

if (inlier_cnt > 30){
    // ȣ��׷��ǰ� ���������� ���� ���
}
```

