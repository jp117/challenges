def digits_between_0_and_x(x):
    """
    Returns the total count of digits from 0 to x (inclusive).
    
    Args:
        x (int): The upper bound (inclusive)
    
    Returns:
        int: Total count of digits from 0 to x
    """

    if x <= 1:
        return 0
    
    # if x <= 10:
    #     return x-1
    
    # if x <= 100:
    #     return (x-10) * 2 + 9
    
    # if x <= 1000:
    #     return (x-100) * 3 + 189
    
    # if x <= 10000:
    #     return (x-1000) * 4 + 2889

    # REFACTOR BELOW
    total_digits = 0
    limit = x-1
    start = 1
    length = 1
    while start <= limit:
        end = min(limit, 10**length - 1)
        total_digits += (end - start + 1) * length
        start *= 10
        length += 1
    return total_digits
