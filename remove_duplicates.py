# given an array of integers, create a function that returns an array containing the values of arr without duplicates (the order doesn't matter)
# example:
# arr = [4,2,5,3,3,1,2,4,1,5,5,5,3,1]
# returned arr = [4,2,5,3,1]


# def remove_duplicates(arr):
#     unique_arr = []
#     for element in arr:
#         if element not in unique_arr:
#             unique_arr.append(element)
#     return unique_arr

# print(remove_duplicates([4,2,5,3,3,1,2,4,1,5,5,5,3,1]))

# *** Video solution ***

# Sort the array first
# sort() works, also sorted(arr) works when you want to assign it to a different variable
#  the range portion is what I was missing from my original solution


# def remove_duplicates(arr):
#     if len(arr) == 0:
#         return []
#     arr.sort()
#     no_duplicates_arr = [arr[0]]
#     for i in range(1,len(arr)):
#         if arr[i] != arr[i-1]:
#             no_duplicates_arr.append(arr[i])
#     return no_duplicates_arr


# Hash table solution
#  first create empty hash,iterate over arr
# store elements into hash
# return the keys in a new array

def remove_duplicates(arr):
    visited = {}
    for element in arr:
        visited[element] = True
    return list(visited.keys())


print(remove_duplicates([4,2,5,3,3,1,2,4,1,5,5,5,3,1]))
