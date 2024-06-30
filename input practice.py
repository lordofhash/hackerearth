N = int(input('Give the size of array\n'))
ok=input("Enter elementsof the array(Space-Seperated):")
array1=list(map(int, ok.split( )[:N]))

def arrsum(arr):
    if len(arr) == 0 or len(arr)==1:
        return arr[0]
    return arr[0]+ arrsum(arr[1:])

result = arrsum(array1)
print(result)

