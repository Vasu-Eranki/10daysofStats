import os 
if __name__=='__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    prob = list(map(int,input().rstrip().split()))
    n_exp = int(input())
    f_prob = prob[0]/prob[1]
    s_prob = 1-f_prob
    total = 5
    sum1 =0
    for i in range(1,total+1):
        sum1 = sum1+f_prob*((s_prob)**(i-1))
    result = round(sum1,3)
    fptr.write(str(result)+'\n')
    fptr.close()
