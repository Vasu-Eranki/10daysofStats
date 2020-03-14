# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math 

def cdf(x,mean,var):
    root2 = 2**0.5
    temp = math.erf((x-mean)/(var*root2))
    temp = 0.5*(1+temp)
    return temp
if __name__=="__main__":
    x = list(map(int,input().rstrip().split()))
    mean = x[0]
    var = x[1]
    limits = int(input())
    limits2 = int(input())
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    result = (1-cdf(limits,mean,var))*100
    result = round(result,2)
    fptr.write(str(result)+'\n')
    result = cdf(limits2,mean,var)
    fptr.write(str(round(100-100*result,2))+'\n')
    fptr.write(str(round(100*result,2))+'\n')
