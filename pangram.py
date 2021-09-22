"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 

"The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import re
from typing import Counter
def is_pangram(s):
    """
    Difficulty: Easy

    Evaluates if a string is pangram (contains all alphabet characters)

    Args:
        s (string): String needed to evaluate

    Returns:
        bool : If the s is pangram or not
    """
    regex_substitute = '[^A-Za-z]+'
    clean_string = (re.sub(regex_substitute, '', s)).lower()
    print(clean_string)
    frequency_letters = Counter(clean_string)
    if len(frequency_letters) == 26:
        return True
    else:
        return False
# Driver program

assert is_pangram("The quick, brown fox jumps over the lazy dog!")