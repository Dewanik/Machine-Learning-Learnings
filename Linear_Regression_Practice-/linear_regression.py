from numpy import *
import matplotlib.pyplot as plt


def gradient_descent(given_x,array_points,learning_rate):
    m = 0
    b = 0
    n = size(array_points)
    x = []
    y = []
    for i in range(len(array_points)):
        x.append(array_points[i,0])
        y.append(array_points[i,1])
    x = array(x)
    y = array(y)


    

    for i in range(1000):
        ypredc = m * x + b
        error = 1/n*sum(y-ypredc)
        print(m,b,error)
        mderv =  -(2/n)*sum(x*(y-ypredc))
        bderv = -(2/n)*sum(y-ypredc)
        m = m - learning_rate * mderv
        b = b - learning_rate * bderv
    print(m*given_x+b)

        
    


def run():
    points = genfromtxt('Dataset.csv',delimiter=',')
    learning_rate = 0.0001
    gradient_descent(32.502345269453031,array(points),learning_rate)




if __name__ == '__main__':
     run()
   
