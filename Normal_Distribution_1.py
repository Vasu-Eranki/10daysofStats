# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
import os 

def cdf(x,u,var):
    root2 = 2**0.5
    temp = math.erf((x-u)/(var*root2))
    temp = 0.5*(1+temp)    
    return temp

if __name__=='__main__':
    ipt = list(map(float,input().rstrip().split()))
    mean = ipt[0]
    var = ipt[1]
    q1 = float(input())
    q = list(map(float,input().rstrip().split()))
    q2 = q[0]
    q3 = q[1]
    result1 = round(cdf(q1,mean,var),3)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(result1)+'\n')
    result1 = cdf(q2,mean,var)
    result2 = cdf(q3,mean,var)
    result2 = round(result2 - result1,3)
    fptr.write(str(result2)+'\n')    
    fptr.close()
