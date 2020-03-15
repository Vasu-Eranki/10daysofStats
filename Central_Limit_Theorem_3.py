# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    sample= int(input())
    mean = int(input())
    var = int(input())
    interval = float(input())
    z = float(input())
    n_var = var/(sample**0.5)
    B = (z*n_var)+mean
    A = -(z*n_var)+mean
    fptr.write(str(A)+'\n')
    fptr.write(str(B))
    fptr.close()
