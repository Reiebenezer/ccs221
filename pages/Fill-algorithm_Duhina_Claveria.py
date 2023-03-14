import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import cv2
from PIL import Image

def plot(two_d_arr:np.array, row, column, color):

    two_d_arr[row, column] = color

    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0, 5])
    plt.colorbar()
    return img

def randomizeplot(two_d_arr:np.array):
    for i in range(3):
        for j in range(3):
            two_d_arr[i, j] = int(np.random.randint(0, 6))

    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0, 5])
    plt.colorbar()
    return img

if __name__ == '__main__':
    two_d_arr = np.array([[1, 0, 1],
                        [0, 1, 0],
                        [1, 0, 1]])
    
    for i in range(3):
        for j in range(3):
            two_d_arr[i, j] = 5 if two_d_arr[i, j] == 1 else 0
    
    if st.button("Click to randomize all pixel colors"):
        img = randomizeplot(two_d_arr)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
    else:
        row = int(st.number_input("Enter Row (from 1 to 3)\n>>> "))
        column = int(st.number_input("Enter  Column (from 1 to 3)\n>>> "))
        color = float(st.number_input("Enter Color Value (from 0 to 5)\nNOTE: must be integer!\n>>> "))

        if st.button("Commit Changes"):
            img = plot(two_d_arr, row-1, column-1, color)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        