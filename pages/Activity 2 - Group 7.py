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
    
    option = st.selectbox("Choose an option", ("Randomize pixel colors", "Customize default pixel color scheme"))

    if option == "Randomize pixel colors":
        img = randomizeplot(two_d_arr)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
    elif option == "Customize default pixel color scheme":
        row = int(st.sidebar.slider("Row", 1, 3, 2))
        column = int(st.sidebar.slider("Column", 1, 3, 2))
        color = int(st.sidebar.slider("Value", 0, 5, 3))
        
        img = plot(two_d_arr, row-1, column-1, color)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
