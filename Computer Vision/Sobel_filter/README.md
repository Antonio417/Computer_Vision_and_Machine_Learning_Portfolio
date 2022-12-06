# 🤖 Sobel Filter
## Edge Detection
Edge Detection is simply a case of trying to find the regions in an image where we have a sharp change in intensity or a sharp change in color,
a high value indicates a steep change and a low value indicates a shallow change. This can be used in various deep learning models such as CNN 
on MNIST or CIFAR-10 dataset. Edge detector can also be useful to implement segmentation and object detection models suchs as YOLO. This project was done to better understand how to implement a **Canny Edge Detector** from scratch without making use of any advance frameworks available.

## Sobel Operator
Sobel Operator approximates the derivative of an image. This is done by using a 3 by 3 matrix, one for each horizontal(x) and vertical(y) direction. 
The gradient in the x direction is calculated by finding the difference between the first column and the third column of the output matrix when 
filtering has been done on the image. The gradient in the y direction is calculated by finding the difference between the first row and 
the third row of the output matrix when filtering has been done on the image. 
Therefore if we look at the x-direction, the filter used will be Gx as shown below and vice versa. 
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/sobelOperator.png" width="842" height="399">

 The filtering step is done by doing convolution where we multiply corresponding values accordingly and eget the output matrix 
 which is usually smaller than the actual image size considering no padding has been added to the image. Below is the illustration of how convolution works
 when we use Gx for finding changes in pixel intensity in the x-direction
 ![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Gx.jpeg)
 
 Below is the illustration of how convolution works when we use Gy for finding changes in pixel intensity in the y-direction
 ![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Gy.jpeg)

## Steps:
## Step 1: Implement Gaussian blur
Here we want to write a program that performs Gaussian blur on an input image using the a pre-determined 5x5 kernel, where B
is the blurred version of input image A. The blur is applied to image A by convolution as shown before. Below is how the calculations should be done to apply gaussian blur
![]()
Here is the result when blur has been applied to the input image A:
![]()

## Step 2: Calculate image gradients
## Step 3: Calculate gradient magnitude
## Step 4: Calculate gradien magnitude
## Step 5: Non-maxima Suppression and thresholding 
