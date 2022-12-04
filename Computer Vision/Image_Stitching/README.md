# 📊 Image Stitching
### Aim: Create a program that stitches two images with known homography into a single wide-angle image using bilinear interpolation. 
## Description:
Two images of the same landscape were provided as a way to test the algorithm used. The differences in the two images are in the angle, height and lighting. Homography coordinates was used to be able to interpret how one coordinate in one image can be translated to another image considering that
they are are taken at different angles. The homography matrix can only be computed between images taken from the same camera shot at different angles. It doesn't matter what is present in the images. Below are the two images that were provided.

Left Image: 

![img1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/left.jpg)

Right Image:

![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/right.jpg)


As we can see that the two images are taken at the same time just at a different angle.

In this case the homography coordinates were given as

H: [[1.6010, -0.0300, -317.9341], [0.1279, 1.5325, -22.5847], [0.0007, 0, 1.2865]]

## Steps:

1. Draw test points on left image to test our homography coordinate as shown below<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/leftH.png" width="512" height="384">
2. Use homography to find whether the matrix given can be used to interpret those coordinate on the second image as shown below<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/rightH.png" width="512" height="384">
3. Write a bilinear interpolation function to compute the intensity of the transformed pixel coordinate in the other image using intensity values from
neighbouring pixel locations
4. Initialize a "canvas" of size 1024x384 for us to print the stitched image (this could change depending on image size used)
5. Image stitching by connecting the left image (512x384) and the rest of the blank area in the canvas using the right image coordinates
6. Improve image accordingly by adjusting width, brightness, gaussian blur at the seam and location of the horizontal seam.

## Result:
The result were quite impressive considering that we are doing all of this without the help of any advance frameworks and all of the calculations were done manually. Below are the output image after stitching was done. This image still has a visible seam because necessary adjustments were not done yet.
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/Stitched_img.jpg" width="1024" height="384">

Below are the final image after blurring the image near the seam to make it less visible and adjusting the brightness of the right side of the seam
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/Stitched_Image_Adjust_Brightness.jpg" width="1024" height="384">

## Improvements:
- Adjusting the brightness were done by trial and error. This was done due to time restrictions on the project. To improve this we can try to normalize the image and adjust the brightness better. We can also focus on doing the normalisation near the seam.
- We can adjust the width of the image automatically with respect to the output image rather than initializing a canvas
- Investigate more on alpha blending methods to make the image seamless

## Questions:
1. What makes a coordinate homogenous ?

**ans:** A homogenenous coordinate is a coordinate system that algebraically treats all points in the projective plane equally. A coordinate is homogenous if x = ax where a ~= 0 and it can be used to represent points at infinity with a finite coordinates. For example if we have a matrix x = [5 10] in euclidean plane and the homogenous coordinate of this is x = [5 10 1], so we add another dimension in our matrix. The points at infinity of our matrix will be equal to x = [5 10 0], this is a point at infinity because with this matrix if we want to go back to the euclidean coordinate, we would divide everything with the last element which is zero and any value divided by zero is equal to infinity

2. How do you reverse a homography operation ?

**ans:** We can reverse the homography operation by dividing our array with the last element and this will make our extra dimension equals to 1 for each channel. Then we can just delete the last element or the added dimension in our array. So for example we have a homogenous coordinates equal to x = [6, 12, 3] after dividing we'll get x = [2, 4, 1] and the last step is deleting the extra dimension, which will give us x = [2, 4]. This is our coordinates in the euclidean plane.

3. Explain why we need bilinear interpolation ?

**ans:** The bilinear interpolation is used to resample the images and the textures that comes with it. So to find the pixel location we use homography and to get the intensity of the pixel we use interpolation. It gaves a really good results because it measures the weighted average of the attributes of 4 surrounding pixels and apply it to the current pixel location. We keep on doing this with every pixel location to interpolate the right image into the left image.

4. Why is there an obvious stitch in the image ?

**ans:** The stitch is still visible because the difference in brightness, texture and the contrast between the two images is quite large. Also, the seam is visible because the pixel intensity value of the left image and the right image overlap at that specific coordinates.

