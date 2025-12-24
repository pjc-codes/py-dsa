def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 7, 24, 56, 78, 123]
    print(binary_search(test_arr, 24))
    print(binary_search(test_arr, 77))
    print(binary_search(test_arr, 78))
