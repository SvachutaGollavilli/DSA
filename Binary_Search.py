A = [-3, -1, 0, 1, 4, 7]


# Time : O(log n)
# Space : O(n)


def Binary_Search(array, integer):
    if not array:
        return False
    
    left = 0
    right = len(array) - 1

    while left <= right:

        mid = left + ((right - left)//2)

        if integer == array[mid]:
            return True

        elif integer > array[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return False


print(Binary_Search(A, 7))


