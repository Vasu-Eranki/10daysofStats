# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math 
import statistics
class stats():
    def __init__(self,n,x,y):
        self.n=n
        self.x=x
        self.y=y
        self.x_stddev = 0
        self.y_stddev = 0
        self.x_mean = 0
        self.y_mean = 0
        self.pearson = 0
    def mean(self):
        self.x_mean = statistics.mean(self.x)
        self.y_mean = statistics.mean(self.y)
    def std_dev(self):
        self.x_stddev = sum([(i-self.x_mean)**2 for i in x])
        self.x_stddev = self.x_stddev/len(x)
        self.x_stddev = self.x_stddev**0.5
        self.y_stddev = sum([(i-self.y_mean)**2 for i in y])
        self.y_stddev = self.y_stddev/len(y)
        self.y_stddev = self.y_stddev**0.5
        #self.x_stddev = round(self.x_stddev,5)
        #self.y_stddev
    def results(self):
        numerator = [(self.x[i]-self.x_mean)*(self.y[i]-self.y_mean) for i in range(0,n)]
        numerator = sum(numerator)
        self.pearson = numerator/(self.n*self.x_stddev*self.y_stddev)
        return self.pearson

if __name__=="__main__":
    n= int(input())
    x = list(map(float,input().rstrip().split()))
    y = list(map(int,input().rstrip().split()))
    S = stats(n,x,y)
    S.mean()
    S.std_dev()
    pearson = S.results()
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(pearson)+'\n')
    fptr.close()
