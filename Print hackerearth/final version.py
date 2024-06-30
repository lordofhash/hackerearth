N=int(input())
   
r=input()[:N]
     
a=r.count('h')//2
     
b=r.count('a')//2
     
c=r.count('c')
     
d=r.count('k')
     
e=r.count('e')//2
     
f=r.count('r')//2
     
j=r.count('t')
     
     
     
     
t=[a,b,c,d,e,f,j]
     
t.sort()
     
print(t[0])