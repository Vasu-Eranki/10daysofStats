# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
from numpy import linalg
import os


def linear_regression(x: numpy.ndarray, y: numpy.ndarray):
    x_t = x.transpose()
    tem = numpy.matmul(x_t,x)
    tem = linalg.inv(tem)
    tem  = numpy.matmul(tem,x_t)
    tem = numpy.matmul(tem,y)
    return tem



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x = list(map(int,input().rstrip().split()))
    m= x[0]
    n= x[1]
    del x
    x = [[0] * (m + 1)] * n
    y = []
    for j in range(0, n):
            x[j][0] = 1
    x = numpy.asarray(x,dtype = numpy.float32)
    for i in range(0,n):
        temp = list(map(float,input().rstrip().split()))
        for j in range(1,m+1):
            x[i,j] = temp[j-1]
        y.append(temp[-1])
    y=numpy.asarray(y,dtype= numpy.float32)
    y=numpy.expand_dims(y,axis=1)
    gradient = linear_regression(x,y)
    queries = int(input())
    x_new = [[0]*(m+1)]*queries
    for j in range(0,queries):
        x_new[j][0] =1
    x_new=numpy.asarray(x_new,dtype=numpy.float32)
    for i in range(queries):
        temp = list(map(float, input().rstrip().split()))
        x_new[i,1:] = temp
    y_pred = numpy.matmul(x_new,gradient).squeeze()
    y_pred = y_pred.tolist()
    for i in y_pred:
        fptr.write(str(i) + "\n")

