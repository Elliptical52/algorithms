"""
Gnome Sort Implementation - 2/13/2026
Constantly steps forward. If adjacent values are unsorted, swaps them and steps back.
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def gnome_sort(arr: list[int]):
    length = len(arr)
    
    i = 0
    while i < length:
        if (i == 0) or (arr[i] >= arr[i - 1]):
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr



print(gnome_sort([3,5,7,2,12,6,7,3,1,3,5]))
