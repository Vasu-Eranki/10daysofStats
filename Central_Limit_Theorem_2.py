import os 
import math 

def cdf(x,mean,var):
    root2 = 2**0.5
    temp = math.erf((x-mean)/(var*root2))
    temp = 0.5*(1+temp)
    return temp
    
if __name__=="__main__":
    total_tickets = int(input())
    n_people = int(input())
    mean = float(input())
    var = float(input())
    n_var = var/(n_people**0.5)
    x = total_tickets/n_people
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    result = round(cdf(x,mean,n_var),4)
    fptr.write(str(result)+'\n')
    fptr.close()
