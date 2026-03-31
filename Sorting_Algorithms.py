# Bubble Sort 
# Time : O(n*n), Space : O(1)

def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

    return arr


A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

c = bubble_sort(A)

print(c)