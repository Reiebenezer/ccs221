import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

tf.compat.v1.disable_eager_execution()

def _plt_basic_object_(points):
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:, 2],
                        triangles=tri,
                        shade=True, cmap=cm.Spectral, lw=0.5)

    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)

    st.pyplot(fig)

def _cube_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],

        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
        
    ])

    return points

def _pyramid_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        
        bottom_lower + [side_length/2, side_length/2, side_length],
        bottom_lower,
        
    ])

    return points

def _diamond_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower + [side_length/2, side_length/2, 0],

        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        
        bottom_lower + [side_length/2, side_length/2, side_length*2],
        bottom_lower + [0, 0, side_length],
        
    ])

    return points

def _hexagonal_prism_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower + [side_length*1/3, 0, side_length],
        bottom_lower + [side_length*2/3, 0, side_length],
        bottom_lower + [side_length, 0, side_length/2],
        bottom_lower + [side_length*2/3, 0, 0],
        bottom_lower + [side_length*1/3, 0, 0],
        bottom_lower + [0, 0, side_length/2],

        bottom_lower + [side_length*1/3, side_length*2, side_length],
        bottom_lower + [0, side_length*2, side_length/2],
        bottom_lower + [side_length*1/3, side_length*2, 0],
        bottom_lower + [side_length*2/3, side_length*2, 0],
        bottom_lower + [side_length, side_length*2, side_length*1/2],
        bottom_lower + [side_length*2/3, side_length*2, side_length],

        bottom_lower + [side_length*1/3, 0, side_length/2],
        
    ])

    return points

def translate_obj(points, amount):
    return tf.add(points, amount)

def main():
    option = st.selectbox("Select a 3D shape", ("cube", "pyramid", "diamond", "hexagonal prism"))

    if option == "cube":
        _init_shape_ = _cube_(side_length=4)

        points = tf.constant(_init_shape_, dtype=tf.float32)
        translation_amount = tf.constant([0, 0, 0], dtype=tf.float32)
        translated_object = translate_obj(points, translation_amount)

        with tf.compat.v1.Session() as session:
            translated_cube = session.run(translated_object)

        _plt_basic_object_(translated_cube)

    elif option == "pyramid":
        _init_shape_ = _pyramid_(side_length=4)
        
        points = tf.constant(_init_shape_, dtype=tf.float32)
        translation_amount = tf.constant([0, 0, 0], dtype=tf.float32)
        translated_object = translate_obj(points, translation_amount)
        
        with tf.compat.v1.Session() as session:
            translated_cube = session.run(translated_object)

        _plt_basic_object_(translated_cube)

    elif option == "diamond":
        _init_shape_ = _diamond_(side_length=4)
        
        points = tf.constant(_init_shape_, dtype=tf.float32)
        translation_amount = tf.constant([0, 0, 0], dtype=tf.float32)
        translated_object = translate_obj(points, translation_amount)

        with tf.compat.v1.Session() as session:
            translated_cube = session.run(translated_object)

        _plt_basic_object_(translated_cube)

    elif option == "hexagonal prism":
        _init_shape_ = _hexagonal_prism_(side_length=4)
        
        points = tf.constant(_init_shape_, dtype=tf.float32)
        translation_amount = tf.constant([0, 0, 0], dtype=tf.float32)
        translated_object = translate_obj(points, translation_amount)

        with tf.compat.v1.Session() as session:
            translated_cube = session.run(translated_object)

        _plt_basic_object_(translated_cube)

if __name__ == '__main__':
    main()