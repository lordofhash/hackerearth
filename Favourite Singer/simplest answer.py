from collections import Counter
     
N=int(input())
a=input().split(" ")
dic=Counter(a)
ans=list(dic.values())
     
output=ans.count(max(ans))
print(output)