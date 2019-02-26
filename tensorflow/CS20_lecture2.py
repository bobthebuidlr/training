import tensorflow as tf
import numpy as np

def part1():

    # You can provide names for the graph variables
    a = tf.constant(2, name="alpha")
    b = tf.constant(3, name="beta")

    # There are multiple kinds of constants that you can use!
    c1 = tf.constant(2, shape=[2, 2], verify_shape=False, name="Shaped Constant")

    c = tf.add(a, b, name="add")

    with tf.Session() as sess:

        # Use the following line to visualize using TensorBoard
        # writer = tf.summary.FileWriter('./graphs', sess.graph)

        print(sess.run(c1))

    # writer.close() # Close the writer when done


def part2():

    # Playing around with constants and scalar matrices
    a = tf.constant([[2, 2], [3, 7]], name="a")
    b = tf.constant([1, 2], name="b")

    # Similar to np.add()
    c = tf.add(b, a, name="c")

    # Similar to np.dot()
    d = tf.multiply(a, b, name="d")

    with tf.Session() as s:
        print(s.run(d))


def part3():

    # Similar to np.zeros()
    a = tf.zeros([2, 2])
    b = tf.constant([[2, 6, 5], [3, 1, 4]])

    # Similar to np.zeros_like()
    c = tf.zeros_like(b)

    # Filling an array with scalar numbers
    d = tf.fill([4, 2], 0.5, name="d")

    with tf.Session() as sess:

        writer = tf.summary.FileWriter('./graphs', sess.graph)
        print(sess.run(d))
        writer.close()


def part4():

    # Creating an array with floats in given range
    a = tf.linspace(10.0, 17.5, 5, name="a")

    # Defining a certain interval within range
    b = tf.range(3, 31, delta=0.70, name="b")

    with tf.Session() as sess:

        print(sess.run(b))


# Defining random constants
def part5():

    # Normally distributed
    a = tf.random_normal([3,5], stddev=1.0)

    # Normally distributed, ALL VALUES WITHIN 2 STD
    b = tf.truncated_normal([3, 5])

    # Shuffling the values within a matrix
    c1 = tf.constant([[3, 6], [4, 8]])
    c2 = tf.random_shuffle(c1, name="c2")

    # Multinomial dist
    d = tf.constant(np.random.normal(size=(3, 4)))
    d2 = tf.multinomial(d, 20)

    # Random gammas
    e = tf.random_gamma([10], [5,15])

    with tf.Session() as sess:

        print(sess.run(e))


def part6():

    a = tf.constant([3, 6])
    b = tf.constant([2, 2])

    c1 = tf.add_n([a, b, b])
    # c2 = tf.matmul(a, b)
    c3 = tf.multiply(a, b)
    c4 = tf.matmul(tf.reshape(b, [1, 2]), tf.reshape(a, [2, 1]))
    c5 = tf.div(a, b)
    c6 = tf.mod(a, b)

    with tf.Session() as sess:

        print(sess.run(c5))



def part7():

    t_0 = 19
    c1 = tf.zeros_like(t_0)
    c2 = tf.ones_like(t_0)

    t_1 = ['apple', 'banana', 'orange']
    c3 = tf.zeros_like(t_1)
    # c4 = tf.ones_like(t_1) # This throws an error

    with tf.Session() as sess:

        print(sess.run(c3))


def part8():

    a = tf.constant([1.0, 2.0], name="a")

    with tf.Session() as sess:

        print(sess.graph.as_graph_def())


def part9():

    a = tf.Variable(2, name="my_var")

    b = a.assign((2 * a.value()))

    with tf.Session() as sess:

        writer = tf.summary.FileWriter(sess.graph)
        print(sess.run(b))
        writer.close()


# Variables have to be INITIALIZED!
def part10():

    a = tf.Variable(tf.truncated_normal([12, 4]))
    b = tf.Variable(2 * a)

    with tf.Session() as sess:

        sess.run(tf.global_variables_initializer())

        print(a.eval())
        print(b.eval())


# Working with placeholders
def part11():

    a = tf.placeholder(tf.float32, shape=[3])
    b = tf.constant([5, 5, 5], tf.float32)
    input = [[1, 2, 3], [4, 5, 6]]
    c = a + b

    with tf.Session() as sess:

        for array in input:
            print(sess.run(c, {a: array}))


# Replacing values
def part12():

    a = tf.add(2, 5)
    b = tf.multiply(a, 5)

    with tf.Session() as sess:

        replace_dict = {a: 15}

        print(sess.run(b, feed_dict=replace_dict))


# Lazy loading -> Only eage variable if needed -> Bloats up graphs
def part13():

    x = tf.Variable(10, name="x")
    y = tf.Variable(20, name="y")

    with tf.Session() as sess:

        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter('./graphs', sess.graph)
        for _ in range(10):
            print(sess.run(tf.add(x, y)))
        writer.close()

part13()


