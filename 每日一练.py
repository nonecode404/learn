def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6, 9, 20, 28]
insertSort(arr)
for it in arr:
    print(it)

def binarySearch(arr, l, r, k):
    mid = (l + r) // 2
    if arr[mid] > k :
        binarySearch(arr, l, mid - 1,k)
    elif arr[mid] < k :
        binarySearch(arr, mid+1, r, k)
    else:
        return mid

print(binarySearch(arr, 0, len(arr) -1 , 11))