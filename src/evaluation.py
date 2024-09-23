from sklearn.metrics import mean_squared_error

def evaluate_model(y_test, predictions):
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    return mse
