# Understanding Data

## Overview

Data is the raw material from which machine learning patterns are extracted and predictions made. Understanding data types, structure, and characteristics is the foundational first step in building successful ML models - the "Garbage In, Garbage Out" principle applies profoundly to ML.

## Key Points

- **Dataset Structure**: Data organized into instances (rows/samples) and features (columns/attributes); an m×n matrix with m instances and n features
- **Numerical Data**: Quantitative measurements - Continuous (height, weight, temperature) or Discrete (counts like number of students)
- **Categorical Data**: Qualitative characteristics - Nominal (no order: gender, color) or Ordinal (ordered: education level, ratings)
- **Structured vs Unstructured**: Structured (tabular, databases, CSV) vs Unstructured (text, images, video, audio)
- **Features vs Labels**: Features (X) are input variables; Label/Target (y) is the output to predict in supervised learning
- **Data Quality**: High-quality, representative data directly determines ML model success

## Important Concepts

- Always examine, visualize, and understand datasets through Exploratory Data Analysis (EDA) before modeling
- Most classic ML algorithms work on structured data; unstructured data requires specialized techniques (NLP for text, Computer Vision for images)
- Understanding data type (numerical/categorical, continuous/discrete, nominal/ordinal) is essential for choosing correct preprocessing and algorithms
- In supervised learning tasks, datasets contain both features (inputs) and labels (desired outputs)

## Notes

- Know how to classify data types - frequently tested in exams
- Be able to identify features vs labels in example datasets
- Understand that data type determines choice of preprocessing techniques and ML algorithms
- Remember the example fruit classification dataset structure
