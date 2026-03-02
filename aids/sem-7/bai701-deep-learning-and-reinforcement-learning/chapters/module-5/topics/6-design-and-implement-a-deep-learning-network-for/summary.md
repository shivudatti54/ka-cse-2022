# **Deep Learning for Time Series Forecasting**

## **Introduction**

- Time series forecasting: predicting future values in a sequence of data
- Deep learning networks: widely used for time series forecasting

## **Key Concepts**

- **Autoregressive Integrated Moving Average (ARIMA) model**:
  - AR: past values affect current
  - I: differencing to remove trends
  - MA: past errors affect current
- **LSTM (Long Short-Term Memory) network**:
  - Recurrent neural network (RNN) architecture
  - Memory cells for storing information
- **Graph Convolutional Network (GCN)**:
  - Graph-based architecture for time series forecasting

## **Important Formulas and Definitions**

- **Mean Absolute Error (MAE)**: $\frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$
- **Mean Squared Error (MSE)**: $\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
- **Root Mean Squared Percentage Error (RMSPE)**: $\sqrt{\frac{1}{n} \sum_{i=1}^{n} \frac{(y_i - \hat{y}_i)^2}{y_i}}$
- **Recurrent Neural Network (RNN)**: neural network with feedback connections

## **Design and Implementation**

- **Data Preparation**:
  - Feature scaling
  - Data normalization
- **Model Architecture**:
  - Choose a suitable architecture (e.g., LSTM, GCN)
  - Define hyperparameters (e.g., number of layers, number of units)
- **Training and Evaluation**:
  - Train the model using backpropagation
  - Evaluate using metrics (e.g., MAE, MSE, RMSPE)

## **Theorems and Results**

- **No Free Lunch Theorem**:
  - no single algorithm is universally optimal
  - best algorithm depends on problem and data
