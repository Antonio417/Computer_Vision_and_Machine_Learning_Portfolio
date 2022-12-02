# 📊 K-Means Clustering

<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/ML.jpg" width="700" height = "500" >

## Unsupervised Learning
As the name suggests, unsupervised learning is a type of machine learning in which the training of a model is not supervised using labels of the training dataset.
Instead, models themselves attempt to find hidden patterns and insights from the given data.
Unsupervised learning cannot be directly applied to a regression or classification problem because unlike supervised learning, 
we have the input data but no corresponding output data (no labels). The goal of unsupervised learning is to find the underlying structure of the dataset,
group that data according to similarities, and represent the data in a compressed format.

## Clustering 
Clustering is a type of unsupervised learning which involves grouping of data points. 
Given a set of data points, we can use a clustering algorithm to classify each data point into a specific group. 
In theory, data points that are in the same group should have similar properties and/or features, 
while data points in different groups should have highly dissimilar properties and/or features. 
There are four types of clustering which are centroid-based, density-based, distribution-based and 
hierarchical. Under these four types of clustering we have a lot of algorithms out there to explore.
Some examples of popular clustering algorithms are:
- K-Means Clustering
- Spectral Clustering
- Mean-Shift Clustering
- DBSCAN
- Gaussian Mixture Models

## K-Means Clustering

<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/kmeans_anim.gif" width="700" height = "500" >

K-Means Clustering is one of the simplest unsupervised machine learning algorithms.
we first decide a number *k*, which corresponds to the number of clusters that we desire to have in our dataset. 
This number will also correspond to the number of centroids.
A centroid is the location representing the center of a cluster. 
Each data point in your dataset is allocated to a specific cluster following a set of rules in an iterative manner. 
Also, the locations of the centroids are updated subsequently by averaging the data points assigned to the respective cluster. 
The **‘means’** in the k-Means Clustering refers exactly to this method of updating each cluster centroid.

In this project we will create a program that clusters and re-colours each pixel in a provided colour image to k mean colours 
using the k-means clustering algorithm. We should use our knowledge of python and numpy to build our own code to perform k-Means Clustering. 
This means that we won't be using any pre-existing framework or libary such as Scikit, Pytorch, TensorFlow,etc. 
The end result of the clustered image should look something like the one shown below.
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/objective.png" width="700" height = "300" >

## Steps:
1. Select the Number of Centroids/Clusters, k
2. Select k Points at Random(does not have to be from the data points) 
3. Make k Clusters
4. Compute New Centroid of Each Cluster

#### Notes: Data points are assigned to their corresponding cluster based on euclidean distance to each centroids. The shortest distance shows which cluster it belongs to.

## Result:
Images below are results from doing K-Means clustering with 4 centroids and 5 iterations, 
where the first image shows results from random centroid and second image shows the output image after K-Means clustering.
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/img1.png" height = "300">
<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Computer%20Vision/K-means/img/img2.png" height = "300">






