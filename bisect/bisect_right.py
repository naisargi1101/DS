def bisect_right(arr, x):
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = (l+r) // 2
        if arr[mid]<=x:
            l = mid + 1
        else:
            r = mid - 1            
    return r if 0<=r<len(arr) and arr[r] == x else -1

arr = [1,1,1,2,2,2,2,3,3,3]
print(bisect_right(arr, 3))