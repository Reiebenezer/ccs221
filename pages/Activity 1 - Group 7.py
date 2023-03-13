import matplotlib.pyplot as plt
import streamlit as st

def DDALine(x1, y1, x2, y2, color, axis):
    """
    Variations:
        relies on a value called steps that chooses the number of values to display plus 1
        steps is the absolute value of maximum distance 
        relies on floating-point calculation through the calculation of Xinc and Yinc (x-increment and y-increment, respectively)
        calculates primarily through division and addition
    """
    dx = x2-x1
    dy = y2-y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx/steps)
    Yinc = float(dy/steps)

    for i in range(0, int(steps + 1)):
        axis.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    axis.set_title("DDA Line Algorithm", fontsize=10)

def BresenhamLine(x1, y1, x2, y2, color, axis):
    """
    Variations:
        dx and dy are absolute values
        relies on the value of variable p that decides whether to change the y-value by 1 or maintain the same value
        does not rely on floating-point calculation; 
        calculates primarily through multiplication, addition and subtraction
        exchanges the x- and y-values if slope is greater than 1
    """
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    slope = dy / float(dx)
    
    if slope > 1:
        #interchange values of x and y
        dx, dy, = dy, dx
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx

    for i in range(0, int(dx + 1)):
        axis.plot(int(x1), int(y1), color)
        if p > 0:
            y1 = y1 + 1 if y1 < y2 else y1 - 1
            p += 2 * (dy - dx)
        else:
            p += 2 * dy
        
        x1 = x1 + 1 if x1 < x2 else x1 - 1
    axis.set_title("Bresenham's Line Algorithm", fontsize=10)


def MidpointLine(x1, y1, x2, y2, color, axis):
    """
    Variations:
        interchange the numbers if x2 > x1 and y2 > y1
        relies on the value of variable d that decides whether to change the y-value by 1 or maintain the same value
        d is calculated through getting the midpoint of the x-distance subtracted from the y-distance
    """
    
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    dx = x2 - x1
    dy = y2 - y1

    # decision parameter
    d = dy - (dx/2)
    
    steps = dx if dx > dy else dy
    
    for i in range(0, int(steps + 1)):
        axis.plot(int(x1), int(y1), color)
        x1 += 1

        if d < 0:
            d += dy
        else:
            d += dy - dx
            y1 += 1
    axis.set_title("Midpoint Line Algorithm", fontsize=10)

def MidpointLine2(x1, y1, x2, y2, color, axis):
    """
    Variations:
        Copied the DDA and Bresenham algorithms, then added a midpoint to each 
    """
    #Assign the x- and y-coordinates to constants to avoid data manipulation
    X1 = x1
    Y1 = y1
    X2 = x2
    Y2 = y2

    #DDA Portion
    DDALine(x1, y1, x2, y2, color, axis[0])
		
    #add midpoint
    axis[0].plot((X1 + X2)/2, (Y1 + Y2)/2, "r.")
    axis[0].set_title("DDA Line Algorithm With Midpoint", fontsize=10)

    #Bresenham Portion
    BresenhamLine(x1, y1, x2, y2, color, axis[1])
		
    #add midpoint
    axis[1].plot((X1 + X2)/2, (Y1 + Y2)/2, "r.")     
    axis[1].set_title("Bresenham's Line Algorithm With Midpoint", fontsize=10)


def main():
    x = int(st.number_input("Enter X1: "))
    y = int(st.number_input("Enter Y1: "))
    xEnd = int(st.number_input("Enter X2: "))
    yEnd = int(st.number_input("Enter Y2: "))
    color = "b."

    if xEnd != 0 and yEnd != 0 and x != xEnd and y != yEnd:
        figure, axis = plt.subplots(1, 2)

        MidpointLine2(x, y, xEnd, yEnd, color, axis)
        st.pyplot(figure)
        


if __name__ == '__main__':
    main()
