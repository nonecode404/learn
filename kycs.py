def binarySearch(arr, left, right, k) :
    if left > right :
        return
    mid = ( left + right) //2
    if arr[mid] > k :
        binarySearch(arr, left, mid - 1, k)
    elif arr[mid] > k :
        binarySearch(arr, mid + 1, right, k)
    else:
        return mid
arr = [2, 2, 3, 4, 10, 40,80]
k = 10

# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, k)

if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")

def insertionSort(arr):
    for i in range(1, len(arr)) :
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            print('j:{0}'.format(j))

        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i])





def bubbleSort(arr) :
    n = len(arr)
    for i in range(n) :
        for j in range(0, n-i-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])

