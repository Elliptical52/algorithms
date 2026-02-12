"""
Bubble Sort Implementation - 2/11/2026
Steps through list and swaps adjacent values in wrong order until list is sorted
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(arr: list[int]):
    is_sorted = False
    length = len(arr)
    while not is_sorted:
        is_sorted = True
        i = 0
        for i in range(length - 1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1

    return arr