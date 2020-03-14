# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math
if __name__=="__main__":
    mean = float(input())
    x = float(input())
    fact = math.factorial(x)
    e = math.e
    p = (mean**x)*(e**(-mean))
    p = p/fact
    p = round(p,3)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(p)+'\n')
    fptr.close()
