from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(y_test, predictions):
    """
    Evaluate the model's performance using various metrics.
    
    Args:
        y_test: True target values.
        predictions: Predicted values.

    Returns:
        Dictionary of evaluation metrics.
    """
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')
    print(f'Mean Absolute Error: {mae}')

    return {
        'MSE': mse,
        'R2': r2,
        'MAE': mae
    }

def plot_results(y_test, predictions):
    """
    Plot the true vs predicted values.
    
    Args:
        y_test: True target values.
        predictions: Predicted values.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=predictions)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('True vs Predicted Values')
    plt.xlim([min(y_test), max(y_test)])
    plt.ylim([min(y_test), max(y_test)])
    plt.grid()
    plt.show()
