import math 
import sys 
import re 
import random 
import os 

def mean(arr):
    d = sum(arr)/len(arr)
    return d
def median(arr):
    y=sorted(arr)
    length = len(arr)
    d = round(length/2)
    if(length%2!=0):
        return y[d-1]
    else:
        return (y[d-1]+y[d])*0.5
def mode(arr): 
    i=0
    arr =sorted(arr)
    y= [arr.count(i) for i in arr]
    y_index = y.index(max(y))
    return arr[y_index] 


    
    return y
if __name__ =='__main__':
    #fptr = open(os.environ['OUTPUT_PATH'],'w')
    arr = int(input())
    arr = list(map(int,input().rstrip().split()))
    x=mean(arr)
    y=median(arr)
    z=mode(arr)
    print(x)
    print(y)
    print(z)
    #fptr.close()
