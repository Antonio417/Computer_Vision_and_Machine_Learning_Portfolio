# 📊 K-Nearest Neigbors
Description: KNN is a supervised learning classifier which uses proximity to make classifications or predictions about the grouping of an individual data point.
The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other. KNN can also be used to solve regression problems.
The difference is that in classification, mode of K labels are returned as output while in regression, mean of K labels are returned.

Steps:

1. Initialize K to a chosen number of neighbors
1. Measure the distance between the new sample and the train sample using euclidean distance
2. Look for the nearest train sample
3. Predict the class of our new sample based on the most common label of their neighbors

Notes: K means are the number of neighbor samples that are used, So if k = 6, means that we'll predict our new sample based on 6 neighbors and look at their 
classes

The Algorithm are as shown below (*refresh page to reset the gif below)

![img1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/KNN/KNN-Classification.gif)
