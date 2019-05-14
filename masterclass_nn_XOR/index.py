# The only dependency. It is necessary for some matrix (table like data storage) operations.
import numpy as np

# Define random seed for reproducability (Random numbers will be the same when rerunning the code)
np.random.seed(3)

# Define input and targets
# X and y consist of 4 different examples. THe index of the arrays correspond to each other
# The statement we are testing is XOR, meaning that if ONE of the two inputs is a 1, the output should be
# a 1. Otherwise it should result in 0.
X = np.array([[[0, 0]], [[1, 0]], [[0, 1]], [[1, 1]]])
y = np.array([[0], [1], [1], [0]])

# Structure of the network
input_nodes = 2
hidden_nodes = 2
output_nodes = 1

# Define the learning rate
# This rate is chosen arbitrarily. You can play around with the rate to see how it affects the neural network learning process
learning_rate = 0.15

# Number of iterations
# Also arbitrarily chosen.
iterations = 50000

# Initialize weights and biases
# THe weights and biases are initialized randomly, and will be trained later on.
W1 = np.random.randn(input_nodes, hidden_nodes)
b1 = np.random.randn(1, hidden_nodes)
W2 = np.random.randn(hidden_nodes, output_nodes)
b2 = np.random.randn(1, output_nodes)

# Define the actiation function
# This is done to make sure the network calculations do not overflow, by keeping the activations between 0 and 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Define the derivative of activations function
# To calculate the gradient of the errors. Google for Gradient Descent in order to find out more.
def deriv_sigmoid(x):
    return x * (1 - x)


# Define the feedforward function
def feedforward(X, predict=False):

    # Calculate the activations at the hidden layer and the output layer.
    hidden_activations = sigmoid(X.dot(W1) + b1)
    output_activations = sigmoid(hidden_activations.dot(W2) + b2)

    # If we want to return the prediction:
    if predict:
        return int(np.round(output_activations))

    return hidden_activations, output_activations


# Define backprop function for updating weights
def backpropagation(X, y):

    # Needed to be able to adjust the variables
    global W1
    global b1
    global W2
    global b2

    # Call the feedforward to get the activations
    hidden_activations, output_activations = feedforward(X)

    # Calculate the errors at every layer
    # Also Google this to find out more
    output_error = 2 * (y - output_activations)
    hidden_error = output_error * W2.T

    # Calculate the updates for output weights / biases
    # This is where the magic happens at aneural network. This complete process is the actual
    # backpropagation. This is important to understand if you truly want to know how a NN functions.
    b2_update = (output_error * deriv_sigmoid(output_activations)) * learning_rate
    W2_update = hidden_activations.T.dot(b2_update)

    # Calculate the updates for hidden weights / biases
    b1_update = (hidden_error * deriv_sigmoid(hidden_activations)) * learning_rate
    W1_update = X.T.dot(b1_update)

    # Update all respective weights and biases
    W1 += W1_update
    b1 += b1_update
    W2 += W2_update
    b2 += b2_update


def train(iterations):

    for i in range(iterations):
        # Randomly choose an example to train on
        # Its important to do this randomly, as other wise the network learns to predict the 'next' item in each list,
        # which is definitely not what you want. You want it to be smart.
        index = np.random.randint(0, 4)
        backpropagation(X[index], y[index])

    print('Prediction for ', X[0], 'is: ', feedforward(X[0], predict=True))
    print('Prediction for ', X[1], 'is: ', feedforward(X[1], predict=True))
    print('Prediction for ', X[2], 'is: ', feedforward(X[2], predict=True))
    print('Prediction for ', X[3], 'is: ', feedforward(X[3], predict=True))

train(iterations)
