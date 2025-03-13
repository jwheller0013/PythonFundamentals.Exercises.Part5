def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    pass  # remove pass statement and implement me


    if len(first_string) != len(second_string):
        return False
    for i in range(int(len(first_string))):
        first_string = first_string.lower()
        second_string = second_string.lower()
        testing = True
        if first_string.find(second_string[i]) == 1:
            testing = True
        elif first_string.find(second_string[i]) == -1:
            testing = False
    return testing