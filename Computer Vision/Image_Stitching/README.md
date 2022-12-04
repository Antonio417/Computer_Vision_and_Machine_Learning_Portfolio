# 📊 Image Stitching
### Aim: Create a program that stitches two images with known homography into a single wide-angle image using bilinear interpolation. 
Description: Two images of the same landscape were provided as a way to test the algorithm used. The differences in the two images are in the angle, height and lighting. Homography coordinates was used to be able to interpret how one coordinate in one image can be translated to another image considering that
they are are taken at different angles. The homography matrix can only be computed between images taken from the same camera shot at different angles. It doesn't matter what is present in the images. Below are the two images that were provided.
