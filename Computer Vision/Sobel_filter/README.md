# 🤖 Sobel Filter
## Edge Detection
Edge Detection is simply a case of trying to find the regions in an image where we have a sharp change in intensity or a sharp change in color,
a high value indicates a steep change and a low value indicates a shallow change. This can be used in various deep learning models such as CNN 
on MNIST or CIFAR-10 dataset. Edge detector can also be useful to implement segmentation and object detection models such as YOLO. This project was done to better understand how to implement a **Canny Edge Detector** from scratch without making use of any advance frameworks available.

## Sobel Operator
Sobel Operator approximates the derivative of an image. This is done by using a 3 by 3 matrix, one for each horizontal(x) and vertical(y) direction. 
The gradient in the x direction is calculated by finding the difference between the first column and the third column of the output matrix when 
filtering has been done on the image. The gradient in the y direction is calculated by finding the difference between the first row and 
the third row of the output matrix when filtering has been done on the image. 
Therefore if we look at the x-direction, the filter used will be Gx as shown below and vice versa. 
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/sobelOperator.png" width="842" height="399">

 The filtering step is done by doing convolution where we multiply corresponding values accordingly and get the output matrix 
 which is usually smaller than the actual image size considering no padding has been added to the image. Below is the illustration of how convolution works
 when we use Gx for finding changes in pixel intensity in the x-direction
 ![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/Gx.jpeg)
 
 Below is the illustration of how convolution works when we use Gy for finding changes in pixel intensity in the y-direction
 ![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/Gy.jpeg)

## Steps:
## Step 1: Implement Gaussian blur
Here we want to write a program that performs Gaussian blur on an input image using the a pre-determined 5x5 kernel, where B
is the blurred version of input image A. Blurring is used in edge detection to reduce the amount of noise in the images which improves the result of our
canny edge detection algorithm. The blur is applied to image A by convolution as shown before. Below is how the calculations should be done to apply gaussian blur (Note: * represents the convolution operation not multiplication)
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/blur.png" width="842" height="399">

Here is the result when blur has been applied to the input image A:
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/blurApplied.png" width="842" height="600">

## Step 2: Calculate image gradients
Sobel filter calculates the gradient of an image intensity at each pixel and the sobel_x_kernel sweeps through the image horizontally and finds the largest increase or decrease in intensity value. This is why the values in the second column of sobel_x_kernel matrix is all zero, so that it can compare the change in values in the x axis. It basically tries to find the discrete approximation to the derivative of each pixel

Below is the output image after applying Gx to the image
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/GxOutput.png" width="842" height="600">

Below is the output image after applying Gy to the image
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/GyOutput.png" width="842" height="600">

## Step 3: Calculate gradient magnitude
Our model measure the change in intensity horizontally for 'gx' and vertically for 'gy'. The gradient magnitude or the eigen values for gx will show a small eigen value for an edge. For a corner, it will show a large eigen value in gx and gy since the change in intensity is in both direction. Lastly, for a solid region the gradient magnitude will be very small regardless of which directions we are measuring since there is no significant change in pixel intensity. The magnitude can be found by using the formula below
![mag](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/magnitudeFormula.png)

Image below is the output image that represents the gradient magnitude.
![mag2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/magnitude.png)

## Step 4: Calculate gradient orientation
The orientation of the gradients can help us visualize differences in pixel intensity value within a particular area in the image. Gradient orientation is calculated by using the formula below

<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/%20orientationFormula.png" width="391" height="140">

The image shown below is the output image that represents the gradient orientation.

![orient2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/orientation.png)

## Step 5: Non-maxima Suppression and thresholding 
The gradient magnitude produced results in thick edges. Ideally, the final image should have thin edges. Thus, we must perform non maximum suppression to thin out the edges. Non maximum suppression works by finding the pixel with the maximum value in an edge. The image is scanned along the image gradient direction, and if pixels are not part of the local maxima they are set to zero. This has the effect of supressing all image information that is not part of local maxima.

Thresholding was done to identify 2 kinds of pixels which is the strong and weak pixels. So that we can remove the irrelevant pixel values or the noise that is present in the image. These values are found by getting the minimum and maximum value from the pixel value in the image array and use the ratio from the argument to determine the high and low threshold. Therefore, lower **'high-threshold-ratio'** will show a more accurate data in the final image since we are taking a more broad pixel range. If we put **'high-threshold-ratio'** equal to 1, it wil only show pixels that are equal to the max value within the image.

Below is the final output of our **Canny Edge Detector**
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/sobel_filter_result.png" width="842" height="600">
