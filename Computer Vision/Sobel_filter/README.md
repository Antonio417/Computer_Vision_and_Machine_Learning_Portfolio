# 🤖 Sobel Filter
## Edge Detection
Edge Detection is simply a case of trying to find the regions in an image where we have a sharp change in intensity or a sharp change in color,
a high value indicates a steep change and a low value indicates a shallow change. This can be used in various deep learning models such as CNN 
on MNIST or CIFAR-10 dataset. Edge detector can also be useful to implement segmentation and object detection models suchs as YOLO. 

## Sobel Operator
Sobel Operator approximates the derivative of an image. This is done by using a 3 by 3 matrix, one for each horizontal(x) and vertical(y) direction. 
The gradient in the x direction is calculated by finding the difference between the first column and the third column of the output matrix when 
filtering has been done on the image. The gradient in the y direction is calculated by finding the difference between the first row and 
the third row of the output matrix when filtering has been done on the image. 
Therefore if we look at the x-direction, the filter used will be Gx as shown below and vice versa. 
![]()
 
 The filtering step is done by doing convolution where we multiply corresponding values accordingly and eget the output matrix 
 which is usually smaller than the actual image size considering no padding has been added to the image. Below is the illustration of how convolution works
 ![]()
