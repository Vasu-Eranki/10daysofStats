# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
def weighted_mean(x,w):
    return x*w

    return total
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n=int(input())
    x = list(map(int,input().rstrip().split()))
    w = list(map(int,input().rstrip().split()))
    op = list(map(weighted_mean,x,w))
    op = sum(op)/sum(w)
    op=round(op,1)
    fptr.write(str(op)+'\n')
    fptr.close()
