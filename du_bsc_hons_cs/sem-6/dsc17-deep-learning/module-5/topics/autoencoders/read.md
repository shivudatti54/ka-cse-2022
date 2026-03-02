# Autoencoders: Comprehensive Study Material

## Deep Learning - BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

### What are Autoencoders?

Autoencoders are a class of artificial neural networks designed to learn efficient representations of data, typically for the purpose of dimensionality reduction or feature learning. They belong to the unsupervised learning paradigm, meaning they can learn patterns from unlabeled data without explicit labels.

The fundamental concept behind autoencoders is deceptively simple: train the network to reconstruct its input at the output layer. However, in doing so, the network learns compressed representations—called **latent codes** or **bottleneck representations**—that capture the most essential features of the data.

### Historical Context and Relevance

Autoencoders were first introduced in the 1980s as a solution to the "backpropagation without a teacher" problem. While early versions faced challenges with training deep networks, the advent of **stacked autoencoders** and later **variational autoencoders** has made them indispensable in modern deep learning.

### Real-World Relevance

Autoencoders power numerous real-world applications:

- **Netflix and Spotify**: Recommendation systems use autoencoders to learn user preferences
- **Medical Imaging**: Anomaly detection in MRI and CT scans
- **Fraud Detection**: Identifying unusual patterns in financial transactions
- **Image Denoising**: Restoring old photographs or removing noise from images
- **Natural Language Processing**: Sentence embeddings and text summarization

---

## 2. Architecture of Autoencoders

### Core Components

An autoencoder consists of three main components:

#### 2.1 Encoder

The encoder is a neural network that compresses the input data into a lower-dimensional representation. It maps the input **x** to the latent space **z**:

```
z = f(x) = σ(W₁x + b₁)
```

Where:
- **x** = input vector
- **z** = latent representation (bottleneck)
- **W₁** = encoder weight matrix
- **b₁** = encoder bias
- **σ** = activation function (ReLU, Sigmoid, Tanh)

#### 2.2 Latent Space (Bottleneck)

The latent space is the compressed representation of the input. It forces the network to learn the most important features by restricting information flow. The dimensionality of the latent space (often denoted as *d*) is a crucial hyperparameter:
- Too large: Network might simply copy the input
- Too small: Loss of critical information

#### 2.3 Decoder

The decoder attempts to reconstruct the original input from the latent representation:

```
x̂ = g(z) = σ(W₂z + b₂)
```

Where:
- **x̂** = reconstructed output
- **W₂** = decoder weight matrix
- **b₂** = decoder bias

### Loss Function

The network is trained to minimize the **reconstruction error**:

```
L(x, x̂) = ||x - x̂||²  (Mean Squared Error)
```

or

```
L(x, x̂) = -Σ[x·log(x̂) + (1-x)·log(1-x̂)]  (Cross-Entropy)
```

---

## 3. Types of Autoencoders

### 3.1 Vanilla (Basic) Autoencoder

The simplest form where encoder and decoder are fully connected layers. It learns to compress and reconstruct data but may suffer from overfitting if the latent space is too large.

**Use Case**: Dimensionality reduction (similar to PCA but nonlinear)

### 3.2 Variational Autoencoders (VAEs)

VAEs are generative models that learn the probability distribution of the data. Instead of encoding to a single point, they encode to a probability distribution (typically Gaussian).

**Key Innovation**: Reparameterization trick

```
z = μ + σ ⊙ ε, where ε ~ N(0, I)
```

**Architecture**:
- Encoder outputs mean (μ) and standard deviation (σ)
- Decoder samples from the learned distribution
- Loss includes reconstruction loss + KL divergence

**Use Case**: Image generation, data augmentation, anomaly detection

### 3.3 Sparse Autoencoders

These impose a sparsity constraint on the latent representation, forcing most neurons to be inactive. This encourages the discovery of meaningful features.

**Implementation**: Add L1 regularization to the loss function

```
L_sparse = L_reconstruction + λ||z||₁
```

**Use Case**: Feature learning, when interpretable representations are needed

### 3.4 Denoising Autoencoders (DAEs)

DAEs are trained to reconstruct clean data from corrupted inputs. The corruption can be:
- Gaussian noise
- Masking noise (randomly zeroing out inputs)
- Salt-and-pepper noise

**Training Process**:
1. Corrupt input: x̃ = Corrupt(x)
2. Reconstruct: x̂ = Decoder(Encoder(x̃))
3. Compare with original: L(x, x̂)

**Use Case**: Image denoising, speech enhancement, pretraining neural networks

### 3.5 Contractive Autoencoders (CAEs)

CAEs add a penalty term that minimizes the sensitivity of the latent representation to small changes in input:

```
L_contractive = L_reconstruction + λ||∂z/∂x||²_F
```

This creates robust representations that are less sensitive to noise.

**Use Case**: Gesture recognition, robust feature extraction

### 3.6 Convolutional Autoencoders (CAEs)

Use convolutional layers instead of fully connected layers, making them ideal for image data.

**Architecture**:
- Encoder: Conv layers + Pooling
- Decoder: Upsampling/Deconv + Conv layers

**Use Case**: Image compression, image generation, medical image processing

### 3.7 Stacked (Deep) Autoencoders

Multiple encoder-decoder pairs stacked together. Each layer learns a more abstract representation.

```
Input → Encoder₁ → Encoder₂ → Latent → Decoder₂ → Decoder₁ → Output
```

**Use Case**: Deep feature learning, pretraining deep neural networks

---

## 4. Practical Implementation

### Example 1: Vanilla Autoencoder with PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, MNIST

# Define the Autoencoder architecture
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        
        # Encoder: 784 → 256 → 64 → 32
        self.encoder = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 32)  # Bottleneck
        )
        
        # Decoder: 32 → 64 → 256 → 784
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 256),
            nn.ReLU(),
            nn.Linear(256, 784),
            nn.Sigmoid()  # Output between 0 and 1
        )
    
    def forward(self, x):
        z = self.encoder(x)
        x_reconstructed = self.decoder(z)
        return x_reconstructed
    
    def encode(self, x):
        return self.encoder(x)

# Training function
def train_autoencoder():
    # Load MNIST dataset
    transform = transforms.Compose([transforms.ToTensor()])
    train_dataset = MNIST(root='./data', train=True, transform=transform, download=True)
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
    
    # Initialize model, loss function, optimizer
    model = Autoencoder()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training loop
    num_epochs = 20
    for epoch in range(num_epochs):
        total_loss = 0
        for batch_data, _ in train_loader:
            # Flatten the images
            batch_data = batch_data.view(batch_data.size(0), -1)
            
            # Forward pass
            outputs = model(batch_data)
            loss = criterion(outputs, batch_data)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss/len(train_loader):.6f}')
    
    return model

# Run training
model = train_autoencoder()

# Save latent representations
def get_latent_features(model, data_loader):
    model.eval()
    latent_features = []
    with torch.no_grad():
        for batch_data, _ in data_loader:
            batch_data = batch_data.view(batch_data.size(0), -1)
            z = model.encode(batch_data)
            latent_features.append(z)
    return torch.cat(latent_features, dim=0)
```

### Example 2: Variational Autoencoder (VAE) with PyTorch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class VAE(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=256, latent_dim=2):
        super(VAE, self).__init__()
        
        # Encoder
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)      # Mean
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)  # Log variance
        
        # Decoder
        self.fc3 = nn.Linear(latent_dim, hidden_dim)
        self.fc4 = nn.Linear(hidden_dim, input_dim)
        
    def encode(self, x):
        h = F.relu(self.fc1(x))
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)
        return mu, logvar
    
    def reparameterize(self, mu, logvar):
        """Reparameterization trick for backpropagation"""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z):
        h = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h))
    
    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        x_recon = self.decode(z)
        return x_recon, mu, logvar

def vae_loss(x_recon, x, mu, logvar):
    """VAE loss = Reconstruction loss + KL Divergence"""
    # Reconstruction loss (Binary Cross Entropy)
    recon_loss = F.binary_cross_entropy(x_recon, x, reduction='sum')
    
    # KL Divergence: -0.5 * sum(1 + log(σ²) - μ² - σ²)
    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    
    return recon_loss + kl_loss

# Training the VAE
def train_vae():
    model = VAE()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    train_dataset = MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
    
    model.train()
    for epoch in range(num_epochs):
        total_loss = 0
        for batch_data, _ in train_loader:
            batch_data = batch_data.view(batch_data.size(0), -1)
            
            optimizer.zero_grad()
            x_recon, mu, logvar = model(batch_data)
            loss = vae_loss(x_recon, batch_data, mu, logvar)
            
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        print(f'Epoch {epoch+1}: Loss = {total_loss/len(train_loader):.4f}')

# Generate new images
def generate_images(model, num_samples=10):
    model.eval()
    with torch.no_grad():
        # Sample from standard normal distribution
        z = torch.randn(num_samples, 2)
        generated = model.decode(z)
        return generated.view(-1, 1, 28, 28)
```

---

## 5. Advanced Concepts

### 5.1 Regularization Techniques

| Technique | Description | Purpose |
|-----------|-------------|---------|
| **L2 Regularization** | Penalizes large weights | Prevents overfitting |
| **Dropout** | Randomly deactivates neurons | Improves generalization |
| **Noise Injection** | Adds noise to input/bottleneck | Creates robustness |
| **Early Stopping** | Monitors validation loss | Prevents overfitting |

### 5.2 Choosing the Latent Dimension

The latent dimension (*d*) should be chosen based on:

1. **Information Theory**: d should capture sufficient information (d > intrinsic dimensionality)
2. **Compression Ratio**: Typically 10-100x compression for images
3. **Empirical Testing**: Cross-validation on reconstruction quality

### 5.3 Evaluation Metrics

- **Reconstruction Error**: MSE or MAE on test data
- **Latent Space Visualization**: t-SNE or PCA on latent vectors
- **Downstream Task Performance**: Accuracy on classification using latent features

---

## 6. Applications

### 6.1 Dimensionality Reduction
Autoencoders provide nonlinear dimensionality reduction, outperforming PCA on complex data.

### 6.2 Anomaly Detection
Reconstruction error above threshold indicates anomalies:
- Financial fraud detection
- Industrial defect detection
- Network intrusion detection

### 6.3 Image Compression
Learned compression can outperform JPEG for specific domains (medical imaging, satellite imagery).

### 6.4 Data Denoising
Denoising autoencoders remove:
- Image noise
- Audio artifacts
- Sensor errors

### 6.5 Generative Modeling
VAEs can generate new samples by sampling from the latent space.

### 6.6 Recommendation Systems
Autoencoders learn user-item interactions for collaborative filtering.

---

## 7. Delhi University Syllabus Context

This content aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically:

- **Unit III: Unsupervised Learning** - Autoencoders as a key unsupervised technique
- **Neural Network Architectures** - Encoder-decoder structure
- **Deep Learning Applications** - Practical implementations

---

## 8. Multiple Choice Questions

### Level 1: Basic (Questions 1-4)

**Q1.** In an autoencoder, which component compresses the input into a latent representation?
- A) Decoder
- B) Encoder
- C) Loss function
- D) Optimizer

**Answer: B**

**Q2.** What is the primary purpose of the bottleneck layer in an autoencoder?
- A) Increase model capacity
- B) Force compression and learn essential features
- C) Prevent overfitting completely
- D) Speed up training

**Answer: B**

**Q3.** Which type of autoencoder is specifically designed for generating new samples?
- A) Denoising Autoencoder
- B) Sparse Autoencoder
- C) Variational Autoencoder
- D) Contractive Autoencoder

**Answer: C**

**Q4.** In a Variational Autoencoder, the reparameterization trick is used to:
- A) Increase the reconstruction loss
- B) Enable backpropagation through stochastic sampling
- C) Reduce the number of parameters
- D) Normalize the input data

**Answer: B**

### Level 2: Intermediate (Questions 5-8)

**Q5.** In a sparse autoencoder, the sparsity constraint is typically enforced by:
- A) Adding L1 regularization to the latent representation
- B) Using max pooling in the encoder
- C) Reducing the batch size
- D) Adding more hidden layers

**Answer: A**

**Q6.** What is the primary difference between a denoising autoencoder and a vanilla autoencoder?
- A) Denoising AE uses convolutional layers
- B) DAE is trained to reconstruct clean data from corrupted input
- C) Vanilla AE cannot handle images
- D) DAE has a larger bottleneck

**Answer: B**

**Q7.** The KL divergence term in VAE loss function serves to:
- A) Maximize reconstruction accuracy
- B) Regularize the latent space to follow a Gaussian distribution
- C) Reduce the number of parameters
- D) Increase the learning rate

**Answer: B**

**Q8.** Which loss function is commonly used for training autoencoders on image data?
- A) Cross-entropy only
- B) Mean Squared Error (MSE)
- C) Hinge loss
- D) Margin ranking loss

**Answer: B**

### Level 3: Advanced (Questions 9-12)

**Q9.** In a contractive autoencoder, the Jacobian regularization term ∂L/∂X encourages:
- A) Larger reconstruction error
- B) Stability of latent representations to input perturbations
- C) Sparser activations
- D) Deeper networks

**Answer: B**

**Q10.** What problem does a stacked autoencoder address in deep networks?
- A) Vanishing gradient during pretraining
- B) Overfitting in shallow networks
- C) Lack of convolutional layers
- D) Insufficient data

**Answer: A**

**Q11.** For anomaly detection using autoencoders, a data point is considered anomalous if:
- A) Its reconstruction error is below the threshold
- B) Its reconstruction error exceeds the threshold
- C) It has a low latent space value
- D) It is correctly classified by a classifier

**Answer: B**

**Q12.** In a convolutional autoencoder for image processing, the decoder typically uses:
- A) Only fully connected layers
- B) Upsampling or transposed convolution layers
- C) Recurrent layers
- D) Attention mechanisms only

**Answer: B**

---

## 9. Flashcards

| Term | Definition |
|------|------------|
| **Autoencoder** | An unsupervised neural network that learns to compress and reconstruct data |
| **Latent Space** | The compressed bottleneck representation learned by the encoder |
| **Reconstruction Error** | The difference between input and reconstructed output |
| **Variational Autoencoder (VAE)** | A generative autoencoder that learns a probability distribution in latent space |
| **Reparameterization Trick** | Method to make stochastic sampling differentiable: z = μ + σ⊙ε |
| **Sparse Autoencoder** | Autoencoder with regularization encouraging most neurons to be inactive |
| **Denoising Autoencoder** | Trained to reconstruct clean data from corrupted inputs |
| **Contractive Autoencoder** | Adds penalty to minimize sensitivity of latent representation to input changes |
| **Encoder** | Network component that maps input to latent representation |
| **Decoder** | Network component that reconstructs input from latent representation |
| **Bottleneck** | The narrowest layer (latent space) that forces data compression |
| **KL Divergence** | Measure used in VAEs to regularize latent space distribution |

---

## 10. Key Takeaways

1. **Autoencoders are unsupervised** learning models that reconstruct their input, learning compressed representations in the process.

2. **Three essential components**: Encoder (compresses), Latent Space (bottleneck), Decoder (reconstructs).

3. **Vanilla autoencoders** are used for basic compression but may overfit if the latent space is too large.

4. **VAEs** add probabilistic modeling, enabling generation of new samples by sampling from learned distributions.

5. **Sparse autoencoders** use regularization to discover meaningful features by constraining most neurons to be inactive.

6. **Denoising autoencoders** learn robust representations by training on corrupted inputs, useful for noise removal.

7. **Contractive autoencoders** create stable representations by penalizing sensitivity to input changes.

8. **Practical applications** span anomaly detection, image compression, recommendation systems, and generative modeling.

9. **Implementation requires** careful consideration of: latent dimension, architecture depth, regularization, and loss function choice.

10. **For the exam**: Focus on understanding when to use each type, the mathematics behind VAE training, and practical implementation details.

---

## References

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
2. Kingma, D. P., & Welling, M. (2014). Auto-Encoding Variational Bayes. *ICLR 2014*.
3. Delhi University NEP 2024 UGCF Syllabus - Computer Science (Hons).

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF guidelines.*