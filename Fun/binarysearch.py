import random

def binarySearch(arr,l,r,x):
    if l <= r:
        middle = l+(r-1)//2

        if arr[middle] == x:
            return middle
        elif arr[middle] > x:
            return binarySearch(arr, l, middle-1, x)
        else:
            return binarySearch(arr, middle+1, r, x)
    else: return -1

# creates array length 10, range between 0 and 100
arr = []
for i in range(10):
    gen = random.randint(0,100)
    arr.append(gen)
arr.sort()

# choses random number in same range
x = random.randint(0,100) 

# algorithm
result = binarySearch(arr, 0, len(arr)-1, x)

# checks result and prints it
if result != -1:
    print("X is in the list at index % d" % result)
else:
    print("X isn't in the list")