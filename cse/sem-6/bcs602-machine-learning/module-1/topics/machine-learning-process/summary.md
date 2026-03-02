# Machine Learning Process

## Overview

The machine learning process is a systematic, iterative workflow consisting of well-defined stages from problem understanding to production deployment and maintenance. Following this process ensures reliable, reproducible results and successful ML model development.

## Key Points

- **Problem Definition**: Formulate business problem as ML task, define success metrics, determine if ML is appropriate solution
- **Data Collection**: Gather data from multiple sources, ensure quality and compliance with privacy requirements
- **Data Preparation**: Most time-consuming step (60-80%), includes cleaning, EDA, feature engineering, selection, and transformation
- **Model Selection**: Choose algorithm based on problem type, data size, interpretability needs, and computational constraints
- **Model Training**: Split data (train 60-70%, validation 15-20%, test 15-20%), tune hyperparameters using cross-validation
- **Model Evaluation**: Assess performance using appropriate metrics (accuracy/precision/recall for classification, MSE/RMSE/R² for regression)
- **Deployment**: Package model as API, integrate with production systems, implement A/B testing
- **Maintenance**: Monitor performance, detect concept drift and data drift, retrain periodically with fresh data

## Important Concepts

- Train/Validation/Test split: Training builds model, validation tunes hyperparameters, test evaluates final performance
- Feature engineering creates new features from existing data to improve model performance
- Concept drift occurs when real-world data distribution changes; data drift when input characteristics change
- Cross-validation (k-fold) provides robust performance estimation during training

## Notes

- Draw the ML pipeline flowchart - commonly asked in exams
- Memorize evaluation metrics for classification vs regression vs clustering
- Understand why each dataset split is needed and typical ratios
- Know the difference between concept drift and data drift for maintenance questions
