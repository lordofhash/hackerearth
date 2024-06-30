N = int(input())
A=list(map(int, input().split( )[:N]))

def arraysum(arr):
    if len(arr) == 0 or len(arr)==1:
        return arr[0]
    return arr[0]+ arraysum(arr[1:])

result = arayrsum(A)
print(result)
