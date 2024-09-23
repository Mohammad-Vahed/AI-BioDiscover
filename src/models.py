import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(X_train, y_train):
    # Convert sequences to numerical representation (for simplicity, use length here)
    X_train_transformed = np.array([[len(seq)] for seq in X_train])
    model = RandomForestRegressor()
    model.fit(X_train_transformed, y_train)
    return model

def predict(model, X_test):
    X_test_transformed = np.array([[len(seq)] for seq in X_test])
    predictions = model.predict(X_test_transformed)
    return predictions

