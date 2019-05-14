import numpy as np

np.random.seed(3)

##############################################
# The following parameters should be tweaked #
##############################################

hidden_nodes = 6
learning_rate = 0.5

##########################################
# The normal execution of neural network #
##########################################

X = np.array([
    [[0, 0]],
    [[1, 0]],
    [[0, 1]],
    [[1, 1]]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])


total_loss = 0


def initialize_weights(hidden_nodes):
    input_nodes = 2
    output_nodes = 1

    W1 = np.random.randn(input_nodes, hidden_nodes)
    b1 = np.random.randn(1, hidden_nodes)
    W2 = np.random.randn(hidden_nodes, output_nodes)
    b2 = np.random.randn(1, output_nodes)

    return W1, b1, W2, b2


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    return x * (1 - x)


def feedforward(X, predict=False):
    hidden_activations = sigmoid(X.dot(W1) + b1)
    output_activations = sigmoid(hidden_activations.dot(W2) + b2)

    if predict:
        print(output_activations)
        prediction = int(np.round(output_activations))
        return prediction

    return hidden_activations, output_activations


def backpropagation(X, y, learning_rate):

    global W1, b1, W2, b2, total_loss

    hidden_activations, output_activations = feedforward(X)

    output_error = 2 * (y - output_activations)
    hidden_error = output_error * W2.T
    total_loss += np.abs(output_error)

    b2_update = output_error * \
        deriv_sigmoid(output_activations) * learning_rate
    W2_update = hidden_activations.T.dot(b2_update)
    b1_update = hidden_error * \
        deriv_sigmoid(hidden_activations) * learning_rate
    W1_update = X.T.dot(b1_update)

    W1 += W1_update
    b1 += b1_update
    W2 += W2_update
    b2 += b2_update


def train(learning_rate):

    for i in range(10000):
        index = np.random.randint(0, 4)
        backpropagation(X[index], y[index], learning_rate)

    predictions = []

    for i in range(4):
        if feedforward(X[i], predict=True) == 0:
            predictions.append('true')
        else:
            predictions.append('false')

    return total_loss, predictions


for i in range(1):
    # hidden_nodes += 1

    learning_rate = 1

    for i in range(1):
        total_loss = 0
        W1, b1, W2, b2 = initialize_weights(hidden_nodes)
        # learning_rate += 0.1
        loss, predictions = train(learning_rate)
        print('Network with ', hidden_nodes,  'nodes and ',
              learning_rate, 'lr has ', loss,  'loss in total')
        # print(predictions)
