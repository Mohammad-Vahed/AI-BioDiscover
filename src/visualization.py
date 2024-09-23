import matplotlib.pyplot as plt

def plot_results(y_test, predictions):
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.title('True vs Predicted Values')
    plt.show()
