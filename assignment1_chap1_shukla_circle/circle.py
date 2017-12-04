import tensorflow as tf
import math
import os

# TensorFlow Assignment 1 Calculate Circumference and Area of Circle using TensorFlow
# Class Discussion Faceebook Group: https://www.facebook.com/groups/deep.learning.edu/

# To shut up the initial warnings messages about not using GPU's etc.
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"

# To define TensorFlow graphs and radius variable
def buildGraphs(radius):
    radius_tensor_var = tf.Variable(radius)
    radius_tensor_var.initializer.run()
    pi_tensor = tf.constant(math.pi)
    diameter_tensor = tf.multiply(radius_tensor_var, tf.constant(2.0))
    circle_circumference_graph = tf.multiply(diameter_tensor, pi_tensor)

    radius_squared_op = tf.pow(radius_tensor_var, 2.0)
    circle_area_graph = tf.multiply(pi_tensor, radius_squared_op)
    return (circle_circumference_graph, circle_area_graph, radius_tensor_var)

defaultRadius = 0.0
sess = tf.InteractiveSession()
circle_circumference_graph, circle_area_graph, radius_tensor_var = buildGraphs(defaultRadius)

while True:
    radius_str = input('Enter the radius of a circle: ')
    radius = float(radius_str)
    tf.assign(radius_tensor_var, radius).eval()
    circumference = circle_circumference_graph.eval()
    area = circle_area_graph.eval()
    print("Circumerence: {} ".format(circumference))
    print("Area: {} ".format(area))
    another = input('Do you want to enter another radius? (Yes)/No):').strip()
    if another == 'No':
        break

sess.close()




