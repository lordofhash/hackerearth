# Print hackerearth

#Problem
#As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please help them.
#
#Input:
#The first line will consists of one integer N denoting the length of string.
#Next line will contain the string
#
#containing only lower case characters.
#
#Output:
#Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).
#
#Constraints:
#
#Each character of string will be in range [a,z]

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