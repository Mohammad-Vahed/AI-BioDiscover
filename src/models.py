import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def train_model(X_train, y_train, model_type='RandomForest', params=None):
    """
    Train a machine learning model based on the specified model type.
    
    Args:
        X_train: Training feature data.
        y_train: Training target data.
        model_type: The type of model to train ('RandomForest', 'LinearRegression', 'SVR').
        params: Hyperparameters for model tuning.

    Returns:
        Trained model.
    """
    # Convert sequences to numerical representation
    X_train_transformed = np.array([[len(seq)] for seq in X_train])
    
    # Define the model based on the model_type argument
    if model_type == 'RandomForest':
        model = RandomForestRegressor()
    elif model_type == 'LinearRegression':
        model = LinearRegression()
    elif model_type == 'SVR':
        model = SVR()
    else:
        raise ValueError("Unsupported model type. Choose 'RandomForest', 'LinearRegression', or 'SVR'.")
    
    # If hyperparameters are provided, use GridSearchCV for tuning
    if params:
        model = GridSearchCV(model, params, cv=5, scoring='neg_mean_squared_error')
    
    # Fit the model
    model.fit(X_train_transformed, y_train)
    
    return model

def predict(model, X_test):
    """
    Make predictions using the trained model.
    
    Args:
        model: The trained model.
        X_test: Test feature data.

    Returns:
        Predictions.
    """
    X_test_transformed = np.array([[len(seq)] for seq in X_test])
    predictions = model.predict(X_test_transformed)
    return predictions
