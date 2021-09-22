"""
A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

"""

def narcissistic(value):
    """
    Difficulty : Easy

    Verify an given number N if every digit to the power of how many digits are is equal to the number.
    Let's say N = abcd , where a,b,c,d are digits
    digits of N = 4 => if a^4 + b^4 + c^4 + d^4 = N => N is narcissistic 

    Args:
        value (integer) : input integer

    Returns:
        bool : if number have narcissistic properties
    """
    digits = len(str(value))
    every_digit = [int(digit)**digits for digit in str(value)]
    narcissistic_test = sum(every_digit)
    if value == narcissistic_test:
        return True
    else:
        return False

# Driver program

assert narcissistic(153) == True
assert narcissistic(7) == True
assert narcissistic(73) == False
