from typing import Counter


def is_isogram(string):
    """
    Difficulty: Very easy

    Summary: Check if string has only unique chars
    
    Args:
        string (string): input 
   
    Status: Completed
    
    Returns:
        bool : If string has or hasn't only unique chars
    """
    frequency = Counter(string.lower())
    if string is "":
        return True
    elif len(frequency) == len(string):
        return True
    else:
        return False

# Driver program

assert is_isogram("moOse") == False
assert is_isogram("abcdefg") == True
assert is_isogram("abacgudac") == False