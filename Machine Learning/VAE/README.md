# ⚙️ Variational Autoencoders
## Autoencoders
Description: Autoencoders is a data compression algorithm where the data compression and decompression functions are data specific, lossy and learned automatically from examples rather than engineered by human. They are made up of two networks concatenated together: an encoder network and a decoder network. The encoder network receives a d-dimensional input feture vector associated with example x and encodes it into a p-dimensional vector z. So it basically tries to learn how to model the function z = f(x), z is also called the latent vector. In this model p < d, hence we can say that the encoder acts as a data compression function. A simple autoencoder architecture is as shown below.

![img1](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/Autoencoder.png)

As mentioned before, autoencoders are data specific which means that the model will only able to compress data similar to what they have been trained on. They are also lossy implies that the decompressed output from the decoder will be degraded when compared to the input. This model will also learn automatically from examples which is a good thing because it is easier to train it to specialized in compressing specific type of input. It doesn't require any new engineering, just appropriate training data

## Variational Autoencoders
Description:  a type of autoencoder with added constraints on the encoded representations being learned. More precisely, it is an autoencoder that learns a latent variable model for its input data. So instead of letting your neural network learn an arbitrary function, you are learning the parameters of a probability distribution modeling your data. If you sample points from this distribution, you can generate new input data samples hence why a VAE is considered as a "generative model".

How it works ?

1. Transform input into two parameters in the latent space 
2. Randomly sample similar points from the latent normal distribution that is assumed to generate the data
3. Decoder network maps these latent space points back to the original input data

Parameters in this model are trained with two loss function, they are:
1. Reconstruction Loss: This will force the model to decode samples that match the inputs
2. KL Divergence: This acts as a regularization term and therefore helps in reducing overfitting to the training data

Below is the architecture of Variational Autoencoders
![img2](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/VAE_img.jpeg)

## Implementation using Convolutional Neural Network
Description: In this project a Convolutional neural network (convnet) was used in order to build the encoder and decoder. Convnet are used because they perform better especially when dealing with images. The model was then used to perform compression and denoising of images from the famous MNIST dataset.
The architecture of the complete model is as shown below

![img3](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/VAE_architecture.png)

Results:
Shown below is the generated image from the latent space with a dimension of 10
![img4](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/generated_images_L10_E_10.png)
Shown below is the visualization of the encoded dimension of the latent space used
![img5](https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/Encoded_dimension_visualization_L10_E10.png)

||**Latent space with dimension of 10**|
|:--:|:--:|
|**Initial Image**|<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/initial%20image.png">|
|**Prediction**|<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/prediction_from_original_images.png">|
|**Noisy Image**|<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/Noisy_images.png">|
|**Denoised Image**|<img src="https://github.com/Antonio417/Computer_Vision_and_Machine_Learning_Portfolio/blob/main/Machine%20Learning/VAE/prediction_from_noisy_image.png">|

## Summary
This project shows us how autoencoders work and the power of representing data in the latent space. These latent space are very useful when dealing with generative models such as GAN, VQ-GAN and VQ-VAE. They also reduces the amount of processing power needed when building and training complex models such as what we see in DALL-E model. The generated image from the latent space with 10 dimension have some bad outputs, this is because the model was overfitting when we use a high latent space dimension. The number of dimension shows us how specific or how general the kinds of features we want our latent space to learn and represent. In this case we can choose a lower dimension for our latent space which will improve the performance of the model. 
