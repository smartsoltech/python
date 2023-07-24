def create_unicode_dict(numbers_string:str) -> dict[int, str]:
    """_summary_

    Args:
        numbers_string (str): _description_

    Returns:
        dict[int, str]: _description_
    """
    num1, num2 = map(int, numbers_string.split())
    start, end = min(num1, num2), max(num1, num2)
    return {chr(i): i for i in range(start, end + 1)}

print(create_unicode_dict("65 90"))
