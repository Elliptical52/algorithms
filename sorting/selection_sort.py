"""
Selection Sort Implementation - 2/11/2026
Continuously swaps smallest element with first unsorted element
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr: list[int]):
    first_sorted_index = 0
    length = len(arr)
    while first_sorted_index < length - 1:
        min_idx = first_sorted_index
        for i in range(first_sorted_index + 1, length):
            if arr[i] < arr[min_idx]: min_idx = i
        
        arr[first_sorted_index], arr[min_idx] = arr[min_idx], arr[first_sorted_index]
        first_sorted_index += 1
        
    return arr
