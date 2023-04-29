# Opencv ���� ���α׷���

## ���� ó��
+ python���� �� �ȼ� ������ ����Ǵ� ��� ���� ���귮�� �ð��� �ɸ���. 
+ c++ ������ �޸� ������ �����ϱ� ������ �����

> �Ϲ����� ���¿����� core cpu ����� 1���� �ִ�. 

������ ������ �������� ������ ������ ó���ϴ� ���

+ �ڵ� ���������� y��ǥ�� ������ ���� �� ������


**OpenCV���� �����ϴ� ���� ���α׷��� ���**
+ Intel TBB (Linux���� ����ص� ������. )
+ HPX
+ OpenMP
+ APPLE GCD
+ Windows RT concurrency
+ Windows concurrency
+ Pthreads (Linux)

### ���� ó���� for ����
```cpp
void parallel_for_(const Range& range, const ParallelLoopBody& body, double nstripes=-1.);
```
+ range: ���� ó���� ������ ����
  + start, end �������� ������ �ִ� class 
  + start ����
  + end �������� ����
+ body: �Լ� ��ü. ParallelLoopBody Ŭ������ ��ӹ��� Ŭ���� �Ǵ� C++11 ���� ǥ����

> ���������� code�� ���󰡴ٺ��� concurrency�� parellel_for�� �̿��ϰ� �Ǵµ� �̰��� parellel_for�� wrapper �����̴�. 

#### ParallelLoopBody
ParallelContarst +> ParallelLoopBody ����ϴ� ���� ¥���Ѵ�. 

+ ������ => ��� ���� �ʱ�ȭ
+ operator () ������
+ operator = ������
    ```cpp
    ParallelContrast& operator =(const ParallelContrast &){
        return *this;
    };

    ```

��� ����
```cpp
int main()
{
    Mat src = imread("hongkong.jpg", IMREAD_GRAYSCAEL);
    Mat dst;

    parallel_for_(Range(0, src.rows), ParallelContrast(src, dst, 1.f));
}

```
#### lambda expression


# Lookup Table(LUT)
+ Ư�� ���꿡 ���� �̸� ��� ���� ����Ͽ� �迭������ ������ ���°�
+ �ȼ� ���� �����ϴ� ��� 256 X 1ũ���� uchar ��Ŀ� �ȼ� �� ��ȯ ���� ��� ���� �̸� �����Ѵ�. 
+ ���� ��� �ȼ��� ���� ���� ������ �����ϴ� ��� ��� ���� �����Ͽ� ��� ���� �ȼ� ���� �����Ѵ�. 

```cpp
void LUT(InputArray src, InputArray lut, OutputArray dst);

```
+ src �Է¿���
+ lut LUT ���̺�
+ dst ��� ����