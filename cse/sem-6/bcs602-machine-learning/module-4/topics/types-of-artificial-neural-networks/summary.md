# Types of Artificial Neural Networks

## Overview

Artificial Neural Networks come in various architectures, each designed for specific types of problems and data. From basic feedforward networks to specialized architectures like CNNs for images and RNNs for sequences, understanding different ANN types is essential for selecting appropriate models.

## Key Points

- **Feedforward Neural Networks (FNN)**: Basic architecture; information flows one direction (input → output); used for tabular data, function approximation
- **Convolutional Neural Networks (CNN)**: Specialized for spatial data (images); convolutional layers detect local patterns; pooling reduces dimensions; dominant in computer vision
- **Recurrent Neural Networks (RNN)**: Handle sequential data; connections form cycles; maintain hidden state; used for time-series, NLP, speech
- **Long Short-Term Memory (LSTM)**: RNN variant with gating mechanisms; solves vanishing gradient; remembers long-term dependencies
- **Autoencoders**: Unsupervised; encoder compresses input to latent representation, decoder reconstructs; dimensionality reduction, denoising
- **Generative Adversarial Networks (GAN)**: Two networks compete - generator creates samples, discriminator judges authenticity; image generation, style transfer

## Important Concepts

- CNN components: convolution (feature detection), pooling (downsampling), fully connected (classification)
- RNN variants: Vanilla RNN (short memory), LSTM (long memory), GRU (simplified LSTM)
- Architecture selection: Tabular→FNN, Images→CNN, Sequences→RNN/LSTM, Unsupervised→Autoencoder
- Transfer learning: use pre-trained networks (ImageNet CNNs) for new tasks

## Notes

- Know architecture for each type: FNN (layers), CNN (conv+pool+FC), RNN (recurrent connections)
- CNN for images (spatial patterns), RNN for sequences (temporal patterns)
- LSTM solves vanishing gradient in RNNs through gating mechanisms
- Understand use cases: vision→CNN, NLP→RNN/LSTM/Transformers, generation→GAN/Autoencoder
