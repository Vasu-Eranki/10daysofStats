# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
import statistics
import os
class stats():
    def __init__(self,n,x,y):
        self.n=n
        self.x=x
        self.y=y
        self.x_stddev = 0
        self.y_stddev = 0
        self.x_mean = 0
        self.y_mean = 0
        self.gradient = 0
        self.c=0
    def mean(self):
        self.x_mean = statistics.mean(self.x)
        self.y_mean = statistics.mean(self.y)
    def std_dev(self):
        self.x_stddev = sum([(i-self.x_mean)**2 for i in self.x])
        self.x_stddev = self.x_stddev/len(x)
        self.x_stddev = self.x_stddev**0.5
        self.y_stddev = sum([(i-self.y_mean)**2 for i in self.y])
        self.y_stddev = self.y_stddev/len(self.y)
        self.y_stddev = self.y_stddev**0.5
    def results(self):
        numerator = [(self.x[i]-self.x_mean)*(self.y[i]-self.y_mean) for i in range (self.n)]
        numerator = sum(numerator)
        pearson = numerator/(self.n*self.x_stddev*self.y_stddev)
        self.gradient = pearson * self.y_stddev/self.x_stddev
        return self.gradient
    def intercept(self):
        self.c = self.y_mean-self.gradient*self.x_mean
        return self.c
if __name__=="__main__":
    n = 5
    x=[]
    y=[]
    for _ in range(n):
        z = list(map(int,input().rstrip().split()))
        x.append(z[0])
        y.append(z[1])
    S=stats(n,x,y)
    S.mean()
    S.std_dev()
    m = S.results()
    c = S.intercept()
    result = 80*m+c
    result = round(result,3)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(result))
    fptr.close()
