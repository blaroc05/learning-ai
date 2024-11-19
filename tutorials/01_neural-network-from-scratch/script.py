import numpy as np
import matplotlib.pyplot as plt

# Dataset: Features and Labels
X = np.array([
    [25, 2],
    [50, 4],
    [75, 6],
    [30, 1],
    [90, 8],
    [45, 3],
    [60, 7],
    [20, 1],
    [85, 9],
    [35, 4]
]).T  # Shape (2, 10)

Y = np.array([
    0, 0, 1, 0, 1, 0, 1, 0, 1, 0
]).reshape(1, -1)  # Shape (1, 10)

plt.scatter(X[0], X[1], c=Y.flatten(), cmap='viridis', s=50)
plt.xlabel("Income (in $1000s)")
plt.ylabel("Time Spent on Website (minutes)")
plt.title("Customer Data: Income vs. Time Spent")
plt.colorbar(label="Bought Product (0 = No, 1 = Yes)")
plt.show()

X = X / np.max(X, axis=1, keepdims=True)  # Normalize features to [0, 1]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(1)
    W1 = np.random.randn(hidden_size, input_size) * 0.01
    b1 = np.zeros((hidden_size, 1))
    W2 = np.random.randn(output_size, hidden_size) * 0.01
    b2 = np.zeros((output_size, 1))
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

def forward_propagation(X, parameters):
    W1, b1, W2, b2 = parameters["W1"], parameters["b1"], parameters["W2"], parameters["b2"]
    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)  # Sigmoid activation
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

def compute_loss(predictions, Y):
    m = Y.shape[1]
    loss = -np.sum(Y * np.log(predictions) + (1 - Y) * np.log(1 - predictions)) / m
    return np.squeeze(loss)

def backward_propagation(X, Y, parameters, cache):
    m = X.shape[1]
    W2 = parameters["W2"]
    A1, A2 = cache["A1"], cache["A2"]

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / m
    db2 = np.sum(dZ2, axis=1, keepdims=True) / m

    dZ1 = np.dot(W2.T, dZ2) * (1 - np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m

    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

def update_parameters(parameters, gradients, learning_rate):
    for key in parameters.keys():
        parameters[key] -= learning_rate * gradients["d" + key]
    return parameters

def train(X, Y, input_size, hidden_size, output_size, epochs, learning_rate):
    parameters = initialize_parameters(input_size, hidden_size, output_size)
    loss_history = []

    for epoch in range(epochs):
        A2, cache = forward_propagation(X, parameters)
        loss = compute_loss(A2, Y)
        gradients = backward_propagation(X, Y, parameters, cache)
        parameters = update_parameters(parameters, gradients, learning_rate)
        loss_history.append(loss)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return parameters, loss_history

parameters, loss_history = train(X, Y, input_size=2, hidden_size=2, output_size=1, epochs=5000, learning_rate=0.01)

# Plot loss
plt.plot(loss_history)
plt.title("Loss Over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

# Predictions
predictions, _ = forward_propagation(X, parameters)
print("Predictions (binary):", (predictions > 0.5).astype(int))
