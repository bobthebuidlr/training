# Import dependencies
import numpy as np

# Define random seed (to make results the same every time)
np.random.seed(3)

# Input and output
X = np.array([
    [[1, 0]],
    [[0, 1]],
    [[0, 0]],
    [[1, 1]]
])

y = np.array([
    [1],
    [1],
    [0],
    [0]
])

# Structure of the network
input_nodes = 2
hidden_nodes = 2
output_nodes = 1

# Initialize weights and biases
W1 = np.random.randn(input_nodes, hidden_nodes)
b1 = np.random.randn(1, hidden_nodes)
W2 = np.random.randn(hidden_nodes, output_nodes)
b2 = np.random.randn(1, output_nodes)

# Define mathmatical calculations
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
    return x * (1 - x)

# Feedforward
def feedforward(X, predict=False):
    hidden_activations = sigmoid(X.dot(W1) + b1)
    output_activations = sigmoid(hidden_activations.dot(W2) + b2)

    if predict:
        print(output_activations)
        prediction = int(np.round(output_activations))
        return prediction

    return hidden_activations, output_activations

# Backpropagation
def backpropagation(X, y):
    global W1, W2, b1, b2

    hidden_activations, output_activations = feedforward(X)

    # calculate the errors
    output_error = 2 * (y - output_activations)
    hidden_error = output_error * W2.T

    # Calculate the updates
    b2_update = output_error * deriv_sigmoid(output_activations) * 0.1
    W2_update = hidden_activations.T.dot(b2_update)
    b1_update = hidden_error * deriv_sigmoid(hidden_activations) * 0.1
    W1_update = X.T.dot(b1_update)

    # Update the weights
    W1 += W1_update
    b1 += b1_update
    W2 += W2_update
    b2 += b2_update

# Training and prediction
def train():

    for i in range(30000):
        index = np.random.randint(0, 4)
        backpropagation(X[index], y[index])            
    
    print(feedforward(X[0], predict=True))
    print(feedforward(X[1], predict=True))
    print(feedforward(X[2], predict=True))
    print(feedforward(X[3], predict=True))

train()