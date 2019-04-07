import numpy as np

np.random.seed(3)

# Input to work with
X = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
y = np.array([[0], [1], [1], [0]])


# Functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative_of_sigmoid(x):
    return x * (1 - x)


# Structure of the network
input_nodes = 2
hidden_nodes = 2
output_nodes = 2

# Initialize weights and biases
W1 = np.random.randn(hidden_nodes, input_nodes)
b1 = np.random.randn(hidden_nodes, 1)

W2 = np.random.randn(output_nodes, hidden_nodes)
b2 = np.random.randn(output_nodes, 1)

learning_rate = 0.1


def feedforward(X, predict=False):

    print(X.shape, W1.shape, b1.shape)

    # Generate hidden activations
    hidden_z = np.dot(W1, X) + b1
    hidden_a = sigmoid(hidden_z)

    # Generate output activations
    output_z = np.dot(W2, hidden_a) + b2
    output_a = sigmoid(output_z)

    print(output_a)

    if predict:
        return output_a

    return hidden_z, hidden_a, output_z, output_a


def backpropagation2(X, y, W1, b1, W2, b2):
    hidden_z, hidden_a, output_z, output_a = feedforward(X)
    X = X.reshape((1, 2))
    # print('X shape: ', X.shape)

    output_error = 2 * (output_a - y)
    output_gradients = derivative_of_sigmoid(output_a)
    output_gradients *= output_error
    output_gradients *= learning_rate

    # print('Output gradients shape: ', output_gradients.shape)
    #
    output_deltas = output_gradients.dot(hidden_a)
    # print('Output deltas shape: ', output_deltas.shape)

    W1 += output_deltas
    b1 += output_gradients

    # print('W2 shape: ', W2.shape)
    #
    hidden_error = W2.dot(output_error)

    print('Hidden error shape: ', hidden_error.shape)
    print('Hidden activations shape: ', hidden_a.shape)
    hidden_gradients = derivative_of_sigmoid(hidden_a.T)
    hidden_gradients *= hidden_error
    hidden_gradients *= learning_rate
    print('Hidden gradients shape: ', hidden_gradients.shape)

    print('Hidden gradients: ', hidden_gradients.shape)

    hidden_deltas = hidden_gradients.dot(X)

    b2 += hidden_gradients
    W2 += hidden_deltas

    print(hidden_deltas)


def backpropagation(X, y, W1, b1, W2, b2):
    hidden_z, hidden_a, output_z, output_a = feedforward(X)
    X = X.reshape((1, 2))

    output_error = 2 * (output_a - y)
    output_gradients = derivative_of_sigmoid(output_a)
    output_gradients = output_gradients.dot(output_error)
    output_gradients *= learning_rate

    output_deltas = hidden_a.T.dot(output_gradients)

    hidden_error = W2.T.dot(output_error)

    print(hidden_error)
    hidden_gradients = derivative_of_sigmoid(hidden_a)
    hidden_gradients = hidden_gradients.T.dot(hidden_error)
    hidden_gradients *= learning_rate

    print(hidden_gradients.shape)
    #
    # hidden_deltas = X.T.dot(hidden_gradients)
    #
    # print(hidden_deltas.shape)
    #
    # print(hidden_gradients.shape, hidden_error.shape)

hidden_z, hidden_a, output_z, output_a = feedforward(X[0])

# backpropagation(X[1], y[1], W1, b1, W2, b2)
