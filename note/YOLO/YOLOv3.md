# YOLOv3

## Architecture
![img](https://res.cloudinary.com/practicaldev/image/fetch/s---OWUOygh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nr5oq1n6ukg89z8e6ytl.png)

## Make model using cfg(config) file
config ������ �̿��Ͽ� ���� �����Ѵ�. 
+ hyperprameters
+ Model architecture
+ Data aughmentation
+ Input resolution
+ ...

�������� �������� ����ִ�. 

## Annotation & configuration

### YOLO format
+ YOLODATA
  + Train
    + a.jpg
    + a.txt
    + b.jpg
    + b.txt
    + ...
  + Eval
  + Test
+ train.list
  + YOLODATA/Train/a.jpg
  + ...
+ eval.list
  + YOLODATA/Eval/c.jpg
  + ...

+ PASCAL VOC FORMAT
![img](img/VOC_FORMAT.PNG)

## Annotation labeling format
![labeling](img/labeling_annotation.png)
YOLO labeling format�� ������ ����
+ Class_index
+ x_center
+ y_center
+ width
+ height
> x, y, w, h�� ������ 0, 1������ ������ ����ȭ�Ǿ��ִ�. 
> �̹� YOLOv3 ���������� Annotation���� XML ������ ������� �ʴ´�. 

## Dataset
Dataset���δ� KITTI dataset�� ��� �� �����̴�.

### Converting label format from KITTI to YOLO
![KITTIFORMAT](https://miro.medium.com/v2/resize:fit:720/format:webp/1*JPq_TsecEHqjLsQZ1uPFDA.jpeg)
**KITTI format**
Pedestrian 0.00 0 -0.20 ... 8.41, 0.01

**YOLO format**
3 0.622 0.609 0.08 0.446

> Convert Code�� �̿��Ͽ� ��ȯ���� ����.

