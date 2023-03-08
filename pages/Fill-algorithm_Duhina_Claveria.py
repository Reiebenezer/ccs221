import numpy as np
import matplotlib.pyplot as plt

def plot(two_d_arr:np.array, row, column, color):

    two_d_arr[row, column] = color

    plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    plt.colorbar()
    plt.show()

def randomizeplot(two_d_arr:np.array):
    for i in range(3):
        for j in range(3):
            two_d_arr[i, j] = int(np.random.randint(0, 6))

    plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    two_d_arr = np.array([[1, 0, 1],
                        [0, 1, 0],
                        [1, 0, 1]])
    
    for i in range(3):
        for j in range(3):
            two_d_arr[i, j] = 5 if two_d_arr[i, j] == 1 else 0
    
    while True:
        randomize = input("Type 1 to randomize all pixel colors. \nType anything else to change specific pixel color\n>>> ")
        if randomize == '1':
            randomizeplot(two_d_arr)
        else:
            row = int(input("Enter Row (from 1 to 3)\n>>> "))
            column = int(input("Enter  Column (from 1 to 3)\n>>> "))
            color = float(input("Enter Color Value (from 0 to 5)\nNOTE: must be integer!\n>>> "))
            plot(two_d_arr, row-1, column-1, color)
        
        exit = input("Exit? Y/N: ")
        if(exit == 'Y' or exit == 'y'):
            break