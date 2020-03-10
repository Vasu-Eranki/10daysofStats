import os 
def variance_calc(x,u):
    return (x-u)**2

if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n = int(input())
    x = list(map(int,input().rstrip().split()))
    d = len(x)
    mean = sum(x)/d
    mean = [mean for i in range(d)]
    var = list(map(variance_calc,x,mean))
    var1 = sum(var)/len(var)
    var1 = var1**0.5
    var1 = round(var1,1)
    fptr.write(str(var1)+'\n')
    fptr.close()
    
