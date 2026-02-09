
# return the smallest in the list
def findTheSmallest(arr) :
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if(arr[i]< smallest):
            smallest = arr[i]
            smallest_index = i

    return smallest_index


# selection sort algorithm
def selectionSort(arr):
    new_arr = []
    for i in range(1, len(arr)):
        smallest = findTheSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

#use the algorithm

arr = [2,3,4,5,1]

print(findTheSmallest(arr))

print(selectionSort(arr))
