# Given an array of integers arr and an integer k,
# create a boolean function that checks if there
# exist two elements in arr such that we get k
# when we add them together.

# Example 1
# Input arr = [4,5,1,-3,6], k = 11
# Output: true
# Explanation: 5 + 6 == 11
#
# example 2:
# Input: arr = [4,5,1,-3,6], k = 8
# Output: false
# Epxlanation: there is no pair that sums to 8

# *** first solution with sorting ***
# def find_pair(arr, k):
#     arr_sorted = sorted(arr)
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         if arr_sorted[left] + arr_sorted[right] == k:
#             return True
#         elif arr_sorted[left] + arr_sorted[right] < k:
#             left += 1
#         else:
#             right -=1
#     return False


# *** second solution with no sorting***

# uses a hash_table/ dictionary
def find_pair(arr, k):
    visited = {}
    for element in arr:
        if visited.get(k-element):
            return True
        else:
            visited[element] = True
    return False


print(find_pair([-5, 17, 2, 6, 8, 7, 1, 1, 6, 4, 9, 12], 35))
