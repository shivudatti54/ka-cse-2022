# **6.4 Ch: Model Identification**

## **Introduction**

Model identification is a crucial step in time series analysis, as it enables us to select the most suitable model that can accurately forecast future values. In this section, we will discuss the objectives of identification, identification techniques, and initial considerations.

## **Objectives of Identification**

The primary objectives of model identification are:

- **Accuracy**: To select a model that can accurately forecast future values.
- **Simplicity**: To choose a model that is simple and easy to understand.
- **Generalizability**: To select a model that can generalize well to new data.

## **Identification Techniques**

There are several identification techniques used to select a suitable model. Some of the most common techniques include:

- **Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF)**:
  - ACF plots the correlation between each time series observation and the previous one.
  - PACF plots the correlation between each time series observation and all previous ones.
  - Both ACF and PACF can be used to identify the order of the autoregressive (AR) and moving average (MA) components.
- **Information Criteria**:
  - **Akaike Information Criterion (AIC)**: A measure of the relative quality of models.
  - **Bayesian Information Criterion (BIC)**: A measure of the relative quality of models.
  - Both AIC and BIC can be used to compare the performance of different models.
- **Cross-Validation**:
  - A method of evaluating the performance of a model by splitting the data into training and testing sets.

## **Initial Considerations**

Before selecting a model, consider the following initial factors:

- **Data Quality**: Ensure that the data is clean, complete, and free of outliers.
- **Model Assumptions**: Check that the model assumptions (e.g., stationarity, linearity) are met.
- **Model Complexity**: Consider the complexity of the model and its potential impact on the forecast accuracy.

## **Example**

Suppose we have a time series dataset with 12 observations. We can use the ACF and PACF plots to identify the order of the AR and MA components.

| Time | Value |
| ---- | ----- |
| 1    | 10    |
| 2    | 12    |
| 3    | 15    |
| 4    | 18    |
| 5    | 20    |
| 6    | 22    |
| 7    | 25    |
| 8    | 28    |
| 9    | 30    |
| 10   | 32    |
| 11   | 35    |
| 12   | 38    |

The ACF plot shows a significant correlation at lag 1 and 2, indicating an AR(2) model. The PACF plot shows a significant spike at lag 1, indicating an MA(1) component.

By considering these factors and using identification techniques, we can select a suitable model that can accurately forecast future values.

## **Key Concepts**

- **Autocorrelation Function (ACF)**: A plot of the correlation between each time series observation and the previous one.
- **Partial Autocorrelation Function (PACF)**: A plot of the correlation between each time series observation and all previous ones.
- **Akaike Information Criterion (AIC)**: A measure of the relative quality of models.
- **Bayesian Information Criterion (BIC)**: A measure of the relative quality of models.
- **Cross-Validation**: A method of evaluating the performance of a model by splitting the data into training and testing sets.
- **Autoregressive (AR)**: A model that assumes the current value is a function of past values.
- **Moving Average (MA)**: A model that assumes the current value is a function of past errors.
- **Stationarity**: A property of a time series that describes the constancy of its statistical characteristics over time.
- **Linearity**: A property of a model that describes the relationship between its inputs and outputs.
