def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # pass  # remove pass statement and implement me
    value = value.lower()
    value = value.replace(" ", "")
    reverse = value[::-1]
    return value == reverse
