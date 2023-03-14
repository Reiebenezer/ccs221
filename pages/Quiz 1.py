import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st

#translation
def Translation(img, x, y):
    width = img.shape[1]
    height = img.shape[0]
    
    # matrix for 
    m_translation = np.float32([[1, 0, x], [0, 1, y], [0, 0, 1]])

    # return the modified image
    return cv2.warpPerspective(img, m_translation, (width, height))

def main():
    BXold = 0
    BYold = 0
    Tx = int(input("Enter translation-x: "))
    Ty = int(input("Enter translation-y: "))
    BXnew = BXold + Tx
    BYnew = BYold + Ty
    
    fig, axs = plt.subplots(2, 5)
    plt.rcParams.update({'font.size': 7})
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.png"]

    for index, img in enumerate(images): 
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        img1 = Translation(img, BXold, BYold)
        img2 = Translation(img, BXnew, BYnew)

        axs[0, index].imshow(img1)
        axs[0, index].axis('off')
        axs[0, index].set_title("Original Image")
        
        axs[1, index].imshow(img2)
        axs[1, index].axis('off')
        axs[1, index].set_title("Translated Image")
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)

if __name__ == '__main__':
    main()