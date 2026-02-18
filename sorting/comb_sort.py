"""""
Comb Sort Implementation - 2/17/2026
Bubble sort with slowly decreasing gap 
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from math import floor

def comb_sort(arr: list[int]):
    length = len(arr)
    gap = length
    shrink = 1.3
    is_sorted = False
    
    while not is_sorted:
        gap = floor(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        elif gap == 9 or gap == 10:
            gap = 11
        
        i = 0
        while i + gap < length:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False
            i += 1
    return arr
