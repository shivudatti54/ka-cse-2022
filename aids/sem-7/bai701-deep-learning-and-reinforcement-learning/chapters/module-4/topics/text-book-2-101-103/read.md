# Text Book – 2: 10.1-10.3

## Recurrent Neural Networks (RNNs)

### Definition and Purpose

A Recurrent Neural Network (RNN) is a type of neural network designed to handle sequential data, such as time series data, speech, or text. RNNs are trained to learn patterns in the data and make predictions or take actions based on that data.

### Key Concepts

- **Recurrent Connection**: A connection between neurons that allows them to retain information from previous time steps.
- **Hidden State**: A variable that captures the internal state of the RNN, used to make predictions or take actions.
- **Unroll**: A process of flattening the RNN's structure to make it easier to train.

### Types of RNNs

- **Simple RNN**: Uses a simple weight matrix to compute the hidden state.
- **Long Short-Term Memory (LSTM) Network**: A type of RNN that uses memory cells to learn long-term dependencies.
- **Gated Recurrent Unit (GRU) Network**: A type of RNN that uses gates to control the flow of information.

### Example Use Cases

- **Language Modeling**: RNNs can be used to predict the next word in a sentence, given the context of the previous words.
- **Speech Recognition**: RNNs can be used to recognize spoken words and convert them into text.
- **Time Series Prediction**: RNNs can be used to predict future values in a time series data.

## 10.2 Recurrent Neural Networks with Long Short-Term Memory (RNN-LSTM)

### Definition and Purpose

A Recurrent Neural Network with Long Short-Term Memory (RNN-LSTM) is a type of RNN that uses memory cells to learn long-term dependencies in the data. RNN-LSTMs are designed to handle sequential data with long-term dependencies.

### Key Concepts

- **Memory Cell**: A cell that captures the long-term dependencies in the data.
- **Gate Mechanism**: A mechanism that controls the flow of information into and out of the memory cell.
- **Cell State**: The state of the memory cell, used to store the long-term dependencies.

### Architecture of an RNN-LSTM

- **Input Gate**: Controls the flow of new information into the memory cell.
- **Cell State**: Stores the long-term dependencies in the data.
- **Output Gate**: Controls the flow of information out of the memory cell.

### Example Use Cases

- **Language Modeling**: RNN-LSTMs can be used to predict the next word in a sentence, given the context of the previous words.
- **Speech Recognition**: RNN-LSTMs can be used to recognize spoken words and convert them into text.
- **Time Series Prediction**: RNN-LSTMs can be used to predict future values in a time series data.

## 10.3 Recurrent Neural Networks with Gated Recurrent Units (RNN-GRU)

### Definition and Purpose

A Recurrent Neural Network with Gated Recurrent Units (RNN-GRU) is a type of RNN that uses gates to control the flow of information. RNN-GRU networks are designed to handle sequential data with long-term dependencies.

### Key Concepts

- **Gate Mechanism**: A mechanism that controls the flow of information into and out of the memory cell.
- **Cell State**: The state of the memory cell, used to store the long-term dependencies.
- **Reset Gate**: A gate that resets the memory cell to zero at each time step.

### Architecture of an RNN-GRU

- **Input Gate**: Controls the flow of new information into the memory cell.
- **Cell State**: Stores the long-term dependencies in the data.
- **Output Gate**: Controls the flow of information out of the memory cell.
- **Reset Gate**: Resets the memory cell to zero at each time step.

### Example Use Cases

- **Language Modeling**: RNN-GRU networks can be used to predict the next word in a sentence, given the context of the previous words.
- **Speech Recognition**: RNN-GRU networks can be used to recognize spoken words and convert them into text.
- **Time Series Prediction**: RNN-GRU networks can be used to predict future values in a time series data.
