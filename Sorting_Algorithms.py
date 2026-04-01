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


# Insertion Sort
# Time : O(n*n), Space : O(n)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, 0, -1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            else:
                break

insertion_sort(A)
print(A)


# Selection Sort
# Time : O(n*n), Space : O(1)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]



# Merge Sort
# Time : O(n log n), Space : O(n) {Space can be made to O(log n), but it is hard to code}

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr) //2
    L = arr[:m]
    R = arr[m:]


    L = merge_sort(L)
    R = merge_sort(R)

    l = r = 0

    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1

        else: 
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr


s_array = merge_sort(A)
print(s_array)



# Quick Sort
# Time : O(n log n) {worst case is O(n*n)}, Space : O(log n) { We will write for O(n)}

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    

    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R


# Counting Sort
# Time : O(n + k) {where k is the range of the data in the array}, Space : O(k)

def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)

    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx+1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

 