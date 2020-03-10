# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import statistics
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    size = int(input())
    arr = list(map(int,input().rstrip().split()))
    arr = sorted(arr)
    middle = statistics.median(arr)
    if(size%2!=0):
        lower = statistics.median(arr[0:int(size/2)])
        higher = statistics.median(arr[int(size/2)+1:])
    else:
        lower = statistics.median(arr[0:int(size/2)])
        higher = statistics.median(arr[int(size/2):])
    fptr.write(str(int(lower))+'\n')
    fptr.write(str(int(middle))+'\n')
    fptr.write(str(int(higher))+'\n')
    fptr.close()
