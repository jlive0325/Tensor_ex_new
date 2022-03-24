import tensorflow as tf
# tf.__version__

hello = tf.constant('Hello, TensorFlow!')
git = tf.constant('Hello, Git')

# sess = tf.Session()
tf.print(hello)
tf.print(git)

a = tf.constant(10)
b = tf.constant(32)
tf.print(a+b)

# sess.close()

""" import tensorflow as tf
tf.__version__ """

""" import tensorflow as tf
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)

tf.print(node1,node2) """