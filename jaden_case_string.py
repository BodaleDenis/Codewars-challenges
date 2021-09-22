"""


"""

def to_jaden_case(string):
    """
    Difficulty: Very easy

    Summary: Every word should start with a capital letter
    
    Args:
        string (string): input 
   
    Status: Completed
    
    Returns:
        string : Every word in string have capital letter
    """
    words = string.split(" ")
    final_string = ""
    for word in words:
        final_string = final_string + word.capitalize() + " "
    final_string = final_string[:-1]
    return final_string


# Driver program

string_test = "How can mirrors be real if our eyes aren't real"
solution_result = "How Can Mirrors Be Real If Our Eyes Aren't Real"
assert to_jaden_case(string_test) == solution_result