# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import statistics

if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    z=[]
    size=int(input())
    data = list(map(int,input().rstrip().split()))
    frequency = list(map(int,input().rstrip().split()))
    for i in range(0,size):
        z = z+[data[i] for j in range(0,frequency[i])]
    d = int(len(z)/2)
    z=sorted(z)
    low = z[0:d]
    if(d%2!=0):
        high = z[d+1:]
    else:
        high = z[d:]
    low1 = statistics.median(low)
    high1 = statistics.median(high)
    diff = round(float(high1-low1),1)
    fptr.write(str(diff)+'\n')
    fptr.close()
