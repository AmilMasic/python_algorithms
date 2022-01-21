# Given an array of int arr that contains n+1 elements between 1 and n inclusive, create a function that return the duplicate element (the elmenet that appears more than once). Assume that:
#     1. There is only one duplicate number:
#     2. The duplicate number can be repeated more than once
#
# Example:
# arr = [4,2,1,3,1]
# Output: 1

def find_duplicate(arr):
    visited = {}
    if arr == []:
        return False
    for element in arr:
        if element in visited:
            return element
        else:
            visited[element] = True
