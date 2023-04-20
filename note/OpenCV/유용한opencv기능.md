# Opencv ���

## ���� �ð� ���� ���
+ TickMeter Ŭ����
	+ ���� �ð� ������ ���� �������� �������̽� ����
```cpp
class TickMeter
{
public:
	TickMeter(); // generator

	void start();
	void stop();
	void reset();

	double getTimeMicro() const; //micro sec
	double getTimeMilli() const; // milli sec
	double getTimeSec() const; // sec
}
```

��� ����

```cpp
TickMeter tm;
tm.strat();

func1();

tm.stop();

cout << "func1(): " << tm.getTimeMilli() << "ms." << endl;

tm.reset();
tm.start();

func2();
tm.stop();

cout << "func2(): " << tm.getTimeMilli() << "ms. " << endl;
```

## Mask ����� ROI(Region of Interest)
+ ����ũ ������ �����ϴ� �ȼ� �� ���� �Լ�
```cpp
void Mat::copyTo(InputArray m, InputArray mask) const;
```

+ m: ��¿��� => ũ�� �G Ÿ���� ���� m�� �Է����� �����ϸ� ���� �������� �ʰ� ������ �����Ѵ�. 
+ mask: ����ũ ���� 0�� �ƴ� �ȼ��� ���ؼ��� ���� ������ �����Ѵ�. 

+ �����Լ� ����
```cpp
void copyTo(InputArray src, OutputArray dst, InputArray mask);
```
### ���ɿ���(ROI)
���󿡼� Ư�� ������ �����ϰ��� �ϴ� ������ �κ� ����

### ����ũ ����
�Ϻ� �Լ��� ���� ROI������ �����Ѵ�. �̶� ����ũ ������ ���ڷ� �Բ� �����ؾ��Ѵ�. 
> ����ũ ������ CV_8UC1Ÿ���� �����̴�. 

> ����ũ ������ �ȼ����� 0�� �ƴ� ��ġ������ ������ ����ȴ�. 
+ ���� ����ũ �������δ� 0�Ǵ� 255�� ������ ���� ������ ����Ѵ�. 


