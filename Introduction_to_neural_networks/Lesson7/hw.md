### Introduction to YOLOv2
Redmon and Farhadi developed an improved version of YOLO, named YOLOv2, which had several features not seen in YOLO, such as multi-scale training (training on images of different resolutions), thus providing an easy trade-off between speed and accuracy.

YOLO makes a larger number of localization errors compared to Fast R-CNN, and it’s recall is low when matched with region proposal based methods. In YOLOv2, the main concern was fixing these errors while maintaining the detection speed and accuracies.

### Advantages
##### 1. Batch Normalization (BN)
```BN provides every layer of a neural network the capability to learn independently of other layers. When BN is added to all convolutional layers in YOLO, a 2% improvement in mAP (mean average precision) is observed.```
##### 2. High Resolution Classifier
   ```In YOLOv2, the classification network is first trained on ImageNet at 224 x 224 resolution, then fine-tuned at the full 448 x 448 resolution for 10 epochs, on the ImageNet dataset, giving the network time to adjust its filters to work better on higher resolution input. This process of developing a high-resolution classification network results in an increase of around 4% mAP.```
   
##### 3. Convolutional with Anchor Boxes
   ```Using anchor boxes decreases the accuracy to 69.2 mAP from 69.5, but results in a significant increase in recall, from 81% to 88%.```
   
##### 4. Dimension Clusters
```This method suggests running K-means clustering on the training set bounding boxes to automatically find good priors, instead of starting with hand-picked anchor box dimensions. Using K-means to generate the bounding boxes initializes the model with a better representation and makes the task easier to learn.```

Source: https://medium.com/analytics-vidhya/deep-dive-on-yolov2-and-yolo9000-2eba212dcf8a