# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    prob = list(map(int,input().rstrip().split()))
    n_exp = int(input())
    f_prob = prob[0]/prob[1]
    s_prob = 1-f_prob
    result = (s_prob)**(n_exp-1)
    result = result*f_prob 
    result = round(result,3)
    fptr.write(str(result)+'\n')
    fptr.close()
    
