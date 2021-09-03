"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors
(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' 
(null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

"""

def divisors(integer):
    """
    Difficulty: Easy

    Show all the divisors of a given number, if the number is prime print {number} is prime

    Args:
        integer (int): Input number
    
    Status : Completed

    Returns:
        string : If number is prime
        list : containing all the divisors of number
    """
    divisors_result = []
    for i in range(2, integer//2 + 1):
        if integer % i == 0:
            divisors_result.append(i)
    if divisors_result:
        return divisors_result
    else:
        return str(integer) + " is prime"




# TEST FUNCTIONALITY
primality_check_result = "13 is prime"
divisors_12 = [2, 3, 4, 6]
divisors_15 = [3, 5]
assert divisors(13) == primality_check_result
assert divisors(15) == divisors_15
assert divisors(12) == divisors_12