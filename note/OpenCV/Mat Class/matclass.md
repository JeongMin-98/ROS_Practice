# Mat Class  ���� ����

## Mat::ptr() �Լ� �����
> �־��� ����� ������ ����� �ʵ��� �����ϵ��� ����
```c++
template<typename _Tp> _Tp* Mat::ptr(int y)
```
+ y: ������ �� ��ȣ
+ return value (_Tp* Ÿ������ ĳ���õ�) y�� ���� ���� �ּ�

### ��� ����
```c++
	for (int y = 0; y < mat1.rows; y++){
		uchar* p = mat1.ptr<uchar> y;

		for (int x = 0; x < mat1.cols; x++){
			p[x]++;
		}
	}

```

## ������ �ȼ� �� ����
+ MatIterator \<T\> �ݺ��� ��� ���
  + OpenCV�� Mat Ŭ������ �Բ� ����� �� �ִ� �ݺ��� Ŭ���� ���ø� Matiterator_�� �����Ѵ�. 
  + `Mat::begin() ` �Լ��� ����� ù ��° ���� ��ġ�� ��ȯ
  + `Mat::end()  ` �Լ��� ����� ������ ���� �ٷ� ���� ��ġ�� ��ȯ