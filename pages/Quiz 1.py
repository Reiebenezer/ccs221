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
    
    # fig, axs = plt.subplots(2, 5)
    # plt.rcParams.update({'font.size': 7})
    image = st.sidebar.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

    if image is not None:
        image_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)

        img = cv2.imdecode(image_bytes, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        img1 = Translation(img, BXold, BYold)
        img2 = Translation(img, BXnew, BYnew)

        # axs[0].imshow(img1)
        # axs[0].axis('off')
        # axs[0].set_title("Original Image")
        
        # axs[1].imshow(img2)
        # axs[1].axis('off')
        # axs[1].set_title("Translated Image")
        
        # st.set_option('deprecation.showPyplotGlobalUse', False)
        # st.pyplot(fig)

        st.image([img1, img2])

if __name__ == '__main__':
    main()