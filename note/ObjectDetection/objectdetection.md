# Object Detection
> ��ü �з�, ����, ���� �ϴ� ���� ���̴� �����ϱ�?
+ classification(�з�): �̹����� ��ü�� �������� �˾Ƴ��� ��.
  + ��ü �з��ܰ迡���� �̹��� �����Ͱ� CNN �� ���̾ ����ϰ� ��� ������ N���� Ȯ�� ������ ������ ��
+ localization(����): �̹����� �ϳ��� ��ü�� ��� �ְ�, �������� �˾Ƴ��� ��
  + �з� �ܰ迡�� CNN���� ����Ͽ� ���ġ�� Ȯ�������� 
  Ŭ���� ���� ������ �Ϳ� �߰��Ͽ� ��ü ��ġ�� ���� ������ �޴� 
  �ٿ���ڽ��� ���� ������ ���� ��ȯ�Ѵ�. 
+ detection(Ž��): �̹������� �������� ��ü�� ���� ��� �ְ�, 
�������� �˾Ƴ��� ��


> �̷� �з�, ���� ������� �����Ͽ� ������ ���� ������� �������� 
��ü Ž���� �ϰ��� �ߴ�. 

+ Sliding Window method
  + �ټ��� ��ü ������ ����
  + ��ǻ�� ���귮�� �ſ� ����, ��ȿ�����̴�. 
  + �ϳ��� �̹������� �ʹ� ���� ������ �ϰ� �ȴ�. 
  + ��ü�� ũ�Ⱑ ū�� ������ �� �� ���� ������ Window�� ũ�⸦ Ư�� �� �� ������. 

+ Classifier + Regressor
  + �������� ������ �ٿ�� �ڽ� ������ Regressor�� ���� �и��Ͽ� ����� ������
  + �������� ��ü�� ���� ������ ���´ٸ� �� ������ Box������ �ڷᱸ���� ���� ���´�.

> �Ϲ����� �з� �𵨰� Ž�� ���� ���̴� �����ϱ�?
+ �з� ��
  + ���� ���� ������ �����鼭 resolution�Ǹ鼭 layer�� ũ�Ⱑ �۾�����. 
  + �ᱹ ���ܿ��� Fully Connected�� ���Ͽ� �ϳ��� ����� ������ �ȴ�. 
  + Fully Connected�� ���� 2D feature layer�� 1D feature map���� �ٲ۴�.
+ Ž�� �� (YOLOv1)
  + �з� �𵨰� ���� ���� ������ ��������� ���� �κп��� �ٸ���.
  + 2D feature map�� ���¸� �״�� ������ ����� ������ �ȴ�. 
    + �ֳ��ϸ� ���������� �� �� �ֵ��� �ؾߵȴ�.

## One stage Detection & Two stage Detection
Object Detection�� �ΰ��� ������� ��������. 
+ �ش� ���� ��Ű��ü�� ���� �з��ȴ�. 

### One stage Detection
�ѹ��� Feed-Fowarding�� ���� ����� ����. 

**architecture**
![architecture](https://pbs.twimg.com/media/FCtkDKvXIAQe1H0.jpg:large)
1. Backbone: �̹����� Ư¡�� �����ϴ� �ܰ�
2. Neck: �������� �̹��� Ư¡�� �̾Ƴ� ���� �ٸ� resolution feature map�� �����Ѵ�. 
   + Neck �ܰ迡�� feature maps ���� �����ϴ� ��������� resolution�� �����ϰ� �������Ѵ�.
   + �����ϴ� ����� �� ������ �ִ�. 
     1. Concat: ���� �ٸ� featuremap���� ���� �޴�, �մܿ� �ٴ´�.
     2. add: ä�� ���� ������ ��� ���� �ٸ� element������ ���Ѵ�.
3. Dense Prediction: Bounding Box�� ��ü�� ���� score�� ����
> Dense Prediction�� ������ ������� �������� feature map���� ����� ���� �� ������ ����ؾ���.
### Many stage Detection
![two_architecture](https://pbs.twimg.com/media/FCtkDKvXIAQe1H0?format=jpg&name=small)
���� �ܰ��� Feed-Fowarding�� ���� ����� ����. 
+ Faster-RCNN
  + ���� ù ��° �ܰ迡�� Feed-Fowarding�� ���� ��ü�� ������ ���� ������ �����Ѵ�. 
  + �� ��° �𵨿����� �ش� ��ü�� ���� (ROI)���� ��ü�� ��ġ ������ �������ϰ� �з��Ѵ�. 
  
## Grid
> Obeject Dection������ grid cell���� ��ü�� �����Ѵ�. 
+ feature map�� Pixel�� ���̴�. 

+ �Ѱ��� �׸��� �ȿ��� 3���� BOX�� �����. �ش� �ڽ��ȿ��� ������ ���� �Ӽ��� �����.
  + Box to coordinates
  + objectness score
  + class scores (C���� class�� ���� ����)

## Anchor
![Anchor](https://machinethink.net/images/object-detection/anchors.png)
��Ŀ�� �Ǵٸ� ���ѿ�Ҹ� �߰������ν� ���� ���� �� ������ ���ϰ� ����� �����ϰ��� �ϴ� ��ü�� ����� �����Ѵ�.
+ Feature map�ȿ��� ��ü�� ���� ������ ������ �� �� ����Ѵ�. 
+ �Ѱ��� ��ü �� �ϳ��� ��Ŀ�� �Ҵ�ȴ�. 
+ �ڽ� �ϳ��� �ϳ��� ��Ŀ�� �Ҵ��.

> � ��ü�� ���ؼ� ũ�⸦ ������ �� ���� ������ ũ�Ⱑ �پ��� �ٿ�� �ڽ��� �����.
> �ش� �ٿ�� �ڽ��� ��Ŀ��� �����ص� ����.

## How to find the object
Bounding box, objectness score and class score�� ����Ͽ� ��ü�� Ž���Ѵ�.
+ Objectness score: Bounding Box�ȿ��� ���ԵǾ��ִ� ��ü�� ���ؼ� Ȯ���� ��Ÿ���� ���̴�. 
  + �� ���� �ش�Ǵ� ��� Ŭ������ ���� ��ü�� ���� Ȯ���� ���� �ȴ�. 1�� 0���� ��Ÿ����. 
+ Class score: Ŭ���� ���� ��ü�� ���� Ȯ�� ��


## Softmax
![softmax](https://miro.medium.com/v2/resize:fit:720/format:webp/1*ReYpdIZ3ZSAPb2W8cJpkBg.jpeg)
�� ������ Ŭ������ ���ؼ� �ջ� 1�� ����� �� �ȿ� probability ���� �����Ѵ�. 
+ ū ���� �ش�ȭ ���� ���� �ּ�ȭ �����ش�. 

## [Cross-entropy loss](https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e)
![Cross-entorpy](https://miro.medium.com/v2/resize:fit:640/format:webp/1*rcvGMOuWLMpnNvJ3Oj7fPA.jpeg)
> cross-entropy�� ���� ��������� �����ϸ�ȴ�. �� ����ȴٸ� ���� �������� �� �� ����ȴٸ� ū �������� ����.

## [Non-Max Suppression](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c)
�� ������ ��ġ�� ������ �ٿ�� �ڽ��� ������ ǥ�õɰ��̴�. �׷��� ������ �� ������ �����Ͽ� ��ü ���¿� ���� ������ ��ġ�Ǵ� �ٿ�� �ڽ��� �����Ѵ�. 

## evaluation metric
![metric](https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/63528aff738b370197906164_Precision%2C%20recall.png)
+ Precision: ������ ������� ���ؼ� ������ ������� �˸°� ����� ���� �ǹ���.
+ Recall: ��ü ���䰪 �߿� ������ �����ؼ� ���� ����

  + TP(True Positive): ���� ���� => �����Ͽ��µ� ���� ��� ��
  + FP(False Positivie): Ʋ�� ���� => �����Ͽ��µ� Ʋ�� ��
  + FN(False Negative): �̰����� ������ => ������ �Ǿ�� �ϴµ� ������ �ȵ� ���
  + TN(True Negative): �̰����� Ʋ���� => ������� �ʾƾ��ϴ� ���� ������ �ȵ� ���

> object detection������ IoU�� ����Ѵ�. 

![f1 score](https://velog.velcdn.com/images%2Fjadon%2Fpost%2Ff06f1d40-605d-4f13-b6ce-35c220c82968%2Fimage.png)
+ F1 Score: Precision�� recall�� ����Ͽ� ���� ���ϸ� ���� ����� �ƴϱ� ������ �ΰ��� ��츦 ȥ���Ͽ� ����Ѵ�.

> Precision�� recall���� ������谡 �����Ѵ�. 

1. high recall + high precision: ���� ������ �ſ� ���� ���(���ϴ� ���� ����Ȱ�)
2. low recall + high precision: ��ü ������ �� �̷������ ���� ����̴�. �����ߴµ� ��ü�� ��ģ���̴�.
3. high recall + low precision: �ٿ�� �ڽ��� �� ���������� �ٸ� Ŭ������ �ִ� ������ ��ü�� Ž���ϴ� ���
4. low recall + low precision: ���� ������ �ſ� �������� ��� (�ƹ��� ��ü Ž���� ����)
