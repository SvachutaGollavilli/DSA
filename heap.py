#Min Heap
# Time : O(N), Space : O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)




#heap push (insert element)
#Time : O(log n)

heapq.heappush(A, 4)

#heap pop (extract min)
#time : O(log n)

minn = heapq.heappop(A)


#heap sort
# Time : O(n log n), Space : O(n)

def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    heap_sort_list = [0] * n

    for i in range(n):
        heap_sort_list[i] = heapq.heappop(arr)

    return heap_sort_list


#putting dictionaries in heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

heap = []

for k,v in counter.items():
    heapq.heappush(heap, (v,k))

    