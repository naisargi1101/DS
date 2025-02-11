# TC: O(2^N) SC: O(2^N)
def subsetRecur(i, arr, res, subset):
    
    # add subset at end of array
    if i == len(arr):
        res.append(list(subset))
        return
    
    # include the current value and 
    # recursively find all subsets
    subset.append(arr[i])
    subsetRecur(i + 1, arr, res, subset)
    
    # exclude the current value and 
    # recursively find all subsets
    subset.pop()
    subsetRecur(i + 1, arr, res, subset)

if __name__ == "__main__":
    arr = [1, 2, 3]
    subset = []
    res = []

    subsetRecur(0, arr, res, subset)
    
    for subset in res:
        for num in subset:
            print(num, end=" ")
        print()