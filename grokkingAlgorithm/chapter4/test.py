
arr = [12,2,3,4,5,5,5]

for i in arr[0:]:
    print(i)

# quicksort test

def quicksort(arr):
    if len(arr) < 2 :
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort(arr))
