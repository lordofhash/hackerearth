def sumofarray(arr):
    n = len(arr)
    s = 0
    for i in range(len(arr)):
        s = s + arr[i]
    return s

array1=[1,2,3,4,5,89]
result1=sumofarray(array1)
print(result1)

def sumarray(arr):
    if len(arr) == 0 or len(arr)==1:
        return arr[0]
    return arr[0] + sumarray(arr[1:])

result2=sumarray(array1)
print(result2)
