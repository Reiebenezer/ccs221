import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st


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
    if direction == 'Horizontal':
        m_shearing = np.float32([
            [1, amount, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
    elif direction == 'Vertical':
        m_shearing = np.float32([
            [1, 0, 0],
            [amount, 1, 0],
            [0, 0, 1]
        ])
    else:
        raise Exception("Invalid skew direction")
        return 0
    # return the modified image
    return cv2.warpPerspective(img, m_shearing, (int(width*1.5), int(height*1.5)))
    

def main():
    
    
    uploaded_file = st.sidebar.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        
        x = int(st.sidebar.slider("Translation_x", 0, 2000, 0))
        y = int(st.sidebar.slider("Translation_y", 0, 2000, 0))
        rot = int(st.sidebar.slider("Rotation", 0, 90, 45))
        xScale = float(st.sidebar.slider("X-axis scale", 0.0, 1.0, 1.0))
        yScale = float(st.sidebar.slider("Y-axis scale", 0.0, 1.0, 1.0))
        skew = float(st.sidebar.slider("Skew Amount", -1.0, 1.0, 0.0))
        skew_dir = st.sidebar.radio("Skew Direction", ("Vertical", "Horizontal"))
        

        img_ = cv2.imdecode(file_bytes, 1)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        width = img_.shape[0]
        height = img_.shape[1]

        functions = [Translation(img_, x, y, width, height), Rotation(img_, rot, width, height), Scaling(img_, xScale, yScale, width, height), Reflection(img_, 'vertical', width, height), Shear(img_, skew_dir, skew, width, height)]

        for f in functions:
            img_ = cv2.imdecode(file_bytes, 1)
            # img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

            img_ = f
            # plt.axis('off')
            # plt.imshow(img_)
            # plt.show()
            st.image(img_, cv2.COLOR_BGR2RGB)

if __name__ == '__main__':
    main()
