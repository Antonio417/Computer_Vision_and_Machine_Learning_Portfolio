# ⚙️ Variational Autoencoders
Description: Autoencoders is a data compression algorithm where the data compression and decompression functions are data specific, lossy and learned automatically from examples rather than engineered by human. They are made up of two networks concatenated together: an encoder network and a decoder network. The encoder network receives a d-dimensional input feture vector associated with example x and encodes it into a p-dimensional vector z. So it basically tries to learn how to model the function z = f(x), z is also called the latent vector. In this model p < d, hence we can say that the encoder acts as a data compression function. A simple autoencoder architecture is as shown below.

![img1]()
