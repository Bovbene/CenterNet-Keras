# CenterNet-Keras
CenterNet: Implementation of target detection model in Keras 

### Data
| Train Data | Weight File  | Test Data | Input Size | mAP 0.5:0.95 | mAP 0.5 |
| :-----: | :-----: | :------: | :------: | :------: | :-----: |
| VOC07+12 | [centernet_resnet50_voc.h5](https://github.com/bubbliiiing/centernet-keras/releases/download/v1.0/centernet_resnet50_voc.h5) | VOC-Test07 | 512x512 | - | 77.1
| COCO-Train2017 | [centernet_hourglass_coco.h5](https://github.com/bubbliiiing/centernet-keras/releases/download/v1.0/centernet_hourglass_coco.h5) | COCO-Val2017 | 512x512 | 39.0 | 57.6 

### Environment Configuration
tensorflow-gpu==1.13.1  
keras==2.1.5  

### Tips
centernet_resnet50_voc.h5 is trained by voc data.
centernet_hourglass_coco.h5 is trained by coco data 
**No Chinese label，no spacebar！**    
**Befor training, U must create a txt in model_data, which contain the category to be classified. Then, point classes_path to this file in train.py.**

### Download Weight File
centernet_resnet50_voc.h5 and centernet_hourglass_coco.h5 can be download in https://pan.baidu.com/s/1Tl56NmZVYljA2jHmOx5zOg (ukm3)

### Instructions for use
#### 1. Use pre-trained weights 
a. Download centernet_resnet50_voc.h5 or centernet_hourglass_coco.h5, put in model_data, run predict.py, enter 
```python predict.py
img/street.jpg
``` 
b. se video.py to perform camera detection.
#### 2. Use self-trained weights 
a. In the yolo.py file, modify model_path and classes_path in the following parts to correspond to the trained files; **model_path corresponds to the weight file under the logs folder, classes_path is the class corresponding to model_path **.

```python
_defaults = {
    "model_path"        : 'model_data/centernet_resnet50_voc.h5',
    "classes_path"      : 'model_data/voc_classes.txt',
    # "model_path"        : 'model_data/centernet_hourglass_coco.h5',
    # "classes_path"      : 'model_data/coco_classes.txt',
    "backbone"          : 'resnet50',
    "model_image_size"  : [512,512,3],
    "confidence"        : 0.3,
    # backbone resnet50 True
    # backbone hourglass False
    "nms"               : True,
    "nms_threhold"      : 0.3,
}
```
b. run predict.py, enter
```python
img/street.jpg
```
c. Use video.py to perform camera detection.   

### Training steps 
1. We use VOC format for training.
2. Before training, put the label file in the Annotation under the VOC2007 folder under the VOCdevkit folder.
3. Before training, place the picture files in the JPEGImages under the VOC2007 folder under the VOCdevkit folder.
4. Use the voc2centernet.py file to generate the corresponding txt before training. 
5. Then run voc_annotation.py in the root directory, and you need to change the classes to your own classes before running.
```python
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```
6、At this time, the corresponding 2007_train.txt will be generated, and each line corresponds to the **position of the picture** and the **position of the real frame**. 
7、**Before training, you need to create a new txt document under model_data, enter the class to be classified in the document, and point classes_path to the file in train.py **, examples are as follows: 
```python
classes_path = 'model_data/new_classes.txt'    
```
model_data/new_classes.txt   
```python
cat
dog
...
```
8、Run train.py to start training. 

### mAP target detection accuracy calculation update 
Updated the get_gt_txt.py, get_dr_txt.py and get_map.py files. 
get_map is copied from https://github.com/Cartucho/mAP  
The specific mAP calculation process can refer to: https://www.bilibili.com/video/BV1zE411u7Vw

### Reference
https://github.com/xuannianz/keras-CenterNet      
https://github.com/see--/keras-centernet      
https://github.com/xingyizhou/CenterNet    
