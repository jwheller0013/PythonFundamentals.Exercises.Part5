
def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    # pass  # remove pass statement and implement me

    return len(str_in)


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    # pass  # remove pass statement and implement me

    return str_in[0]


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    # pass  # remove pass statement and implement me

    last_char = len(str_in) - 1
    return str_in[last_char]

def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    # pass  # remove pass statement and implement me
    # only passes 1 of 3
    str_in = str_in.lower()
    sub_str_in = sub_str_in.lower()
    return str_in.find(sub_str_in) != -1

def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    # pass  # remove pass statement and implement me

    return str_in[start:stop]


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """
    pass  # remove pass statement and implement me

    return str_in.swapcase()