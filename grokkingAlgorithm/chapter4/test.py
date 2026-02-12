
arr = [12,2,3,4,5,5,5]

for i in arr[0:]:
    print(i)

# quicksort test

def quicksort(arr):
    pivot = arr[0]
    lesser = [for i in arr[1:] if i < pivot]
    greater = [for i in arr[1:] if i > pivot]
    
    return quicksort(lesser) + [pivot] + quicksort(greater)