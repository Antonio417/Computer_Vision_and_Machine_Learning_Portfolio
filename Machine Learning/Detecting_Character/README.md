# 🤖 Detecting Character
Description: Convolutional Neural Networks are well known for providing solutions for classification task. The aim of this project was to build a model that could accurately identify character's name within a frame. Challenges arise in this project mainly comes from the randomness of the dataset where for each character, they are presented in a variety of situations with different backgrounds, different angles, etc. I also wanted to compare and understand how change in architecture of these networks affects their performance. I then investigated other pre-trained model such as VGG16 and compare them with the base model.

## Pre-Processing
The data initially had 43 classes with an unequal distribution in the amount of images for each classes. This means that some of the classes will have more images in them than others. This is could lead to bias in our classification model because the model have a better accuracy for classes with more images. To solve this, I removed some of the classes that have less than 150 images in them since it is more advantageous to have at least 100 images in a class in order to get good results from our model. The final dataset that was used for training and testing have only 20 classes where in each classes there are more than 150 images. The images is then resized to 128 x 128. We can increase the number of data that we have by applying random transformation and augmenting it in many different ways. This could also lessen the chance for our model to overfit the data.

## Label Processing
Labels in the dataset are categorical while model needs the label to be a number. Solution for this is to do one-hot encoding to represent the classes. One-hot encoding was done because it avoids order of classes. LabelEncoder from Sklearn and to_categorical from Keras was used since it helps us to encode these labels for us.

## Base Model
The model that I created were inspired by the LeNet5 model. It is basically a CNN model where the convolutional and maxpooling layer were alternately applied. The model is as shown below.

<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/model_summary.png" width=400 height=550>

To avoid overfitting where the model is to sensitive with changes in the data I use earlystopping where we would stop training the model when their performance has not increase for certain amount of epoch. By doing this we can get a model that could perform better with unseen data and this is what we want at the end. The base model after training it for 10 epoch have an accuracy of 91.6% with the test set. The difference in accuracy between the train and validation was around 11%, this means that overfitting still exist which can lead to an inconsistent model. Reducing overfitting can be done through variety of regularisation methods such as L1/L2 and dropout. This can be further investigated in the future.

## VGG-16 Model
This model was first made to win the ILSVR(Imagenet) competition back in 2014. It consist of convolutional layers of 3x3 filter with a stride 1 and always used same padding and maxpool layer of 2x2 filter of stride 2. It follows this arrangement of convolution and maxpooling layers consistently throughout the whole architecture. The 16 in the name of the model refers to the number of layers that actually have weights in them. The model is as shown below

<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/vgg16.png" width=700 height=400>

Earlystopping was also done with this model to reduce the chance of the model to overfit the training data. This model after training it for 10 epoch gave an accuracy of 85% for the test dataset. This might seem worse than the base model but this could be better because the model does not overfit the training data.

## Result
These two models were compared by taking an image that is not within the dataset and feed it to each model. The VGG-16 model performed way better compared to the base model that I have built. It also give a more definite probability of the chosen classes for the image provided while the base model have a more spread out probability. The image feeded in to the model is as shown below.

<img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/prediction_homer.jpeg" width=250 height=200><img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/prediction_marge.jpeg" width=250 height=200><img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/prediction_lisa.jpeg" width=250 height=200><img src = "https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/Detecting_Character/images/prediction_bart.jpeg" width=250 height=200>

## Key Takeaways 
- **Always make sure to check the dataset beforehand**. The dataset used in this project has a lot of classes where there is not a single image provided for it, this can lead to our model classifying an image as this class because it will give out the class with the highest probability which in this case is the one that has no data in it. So I decided to remove these classes in the data pre-processing step
- **Pay attention to memory**. This project make use of google colab for training since I do not own a GPU and in colab there is a limitation in the amount of memory that they could provide for non-members. So to work around this problem I changed numbers data type into integer32 or integer16, float32 or float16 because these data types used less memory in practice. I also delete unnecessary variables at some stages when it is not used any further
- **Transfer learning**. Finally I learned how to adjust a pre-trained model such as VGG-16 to be able to work in our favour
