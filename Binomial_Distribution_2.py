# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
import math 


def binomial(failure, success, batch,total):
    sum1 = 0
    for i in range(0, total):
        temp = math.factorial(batch)
        temp1 = math.factorial(i) * math.factorial(batch - i)
        temp = temp/temp1
        temp1 = (failure) ** (i)
        temp1 = temp1 * ((success) ** (batch - i))
        sum1 = sum1 + temp*temp1
    sum1 = round(sum1, 3)
    return sum1


if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    prob = list(map(int,input().rstrip().split()))
    failure = prob[0]/100
    batch = prob[1]
    success = 1-failure 
    result = binomial(failure,success,batch,total=3)
    result1 = binomial(failure,success,batch,total=2)
    result1 = round(1-result1,3)
    fptr.write(str(result)+'\n')
    fptr.write(str(result1)+'\n')
    fptr.close()
