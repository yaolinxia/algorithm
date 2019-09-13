def solution(k,a,b):
    res=[]
    def dfs(current,a,b,k):
        if len(current)>=a and len(current)<=b:
            count = 0
            for c in current:
                if c=="白":
                    count+=1
            if count%k==0:
                res.append(current)
        if len(current)>b:
            return
        for c in ["红","白"]:
            if c=="红":
                count=0
                for i in range(1,len(current)+1):
                    if current[-i]=="白":
                        count+=1
                    else:
                        break
                if count%k==0 or current[-1]=="红":
                    dfs(current+[c],a,b,k)
            else:
                count = 0
                for i in range(1, len(current) + 1):
                    if current[-i] == "白":
                        count += 1
                    else:
                        break
                if b-len(current)+count<k:
                    continue
                dfs(current+[c],a,b,k)
    dfs(["红"],a,b,k)
    dfs(["白"],a,b,k)
    return int(len(res)%(1e9+7))
import sys
line=sys.stdin.readline().strip()
N,k=list(map(int,line.split()))
res=[]
for _ in range(N):
    line = sys.stdin.readline().strip()
    a,b=list(map(int,line.split()))
    res.append(solution(k,a,b))
for r in res:
    print(r)