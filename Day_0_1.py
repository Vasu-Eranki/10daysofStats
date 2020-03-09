# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
def weighted_mean(n,x,w):
    total =0
    for i in range(0,n):
        total = total+x[i]*w[i]
    total = total/sum(w)
    return total
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n=int(input())
    x = list(map(int,input().rstrip().split()))
    w = list(map(int,input().rstrip().split()))
    op = weighted_mean(n,x,w)
    fptr.write(str(op)+'/n')
    fptr.close()
