

# binary search 
def binarySearch(arr , guess):
    n = len(arr) - 1
    start = arr[0]
    end = arr[n]

    while start <= end:
        mid = (start+end)//2
        guess = arr[mid]

        if arr[mid]== guess:
            return mid 
        elif arr[mid] < guess:
            start = mid + 1
        else:
            end = mid - 1


# implementation
list = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(list , 7))

# selection sort
def smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest :
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        val = smallest(arr)
        new_arr.append(arr.pop(val))
    return new_arr

#implementation
arr = [5,6,4,56,3]
print(smallest(list))
print(selectionSort(arr))

# recursion
def countdown(i):
    if i == 0:
        return
    print(i)
    return countdown(i-1)

# implementation
countdown(10)

def factorial(i):
    if i < 2:
        return i
    return i * factorial(i-1)

# implementation
print(factorial(5))


