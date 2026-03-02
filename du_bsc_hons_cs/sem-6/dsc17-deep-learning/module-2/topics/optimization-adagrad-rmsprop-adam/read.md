# Optimization Algorithms: AdaGrad, RMSProp, and Adam

## Deep Learning — BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

Optimization algorithms form the backbone of deep learning. When we train neural networks, we aim to minimize a loss function that measures how far our predictions are from actual values. This is achieved through iterative optimization techniques that update model parameters in the direction that reduces the loss.

In the context of Delhi University's BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, understanding adaptive optimization algorithms is crucial for courses on Neural Networks and Deep Learning. This study material covers three fundamental adaptive optimization methods: **AdaGrad**, **RMSProp**, and **Adam** — each representing significant advances in addressing the challenges of gradient-based optimization.

### Real-World Relevance

These optimization algorithms are used in:
- **Computer Vision**: Training CNNs for image classification (e.g., ResNet, VGG)
- **Natural Language Processing**: BERT, GPT, and transformer architectures
- **Autonomous Vehicles**: Real-time decision making with deep reinforcement learning
- **Medical Imaging**: Segmentation and diagnosis systems
- **Recommendation Systems**: Netflix, Amazon, YouTube algorithms

---

## 2. Background: The Challenge of Stochastic Gradient Descent

Traditional **Stochastic Gradient Descent (SGD)** updates parameters as:

$$\theta_{t+1} = \theta_t - \eta \cdot g_t$$

Where:
- $\eta$ = learning rate (fixed)
- $g_t$ = gradient at iteration $t$
- $\theta$ = parameters

### Key Challenges with Vanilla SGD:

1. **Learning Rate Sensitivity**: Fixed learning rate either causes slow convergence or oscillation
2. **Ill-conditioned landscapes**: Loss surfaces with different curvature in different directions
3. **Saddle points**: Algorithms can get stuck at saddle points in high-dimensional spaces
4. **Feature scaling sensitivity**: Performance varies significantly with feature normalization

These challenges led to the development of adaptive learning rate methods.

---

## 3. AdaGrad (Adaptive Gradient Algorithm)

### Concept and Motivation

**AdaGrad**, introduced by Duchi, Hazan, and Singer in 2011, adapts the learning rate for each parameter based on the history of gradients. Parameters that receive large gradients get smaller learning rates, while parameters with small gradients receive larger learning rates.

### Mathematical Formulation

For each parameter $\theta_i$:

**Step 1: Accumulate squared gradients**
$$r_i = r_i + g_i^2$$

**Step 2: Compute update**
$$\Delta\theta_i = -\frac{\eta}{\sqrt{r_i + \epsilon}} \cdot g_i$$

**Step 3: Apply update**
$$\theta_i = \theta_i + \Delta\theta_i$$

Where:
- $g_i$ = gradient for parameter $i$ at current iteration
- $r_i$ = accumulated squared gradients (initialized to 0)
- $\epsilon$ = small constant (typically $10^{-8}$) to prevent division by zero
- $\eta$ = global learning rate

### Intuition

The accumulated squared gradients $r_i$ grow over time. For frequently updated parameters (high gradient magnitude), the effective learning rate decreases. For rarely updated parameters, the learning rate remains higher.

### Pseudocode

```
INPUT: initial parameter θ, learning rate η, 
       constant ε, initial accumulator r = 0
OUTPUT: updated parameters θ

FOR each iteration t:
    FOR each parameter θ_i:
        # Compute gradient
        g_i ← ∇_θ L(θ)  # gradient of loss
        
        # Accumulate squared gradients
        r_i ← r_i + g_i^2
        
        # Compute update (element-wise)
        Δθ_i ← - (η / √(r_i + ε)) * g_i
        
        # Apply update
        θ_i ← θ_i + Δθ_i
    END FOR
END FOR
```

### Advantages of AdaGrad

- **Adaptive Learning Rates**: Automatically adjusts based on gradient history
- **Effective for Sparse Features**: Works well when features are sparse (e.g., NLP, recommender systems)
- **No manual tuning needed**: Eliminates need for separate learning rates per parameter

### Disadvantages

- **Monotonically decreasing learning rate**: The accumulated sum keeps growing, eventually making learning rates extremely small
- **Training can stall**: Model stops learning in later epochs
- **Not suitable for non-convex problems**: Performance degrades over long training periods

### Python Implementation

```python
import numpy as np

class AdaGrad:
    def __init__(self, lr=0.01, epsilon=1e-8):
        self.lr = lr
        self.epsilon = epsilon
        self.cache = {}  # Accumulated squared gradients
    
    def update(self, params, grads, layer_name):
        # Initialize cache for first time
        if layer_name not in self.cache:
            self.cache[layer_name] = np.zeros_like(params)
        
        # Accumulate squared gradients
        self.cache[layer_name] += grads ** 2
        
        # Compute adaptive learning rate
        adjusted_lr = self.lr / (np.sqrt(self.cache[layer_name]) + self.epsilon)
        
        # Update parameters
        updated_params = params - adjusted_lr * grads
        
        return updated_params

# Example usage with a simple gradient
params = np.array([1.0, 2.0, 3.0])
grads = np.array([0.5, -0.3, 0.8])

optimizer = AdaGrad(lr=0.1)
params = optimizer.update(params, grads, 'dense1')
print("Updated params:", params)
```

---

## 4. RMSProp (Root Mean Square Propagation)

### Concept and Motivation

**RMSProp**, developed by Geoffrey Hinton (2012), addresses AdaGrad's main weakness — the monotonically decreasing learning rate. It introduces **exponential moving average** of squared gradients instead of cumulative sum.

### Mathematical Formulation

For each parameter $\theta_i$:

**Step 1: Compute exponential moving average of squared gradients**
$$r_i = \rho \cdot r_i + (1 - \rho) \cdot g_i^2$$

**Step 2: Compute update**
$$\Delta\theta_i = -\frac{\eta}{\sqrt{r_i + \epsilon}} \cdot g_i$$

**Step 3: Apply update**
$$\theta_i = \theta_i + \Delta\theta_i$$

Where:
- $\rho$ (rho) = decay rate (typically 0.9)
- Other variables same as AdaGrad

### Intuition

By using exponential moving average, RMSProp keeps only recent gradient history in memory. This allows the learning rate to adapt dynamically — neither growing unbounded nor shrinking to zero.

### Pseudocode

```
INPUT: initial parameter θ, learning rate η, decay ρ, 
       constant ε, initial moving average r = 0
OUTPUT: updated parameters θ

FOR each iteration t:
    FOR each parameter θ_i:
        # Compute gradient
        g_i ← ∇_θ L(θ)
        
        # Update running average of squared gradients
        r_i ← ρ * r_i + (1 - ρ) * g_i^2
        
        # Compute update
        Δθ_i ← - (η / √(r_i + ε)) * g_i
        
        # Apply update
        θ_i ← θ_i + Δθ_i
    END FOR
END FOR
```

### Key Difference from AdaGrad

| Aspect | AdaGrad | RMSProp |
|--------|---------|---------|
| Gradient accumulation | Cumulative sum | Exponential moving average |
| Learning rate behavior | Always decreases | Can recover if gradient decreases |
| Memory | Grows unbounded | Bounded (uses fixed window) |

### Advantages

- **Non-monotonic learning rates**: Can recover from small learning rates
- **Better for recurrent neural networks**: Widely used in RNNs and LSTMs
- **Handles non-stationary targets**: Good for online learning

### Disadvantages

- **Hyperparameter sensitivity**: Performance depends on $\rho$ and $\eta$ choices
- **Still global learning rate**: All parameters share same $\eta$

### Python Implementation

```python
import numpy as np

class RMSProp:
    def __init__(self, lr=0.001, rho=0.9, epsilon=1e-8):
        self.lr = lr
        self.rho = rho
        self.epsilon = epsilon
        self.cache = {}
    
    def update(self, params, grads, layer_name):
        if layer_name not in self.cache:
            self.cache[layer_name] = np.zeros_like(params)
        
        # Exponential moving average of squared gradients
        self.cache[layer_name] = (self.rho * self.cache[layer_name] + 
                                   (1 - self.rho) * grads ** 2)
        
        # Compute adaptive learning rate
        adjusted_lr = self.lr / (np.sqrt(self.cache[layer_name]) + self.epsilon)
        
        # Update parameters
        updated_params = params - adjusted_lr * grads
        
        return updated_params

# Demonstrate with loss surface optimization
def rosenbrock(x, y):
    """Rosenbrock function - a common test function"""
    return (1 - x)**2 + 100 * (y - x**2)**2

def rosenbrock_grad(x, y):
    """Gradient of Rosenbrock function"""
    dx = -2 * (1 - x) - 400 * x * (y - x**2)
    dy = 200 * (y - x**2)
    return np.array([dx, dy])

# Initialize
x, y = -1.0, 1.0
optimizer = RMSProp(lr=0.01, rho=0.9)

# Train for 1000 iterations
for i in range(1000):
    grads = rosenbrock_grad(x, y)
    x = x - optimizer.lr / (np.sqrt(optimizer.cache.get('w', [0, 0])[0]) + 1e-8) * grads[0]
    # Simplified for demonstration

print(f"Final position: ({x:.4f}, {y:.4f})")
```

---

## 5. Adam (Adaptive Moment Estimation)

### Concept and Motivation

**Adam**, introduced by Kingma and Ba in 2014, combines the benefits of AdaGrad (handling sparse gradients) and RMSProp (handling non-stationary objectives). It computes individual adaptive learning rates from estimates of first and second moments of gradients.

### Mathematical Formulation

Adam maintains two moving averages:

1. **First moment** (m): Estimate of the mean of gradients (like velocity in momentum)
2. **Second moment** (v): Estimate of the uncentered variance of gradients (like RMSProp)

**Algorithm Steps:**

For each parameter $\theta_i$:

**Step 1: Compute gradients**
$$g_i = \nabla_\theta L(\theta)$$

**Step 2: Update first moment estimate (biased toward zero)**
$$m_i = \beta_1 \cdot m_i + (1 - \beta_1) \cdot g_i$$

**Step 3: Update second moment estimate**
$$v_i = \beta_2 \cdot v_i + (1 - \beta_2) \cdot g_i^2$$

**Step 4: Bias correction (important for early iterations)**
$$m_i^{corr} = \frac{m_i}{1 - \beta_1^t}$$
$$v_i^{corr} = \frac{v_i}{1 - \beta_2^t}$$

**Step 5: Compute update**
$$\Delta\theta_i = -\eta \cdot \frac{m_i^{corr}}{\sqrt{v_i^{corr}} + \epsilon}$$

**Step 6: Apply update**
$$\theta_i = \theta_i + \Delta\theta_i$$

Where:
- $\beta_1$ = exponential decay rate for first moment (default: 0.9)
- $\beta_2$ = exponential decay rate for second moment (default: 0.999)
- $\epsilon$ = small constant (default: $10^{-8}$)
- $t$ = iteration counter

### Intuition

- **First moment (m)**: Acts like momentum, dampens oscillations
- **Second moment (v)**: Like RMSProp, scales learning rate by gradient variance
- **Bias correction**: Corrects initialization bias (m and v start at zero)

### Pseudocode

```
INPUT: step size η, exponential decay rates β1, β2,
       initial parameters θ, small constant ε
OUTPUT: updated parameters θ

# Initialize first and second moment vectors
m ← 0  (first moment)
v ← 0  (second moment)
t ← 0  (iteration counter)

WHILE θ not converged:
    t ← t + 1
    g ← ∇_θ L(θ)  # gradient
    
    # Update biased first moment estimate
    m ← β1 * m + (1 - β1) * g
    
    # Update biased second raw moment estimate
    v ← β2 * v + (1 - β2) * g^2
    
    # Compute bias-corrected first moment estimate
    m_corr ← m / (1 - β1^t)
    
    # Compute bias-corrected second raw moment estimate
    v_corr ← v / (1 - β2^t)
    
    # Compute update
    Δθ ← - η * m_corr / (√v_corr + ε)
    
    # Apply update
    θ ← θ + Δθ
END WHILE
```

### Advantages of Adam

- **Combines momentum and adaptive learning rates**: Best of both worlds
- **Bias correction**: More accurate estimates, especially early in training
- **Robust to default hyperparameters**: Works well out-of-the-box
- **Memory efficient**: Only stores two vectors per parameter
- **Excellent for deep neural networks**: Most popular optimizer in practice

### Disadvantages

- **Can converge to suboptimal solutions**: Sometimes in some settings, SGD with momentum performs better
- **More hyperparameters**: $\beta_1$, $\beta_2$ need tuning
- **Generalization gap**: Sometimes generalizes worse than SGD

### Python Implementation

```python
import numpy as np

class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = {}  # First moment
        self.v = {}  # Second moment
        self.t = {}  # Time step per layer
    
    def update(self, params, grads, layer_name):
        # Initialize moment vectors
        if layer_name not in self.m:
            self.m[layer_name] = np.zeros_like(params)
            self.v[layer_name] = np.zeros_like(params)
            self.t[layer_name] = 0
        
        # Increment time step
        self.t[layer_name] += 1
        t = self.t[layer_name]
        
        # Update biased first moment estimate
        self.m[layer_name] = (self.beta1 * self.m[layer_name] + 
                              (1 - self.beta1) * grads)
        
        # Update biased second raw moment estimate
        self.v[layer_name] = (self.beta2 * self.v[layer_name] + 
                              (1 - self.beta2) * (grads ** 2))
        
        # Bias correction
        m_hat = self.m[layer_name] / (1 - self.beta1 ** t)
        v_hat = self.v[layer_name] / (1 - self.beta2 ** t)
        
        # Compute update
        updated_params = params - self.lr * m_hat / (np.sqrt(v_hat) + self.epsilon)
        
        return updated_params

# Complete training example with a neural network
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        np.random.seed(42)
        # Xavier initialization
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))
        self.optimizer = Adam(lr=0.001)
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def relu_derivative(self, x):
        return (x > 0).astype(float)
    
    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.relu(self.z2)  # For demo (use softmax for classification)
        return self.a2
    
    def backward(self, X, y, learning_rate=0.001):
        m = X.shape[0]
        
        # Output layer gradient (simplified for MSE)
        dz2 = (self.a2 - y) * self.relu_derivative(self.z2)
        dW2 = (1/m) * self.a1.T @ dz2
        db2 = (1/m) * np.sum(dz2, axis=0, keepdims=True)
        
        # Hidden layer gradient
        dz1 = (dz2 @ self.W2.T) * self.relu_derivative(self.z1)
        dW1 = (1/m) * X.T @ dz1
        db1 = (1/m) * np.sum(dz1, axis=0, keepdims=True)
        
        # Update using Adam
        self.W1 = self.optimizer.update(self.W1, dW1, 'W1')
        self.b1 = self.optimizer.update(self.b1, db1, 'b1')
        self.W2 = self.optimizer.update(self.W2, dW2, 'W2')
        self.b2 = self.optimizer.update(self.b2, db2, 'b2')

# Generate sample data
np.random.seed(42)
X_train = np.random.randn(100, 10)
y_train = np.random.randn(100, 1)

# Train
model = SimpleNeuralNetwork(10, 20, 1)
for epoch in range(100):
    output = model.forward(X_train)
    model.backward(X_train, y_train)
    if epoch % 20 == 0:
        loss = np.mean((output - y_train) ** 2)
        print(f"Epoch {epoch}, Loss: {loss:.4f}")
```

---

## 6. Comprehensive Comparison

### Algorithm Comparison Table

| Feature | SGD | AdaGrad | RMSProp | Adam |
|---------|-----|---------|----------|------|
| **Adaptive Learning Rate** | ❌ | ✅ | ✅ | ✅ |
| **Momentum** | ❌ | ❌ | ❌ | ✅ |
| **Bias Correction** | N/A | ❌ | ❌ | ✅ |
| **Memory** | O(n) | O(n) | O(n) | O(n) |
| **Sparse Gradients** | Poor | Good | Moderate | Good |
| **Convergence Speed** | Slow | Fast | Fast | Fastest |
| **Default Use Case** | Simple models | Sparse data | RNNs/LSTMs | Default choice |

### When to Use Which?

| Scenario | Recommended Optimizer |
|----------|----------------------|
| Quick prototyping | **Adam** (default choice) |
| Sparse data (NLP, recommender systems) | **AdaGrad** or **Adam** |
| Recurrent Neural Networks | **RMSProp** or **Adam** |
| Computer Vision (production) | **SGD with momentum** |
| Limited computational resources | **Adam** |
| Research/experimentation | **Adam** with weight decay |

---

## 7. Hyperparameter Tuning Guide

### Learning Rate (η)

| Range | Typical Use |
|-------|--------------|
| 0.1 - 1.0 | Simple models, SGD |
| 0.001 - 0.01 | Adam, RMSProp (default: 0.001) |
| 0.0001 | Fine-tuning pretrained models |

### Adam-Specific Hyperparameters

| Parameter | Default | Range | Effect |
|-----------|---------|-------|--------|
| $\beta_1$ | 0.9 | 0.8-0.99 | Controls momentum decay |
| $\beta_2$ | 0.999 | 0.9-0.9999 | Controls variance estimation |
| $\epsilon$ | 1e-8 | 1e-4 to 1e-8 | Numerical stability |

### Practical Tips

1. **Learning Rate Scheduling**: Reduce learning rate by factor of 2-10 when validation loss plateaus
2. **Warm-up**: For Adam, consider learning rate warm-up (start small, increase)
3. **Weight Decay**: Add L2 regularization (weight decay) to prevent overfitting
4. **Gradient Clipping**: Clip gradients to prevent exploding gradients (threshold: 1.0-5.0)

---

## 8. Key Takeaways

1. **AdaGrad** adapts learning rates based on accumulated squared gradients, excellent for sparse features but suffers from monotonically decreasing rates.

2. **RMSProp** improves AdaGrad by using exponential moving average, allowing learning rates to recover and making it suitable for RNNs.

3. **Adam** combines momentum (first moment) with adaptive learning rates (second moment), includes bias correction, and is the most widely used optimizer in deep learning.

4. **Bias correction** in Adam is crucial for early iterations when m and v are initialized to zero.

5. **No universal best optimizer** exists — the choice depends on:
   - Problem type (CV, NLP, RL)
   - Model architecture
   - Dataset size and characteristics
   - Computational constraints

6. **Default starting point**: Use Adam with $\eta=0.001$, $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$.

---

## 9. Challenging MCQs

### Mathematical & Conceptual Questions

**Q1.** In Adam, what is the purpose of bias correction?  
a) To correct for gradient vanishing  
b) To offset initialization bias of m and v being zero  
c) To prevent division by zero  
d) To normalize gradients  

**Answer: b**  
*Explanation: Since m and v are initialized to zero, they are biased toward zero, especially in early iterations. Bias correction divides by (1 - β^t) to offset this.*

---

**Q2.** In AdaGrad, as training progresses, the effective learning rate:  
a) Increases monotonically  
b) Decreases monotonically  
c) Oscillates randomly  
d) Stays constant  

**Answer: b**  
*Explanation: AdaGrad accumulates squared gradients, so the denominator √(r + ε) keeps growing, causing the learning rate to decrease over time.*

---

**Q3.** Which optimizer is most suitable for training RNNs on sequences with vanishing gradient problems?  
a) AdaGrad  
b) SGD with momentum  
c) RMSProp  
d) Vanilla Gradient Descent  

**Answer: c**  
*Explanation: RMSProp's exponential moving average helps adapt to changing gradient magnitudes, making it effective for recurrent networks.*

---

**Q4.** In RMSProp, if ρ (rho) = 0.99, the optimizer gives more weight to:  
a) Recent gradients  
b) Old gradients  
c) Current gradient only  
d) None of the above  

**Answer: b**  
*Explanation: Higher ρ means slower decay, so older gradients have more influence in the moving average.*

---

**Q5.** What is the time complexity of Adam's memory usage?  
a) O(1)  
b) O(t) where t is iterations  
c) O(n) where n is number of parameters  
d) O(n²)  

**Answer: c**  
*Explanation: Adam stores two vectors (m and v) of size equal to the number of parameters.*

---

**Q6.** The first moment estimate in Adam (m) is analogous to:  
a) Velocity in physics  
b) Acceleration in physics  
c) Mass in physics  
d) Position in physics  

**Answer: a**  
*Explanation: Like velocity, the first moment accumulates gradient direction, providing momentum that smooths updates.*

---

**Q7.** If β₁ = 0 and β₂ = 0.999 in Adam, what does it reduce to?  
a) AdaGrad  
b) RMSProp with momentum  
c) Pure RMSProp  
d) Gradient descent  

**Answer: c**  
*Explanation: With β₁ = 0, no momentum is used. With β₂ = 0.999, we have RMSProp's adaptive learning rate.*

---

**Q8.** What happens if ε (epsilon) is set too large in Adam?  
a) Gradients explode  
b) Learning becomes too slow  
c) Model overfits  
d) Nothing changes  

**Answer: b**  
*Explanation: Large ε in denominator makes the adaptive learning rate term smaller, slowing down learning.*

---

## 10. Advanced Flashcards

### Flashcard Set

**Card 1: AdaGrad**  
*Front: What problem does AdaGrad solve?*  
*Back: AdaGrad solves the problem of having different learning rates for different parameters by scaling the learning rate inversely proportional to the square root of the sum of squared historical gradients.*

---

**Card 2: RMSProp**  
*Front: How does RMSProp differ from AdaGrad in gradient accumulation?*  
*Back: RMSProp uses exponential moving average (ρ * old_cache + (1-ρ) * gradient²) instead of cumulative sum. This allows the learning rate to adapt dynamically rather than monotonically decreasing.*

---

**Card 3: Adam**  
*Front: Why is bias correction necessary in Adam?*  
*Back: At iteration t=1, with m and v initialized to zero, the estimates would be biased toward zero. Bias correction by dividing by (1 - β^t) provides unbiased estimates, especially important in early iterations.*

---

**Card 4: Hyperparameters**  
*Front: What are the default values of β₁, β₂, and ε in Adam?*  
*Back: β₁ = 0.9 (momentum decay), β₂ = 0.999 (variance decay), ε = 10⁻⁸ (numerical stability).*

---

**Card 5: Convergence**  
*Front: Why might Adam converge faster than SGD?*  
*Back: Adam combines adaptive learning rates (efficient for different parameter scales) with momentum (helps navigate plateaus and saddle points), leading to faster convergence in most deep learning scenarios.*

---

**Card 6: Generalization**  
*Front: In what scenario might SGD outperform Adam?*  
*Back: In some computer vision tasks, especially with very large datasets, SGD with momentum often achieves better generalization (lower test error) than Adam, though it requires more careful learning rate tuning.*

---

*End of Study Material — Delhi University, BSc (Hons) Computer Science, NEP 2024 UGCF*