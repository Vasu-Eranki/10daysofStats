# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math 
import statistics 

def binomial(b_prob,g_prob): 
    sum1 =0
    total = 6
    for i in range(int(total/2),total+1):
        temp = math.factorial(total)
        temp1 = math.factorial(i)*math.factorial(total-i)
        temp = temp/temp1
        temp1 = b_prob**i
        temp1 = temp1*(g_prob**(total-i))
        sum1 =sum1+temp*temp1
    return round(sum1,3)

    

if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    prob = list(map(float,input().rstrip().split()))
    b_prob = prob[0]/sum(prob)
    g_prob = prob[1]/sum(prob)
    assert b_prob+g_prob==1
    result = binomial(b_prob,g_prob)
    fptr.write(str(result)+'\n')
    fptr.close()
