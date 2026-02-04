import math

# sorted
list = [1,2,3,4,5,6,7,8,9,10]

def binarySearch(list, item):
    leng = len(list) - 1
    hi = list[leng] 
    low = list[0]
    
    while low <= hi:
        mid = math.floor((hi+low)/2)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            hi = mid - 1
        else:
            low = mid + 1

    return None

print(binarySearch(list, 7))
