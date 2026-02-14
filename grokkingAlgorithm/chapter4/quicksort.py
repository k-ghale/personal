# swap in a different way

a = 5
b = 7

a ^= b
b ^= a
a ^= b

print(a,b)

# sum
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


# quick sort algorithm

# short and simple one 
def quickSort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        less = [i for i in arr[1:]  if i <= pivot]
        
        great = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(great)

# in depth
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        lesser = []
        greater = []

        for i in arr[1:]:
            if i <= pivot:
                lesser.append(i)

        for i in arr[1:]:
            if i > pivot:
                greater.append(i)
        
        return quicksort(lesser) + [pivot] + quicksort(greater)

# implementation

arr = [1,2,3,4,5]
sort_this = [5,12,4,6,8,3]

print(sum(arr))
print(quickSort(sort_this))
print(quicksort(sort_this))
