import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train, X_test = np.array(y_train), np.array(X_test)
    n = len(X_test)
    frequencies, count = np.unique(y_train, return_counts=True)
    idx = frequencies[np.argmax(count)]
    C = np.full([n], idx)
    return C