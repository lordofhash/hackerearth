from collections import Counter
N=int(input())
A=input().split()[:N] #using .split() makes the input array, instead of slicing a string
hash1=Counter(A)
sorted_hash1_by_value = sorted(hash1.items(), key=lambda x:x[1], reverse=True)
# print(sorted_hash1_by_value)
y = sorted_hash1_by_value[0] #took help, used chatgpt here. I had confusion. So...yeah
L = [k for k, v in hash1.items() if v == y[1]]
print(len(L))