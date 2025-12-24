def find_min_rotated(arr):
    left, right = 0, len(arr)-1
    boundary_idx = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= arr[-1]:
            boundary_idx = mid
            right = mid-1
        else:
            left = mid + 1
    return boundary_idx

arr1=[30, 40, 50, 10, 20]
arr2=[3, 5, 7, 11, 13, 17, 19, 20]

print(find_min_rotated(arr1))
print(find_min_rotated(arr2))
