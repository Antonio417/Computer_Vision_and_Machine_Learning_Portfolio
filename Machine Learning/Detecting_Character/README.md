# 🤖 Detecting Character
Description: Convolutional Neural Networks are well known for providing solutions for classification task. The aim of this project was to build a model that could accurately identify character's name inside an image. Challenges arise in this project mainly comes from the randomness of the dataset where for each character, they are presented in a variety of situations with different backgrounds, different angles, etc. I also wanted to compare and understand how change in architecture of these networks affects their performance. I then investigated other pre-trained model such as VGG16 and compare them with the base model.

## Pre-Processing
The data initially had 43 classes with an unequal distribution in the amount of images for each classes. This means that some of the classes will have more images in them than others. This is could lead to bias in our classification model because the model have a better accuracy for classes with more images. To solve this, I removed some of the classes that have less than 150 images in them since it is more advantageous to have at least 100 images in a class in order to get good results from our model. The final dataset that was used for training and testing have only 20 classes where in each classes there are more than 150 images. The images is then resized to 128 x 128. We can increase the number of data that we have by applying random transformation and augmenting it in many different ways. This could also lessen the chance for our model to overfit the data.

## Label Processing
Labels in the dataset are categorical while model needs the label to be a number. Solution for this is to do one-hot encoding to represent the classes. One-hot encoding was done because it avoids order of classes. LabelEncoder from Sklearn and to_categorical from Keras was used since it helps us to encode these labels for us.

## Base Model
The model that I created are inspired by the LeNet5 model. It is basically a CNN model with maxpooling applied to it. The model is as shown below.

Overfitting is a problem where the model is to sensitive with changes in the data. In this case the model could overfit the training data. To prevent this I use earlystopping, where we would stop training the model when their performance has not increase for certain amount of epoch. By doing this we can get a model that could perform better with unseen data and this is what we want at the end.

