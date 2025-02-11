def bisect_left(arr, x):
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = (l+r) // 2
        if arr[mid]>=x:
            r = mid - 1
        else:
            l = mid + 1
    return l if 0<=l<len(arr) and arr[l] == x else -1

arr = [1,1,1,2,2,2,2,3,3,3]
print(bisect_left(arr, 3))