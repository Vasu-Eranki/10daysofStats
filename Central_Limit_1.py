# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math 

def cdf(x,mean,var):
    root2 = 2**0.5
    temp = math.erf((x-mean)/(var*root2))
    temp = 0.5*(1+temp)
    return temp
    
if __name__=="__main__":
    total_weight = int(input())
    n_boxes = int(input())
    mean = int(input())
    var = int(input())
    n_var = var/(n_boxes**0.5)
    x = int(total_weight/n_boxes)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    result = cdf(x,mean,n_var)
    fptr.write(str(result)+'\n')
    fptr.close()
