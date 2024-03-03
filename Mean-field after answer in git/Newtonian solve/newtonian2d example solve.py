import numpy as np 
from numpy.linalg import inv

def derive_x(function, value1,value2):
    h = 0.00000000001
    top = function(value1 + h,value2) - function(value1,value2)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)
def derive_y(function, value1,value2):
    h = 0.00000000001
    top = function(value1,value2 + h) - function(value1,value2)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)

def f1(x,y):
    return x**2+x*y-10
def f2(x,y):
    return y+3*x*(y**2)-57 

def main():

    #Initial guess values of y1 and y2 at time = 0. This is constant for each time step
    y1_o = 1.5
    y2_o = 3.5
    #Column vector to store the values for vectorization of the code. This changes during each iteration at that time step
    Y_old = np.ones((2,1))
    Y_old[0] = y1_o
    Y_old[1] = y2_o
    F = np.copy(Y_old)
    Y_new = Y_old 
    J = np.ones((2,2))

    for i in range (0,50):
        F[0] = f1(Y_old[0],Y_old[1])
        F[1] = f2(Y_old[0],Y_old[1])
        #Row 1
        J[0,0] = derive_x(f1,Y_old[0],Y_old[1])
        J[0,1] = derive_y(f1,Y_old[0],Y_old[1])
        #Row 2
        J[1,0] = derive_x(f2,Y_old[0],Y_old[1])
        J[1,1] = derive_y(f2,Y_old[0],Y_old[1])
        Y_new = Y_old - np.matmul(inv(J),F)
        Y_old = Y_new
        print(Y_new)

    pass


if __name__=="__main__":
    main()