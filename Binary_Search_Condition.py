# Condition based binary search

B = [False, False, False, False, False, True, True]

def binary_search_condition(arr):
    l = 0
    r = len(arr) - 1


    while l < r:
        m = l + ((r-l)//2)

        if arr[m]:
            r = m

        else:
            l = m + 1

    return l

print(binary_search_condition(B))