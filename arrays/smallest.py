# given an array, find the smallest number in it

def smallest(arr):
    lowest = arr[0]
    for n in arr[1:]:
        if n<lowest:
            lowest=n
    return lowest

arr = [11,66,24,3,66,7,2,44,1,55,2]

print(smallest(arr))