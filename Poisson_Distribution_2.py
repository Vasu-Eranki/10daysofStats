# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
if __name__=="__main__":
    mean = list(map(float,input().rstrip().split()))
    x = mean[0]
    y=mean[1]
    Ca = round(160+40*(x+x**2),3)
    Cb = round(128+40*(y+y**2),3)
    fptr = open(os.environ["OUTPUT_PATH"],'w')
    fptr.write(str(Ca)+'\n')
    fptr.write(str(Cb)+'\n')
    fptr.close()
