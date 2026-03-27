# Restaurant Rating Predictor

A machine learning web application that predicts restaurant review categories using structured input features.  
This project demonstrates end-to-end ML pipeline development, model deployment, and interactive application design.


# Project Objective

The goal of this project was to build a predictive system capable of classifying restaurant ratings based on key operational and customer-related attributes.

This project showcases:
- Data preprocessing
- Supervised machine learning modeling
- Model evaluation and optimization
- Model serialization and deployment
- Web-based user interaction using Streamlit

## Technical Implementation

### Data Processing
- Cleaned and structured raw dataset
- Handled missing values and categorical encoding
- Applied feature scaling using `StandardScaler`

### Model Development
- Trained classification model using Scikit-learn
- Evaluated performance using appropriate metrics
- Optimized model for generalization

### Deployment
- Serialized trained model using `joblib`
- Built interactive front-end with Streamlit
- Integrated saved model for real-time predictions

## Python Libraries

- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
