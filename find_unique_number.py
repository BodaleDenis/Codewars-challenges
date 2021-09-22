"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique
"""
from collections import Counter

def find_uniq(arr):
    """
    Difficulty : Easy

    In a list there are multiple elements of the same value and one element which is different from others

    Args:
        arr (array): Input array

    Returns:
        integer: unique element
    """
    frequency = Counter(arr)
    for key, value in frequency.items():
        if value == 1:
            return key   
    
# Driver program

test_list1 = [1, 1, 1, 2, 1, 1]
test_list2 = [0, 0, 0.55, 0, 0]
assert find_uniq(test_list1) == 2
assert find_uniq(test_list2) == 0.55