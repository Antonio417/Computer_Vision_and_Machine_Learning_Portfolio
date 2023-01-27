# Computer Vision and Machine Learning Portfolio
<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/coverImage.jpeg" width=800 height=420>

### Welcome to my Computer Vision 👀 and Machine Learning 🤖 Portfolio 
### Here I provide a brief explanation to all of my Computer Vision and Machine Learning related projects
### Feel free to click on the project's name to take a look at each project in more detail 

## 📚 Table of Contents
- [Computer Vision](#computer-vision)
- [Machine Learning](#machine-learning)

# Computer Vision 
| Project Name | Area | Description | 
|---|---|---|
| [K-Means Clustering on Image](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Computer%20Vision/K-means) | Centroid-Based Clustering | This project was done to better understand how K-Means and K-means++ clustering can be done on an image. K-means is an unsupervised learning model where the dataset has no data to class pair like what we have in a classification problem. The model will have to find clusters or pattern within the data by itself. The result of this project is as shown below. First image shows expected result, second image shows image after clustering it with four initial random centroids and third image show the final image after K-Means clustering for 5 iteration![Kmeans](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/objective.png) ![image1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/img1.png)![image2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/img2.png)| 
| [Image Stitching](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Computer%20Vision/Image_Stitching) | Projective Geometry and Use of Homography Matrix | This project main aim was to be able to stitch two or more images of the same landscape that are taken at different angle, height and lighting into one long image. The output image expected was an image that is similar to a panoramic image. The output of this project is as shown below. The first two image are the initial image that are taken at a different angle compared to the other one. The last image is the stitched image. ![left](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/left.jpg)![right](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/right.jpg)![Image Stitching](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Image_Stitching/Stitched_Image_Adjust_Brightness.jpg) | 
| [Sobel Filter](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Computer%20Vision/Sobel_filter) | Image Filtering and Edge Detection | This project was done to help us understand how to build a **Canny Edge Detector** from scratch by using a sobel filter and investigate how to perform these tasks manually without using any pre-existing frameworks. Below was the result obtained from this project.![Computer Vision](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/Sobel_filter/Visuals/sobel_filter_result.png) | 

# Machine Learning 
#### Projects shown below were done to better understand machine learning or deep learning models and investigate the application of these models to solve real-life problems.
| Project Name | Description | 
|---|---|
| [Detecting Character](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/Detecting_Character) | Convolutional Neural Networks are well known for providing solutions for a classification task. This project was done to compare and understand how change in architecture of these networks affects their performance. I also investigated other pre-trained model such as VGG16 and compare these model with the base model that I have built. The final model was expected to be able to identify a character's name in a given frame with an acceptable accuracy.<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/example.png" width=400 height=400>
| [Convolutional Variational Autoencoders](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/VAE) | It is an autoencoder that learns a latent variable model for its input data. So instead of letting your neural network learn an arbitrary function, you are learning the parameters of a probability distribution function modeling your data. If you sample points from this distribution, you can generate new input data samples hence why a VAE is considered as a "generative model". They can be used to compress data and denoise data which can be useful when we are dealing with images. Architecture of the model is as shown below. ![VAE](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/Images/VAE_img.jpeg)
| [Linear Regression](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/Linear-Regression) | Regression is a statistical method that attempts to determine the strength and character of the relationship between one dependent variable (usually denoted by Y or 'label' in machine learning) and a series of other variables (known as independent variables). Linear regression attempts to find the line (or a more complex linear combination) that most closely fits the data according to a specific mathematical criterion. Result is as shown below. <img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Linear-Regression/Linear_Regression.png" width=500 height=420>
| [Logistic Regression](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/Logistic-Regression) | Logistic Regression attempts to find the probability of an event taking place by having the log-odds for the event be a linear combination of one or more independent variables. Logistic Regression is fitting the line values to the sigmoid curve. Loss Function for Logistic Regression is the Cross Entropy. Result is as shown below ![img1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Logistic-Regression/result.jpeg)
| [K-Nearest Neighbor](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/KNN) | KNN is a supervised learning classifier which uses proximity to make classifications or predictions about the grouping of an individual data point. The process of this algorithm is as shown below (reload the page to replay gif)<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/KNN/KNN-Classification.gif" width=600 height=420>
| [Support Vector Machine](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/SVM) | The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space(N — the number of features) that distinctly classifies the data points. The best hyperplane is the one that represents the largest equal separation between the two classes. Result is as shown below where one represents the hyperplane in a 2D data and the other one in 3D data <img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/SVM/svm2d.gif" width="680" height="500" /> <img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/SVM/Linear3D.gif" width="680" height="500" />|
| [Decision Tree](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/tree/main/Machine%20Learning/Decision-Tree) | A decision tree is a flowchart-like structure in which each internal node represents a test on a feature (e.g. whether a coin flip comes up heads or tails) , each leaf node represents a class label (decision taken after computing all features) and branches represent conjunctions of features that lead to those class labels. This model breaks down our data by making a decision based on asking a series of questions. An example of this process is as shown<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Decision-Tree/decisionTree.gif" width="680" height="420" />
 
