import tensorflow as tf

# Needed to configure parallel computing
config = tf.ConfigProto(inter_op_parallelism_threads=8)

# Defining different graphs (not very common)
g = tf.Graph()
f = tf.Graph()

with g.as_default():

    x = 3
    y = 2

    op1 = tf.add(x, y)
    op2 = tf.multiply(x, y)
    op3 = tf.pow(op1, op2)

# Graph to be initialized in sessions
with tf.Session(config=config, graph=g) as sess:

    print(sess.run(op3))
