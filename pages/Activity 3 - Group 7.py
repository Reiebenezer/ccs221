import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from io import StringIO

#translation
def Translation(img, x, y, width, height):
    
    # matrix for translation
    m_translation = np.float32([[1, 0, x], [0, 1, y], [0, 0, 1]])

    # return the modified image
    return cv2.warpPerspective(img, m_translation, (width, height))
    

def Rotation(img, angle, width, height):
    
    # convert deg to rad
    angle_rad = np.radians(angle) 
    
    # add a matrix that defines rotation
    m_rotation = np.float32([
        [np.cos(angle_rad)*0.5, -(np.sin(angle_rad)), 0], #x
        [np.sin(angle_rad), np.cos(angle_rad)*0.5, 0], #y
        [0, 0, 1] #z
    ])

    # return the modified image
    return cv2.warpPerspective(img, m_rotation, (width, height))
    

def Scaling(img, xScale, yScale, width, height):

    # matrix for scaling
    m_scaling = np.float32([
        [xScale, 0, 0],
        [0, yScale, 0],
        [0, 0, 1]
    ]) 

    # return the modified image
    return cv2.warpPerspective(img, m_scaling, (width, height))
    

def Reflection(img, flip_direction, width, height):

    #determine flip_direction and create matrix for each possibility
    if flip_direction == 'vertical':
        m_reflection = np.float32([
            [1, 0, 0],
            [0, -1, height],
            [0, 0, 1]
        ])
    elif flip_direction == 'horizontal':
        m_reflection = np.float32([
            [-1, 0, width],
            [0, 1, 0],
            [0, 0, 1]
        ])

    # return the modified image
    return cv2.warpPerspective(img, m_reflection, (width, height))
    

def Shear(img, direction, amount, width, height):

    #determine shear direction and create matrix for each possibility
    if direction == 'horizontal':
        m_shearing = np.float32([
            [1, amount, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    elif direction == 'vertical':
        m_shearing = np.float32([
            [1, 0, 0],
            [amount, 1, 0],
            [0, 0, 1]
        ])

    # return the modified image
    return cv2.warpPerspective(img, m_shearing, (int(width*1.5), int(height*1.5)))
    

def main():
    

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
    
    image = stringio
    
    x = int(input("Enter translation_x: "))
    y = int(input("Enter translation_y: "))
    rot = int(input("Enter rotation in degrees: "))
    xScale = float(input("Enter x-axis scale (0 to 1): "))
    yScale = float(input("Enter y-axis scale (0 to 1): "))
    skew = float(input("Enter skew amount (-1 to 1): "))
    skew_dir = str(input("Enter skew direction: "))

    img_ = cv2.imread(image)
    img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

    width = img_.shape[0]
    height = img_.shape[1]

    functions = [Translation(img_, x, y, width, height), Rotation(img_, rot, width, height), Scaling(img_, xScale, yScale, width, height), Reflection(img_, 'vertical', width, height), Shear(img_, skew_dir, skew, width, height)]

    for f in functions:
        img_ = cv2.imread(f"{image}")
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        img_ = f
        plt.axis('off')
        plt.imshow(img_)
        plt.show()

if __name__ == '__main__':
    main()
