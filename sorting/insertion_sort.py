"""
Insertion Sort Implementation - 2/11/2026
Inserts numbers into their sorted position in portion of the array
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(arr: list[int]):
    length = len(arr)
    for i in range(1, length): # assume first element is sorted
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print(insertion_sort([3,45,6,8,3,2,1,56,7]))