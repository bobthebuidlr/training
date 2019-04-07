# Import dependencies
import numpy as np

np.random.seed(3)


# Function definitions -> Sigmoid and derivative of sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative_of_sigmoid(x):
    return x * (1 - x)


# Input
X = np.array([[[0, 0]], [[1, 0]], [[0, 1]], [[1, 1]]])

# Labels (output)
y = np.array([[0], [1], [1], [0]])

# Structure the network
input_nodes = 2
hidden_nodes = 3
output_nodes = 1

W1 = np.random.rand(hidden_nodes, input_nodes)
W2 = np.random.rand(output_nodes, hidden_nodes)

b1 = np.random.rand(hidden_nodes, 1)
b2 = np.random.rand(output_nodes, 1)

parameters = {
    "W1": W1,
    "b1": b1,
    "W2": W2,
    "b2": b2
}


# Training (feedforward + backpropagation)
def feedforward(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]

    Z1 = X.dot(W1) + b1
    A1 = sigmoid(Z1)
    Z2 = A1.dot(W2) + b2
    A2 = sigmoid(Z2)

    cache = {
        "a1": A1,
        "a2": A2
    }
    return A2, cache


def backpropagation(X, y, cache, parameters):
    A1 = cache["A1"]
    A2 = cache["A2"]

    W2 = parameters["W2"]

    dZ2 = A2 - y
    dW2 = np.dot(dZ2, A1.T)


    hidden_activations, output_activations = feedforward(input)
    print('Hidden activations: ', hidden_activations)
    print('Output activations: ', output_activations)
    error_derivative = 2 * (output_activations - target)
    activation_derivative = derivative_of_sigmoid(output_activations)
    hidden_gradients = np.dot(activation_derivative, error_derivative)
    print('Hidden gradients: ', hidden_gradients)
    hidden_deltas = np.dot(hidden_activations.T, hidden_gradients)
    print('Hidden deltas: ', hidden_deltas)

    # prev_activations = hidden_activations
    #
    # hidden_deltas = prev_activations * activation_derivative * error_derivative
    # print(hidden_deltas)

    # print('error: ', error)
    # output_deltas = derivative_of_sigmoid(output) * error
    # output_weights_errors = output_deltas.dot(hidden_activations.T)
    #
    # hidden_deltas = derivative_of_sigmoid(hidden_activations.T) * output_weights_errors
    # hidden_weights_errors = hidden_deltas.dot(input.T)
    #
    # return error, output_weights_errors, hidden_deltas, hidden_weights_errors


# Evaluation
backpropagation(X[0], y[0])
