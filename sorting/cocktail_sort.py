"""
Cocktail Sort Implementation - 2/11/2026
Variation of Bubble Sort that traverses left-right then right-left
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def cocktail_sort(arr: list[int]):
    is_sorted = False
    length = len(arr)
    end = length - 1
    while True:
        is_sorted = True
        i = 0
        for i in range(length - 1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
        if is_sorted: break
        
        end -= 1
        
        for i in range(end - 1, -1, -1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
