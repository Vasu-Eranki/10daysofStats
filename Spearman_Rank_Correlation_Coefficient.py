# Enter your code here. Read input from STDIN. Print output to STDOUT
import os 
class stats():
    def __init__(self,n,x,y):
        self.n=n
        self.x=x
        self.y=y
        self.spearman = 0
        self.x_rank=[]
        self.y_rank = []
    def rank_generator(self):
        temp1 = sorted(self.x)
        temp2 = sorted(self.y)
        self.x_rank = [(temp1.index(i)+1) for i in self.x]
        self.y_rank = [(temp2.index(i)+1) for i in self.y]
    def spearman_calc(self):
        temp = [(self.x_rank[i]-self.y_rank[i])**2 for i in range(self.n)]
        temp = 6*sum(temp)
        print(temp)
        self.spearman = temp/(self.n**3-self.n)
        return 1-self.spearman

if __name__=="__main__":
    n= int(input())
    x = list(map(float,input().rstrip().split()))
    y = list(map(int,input().rstrip().split()))
    S = stats(n,x,y)
    S.rank_generator()
    spearman = round(S.spearman_calc(),3)
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    fptr.write(str(spearman)+'\n')
    fptr.close()
