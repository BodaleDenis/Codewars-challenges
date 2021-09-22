"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is 
made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""
import sys

def is_all_elements_oneway(elements, status):
    """
    Verify if all array elements are positive or negative

    Args:
        elements (list): An list containing needed to check elements`
        status (string): An string which determines which check to be done "positive" or "negative"

    Returns:
        [bool]: If there are only one type of elements positive/negative
    """
    if status == "positive":
        for element in elements:
            if element < 0:
                return False
        return True
    else:
        for element in elements:
            if element > 0:
                return False
        return True       

def kadanes_alg(arr, size):
    """
    Kadane's algorithm to calculate max sum in a substring

    Args:
        arr (list): A list containing all elements
        size (integer): Size of the list

    Returns:
        [integer]: Maximum sum which can be done in the list's substrings
    """
    max_so_far = arr[0]
    max_ending = 0
    for element in range(0, size):
        max_ending = max_ending + arr[element]
        if max_ending < 0:
            max_ending = 0
        elif max_so_far < max_ending:
            max_so_far = max_ending
    return max_so_far

def max_sequence(arr):
    """
    Difficulty: Easy

    Determines maximum sum in a substrings
    If all elements are < 0 evaluates as 0
    If all elements are > 0 evaluates as sum of ALL elements
    If elements are mixed calculates maximum sum in a substring based on Kandane's algorithm

    Args:
        arr (list): List containing all elements

    Returns:
        integer: Max value of a substring in list
    """
    if is_all_elements_oneway(arr, "positive"):
        return sum(arr)
    elif not arr:
        return 0
    elif is_all_elements_oneway(arr, "negative"):
        return 0
    else:
        return kadanes_alg(arr, len(arr))

# Driver program

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(arr))
assert max_sequence(arr) == 6