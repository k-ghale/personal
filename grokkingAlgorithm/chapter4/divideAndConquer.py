
# recursive function to sum all

arr = [1,2,3,4,5,6]

def sum_recursion(arr, i=0):
    if i == len(arr):
        return 0
    else:
        return arr[i] + sum_recursion(arr[1:])

print(sum_recursion(arr))
