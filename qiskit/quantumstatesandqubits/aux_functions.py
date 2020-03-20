def numbertobin(number):
    """Transform numbers to binary notation.
    
    Using recursively divmod operation to calc coeficients of
    the division to create the binary number.

    Parameters
    ----------
    number : int
        Number to transform into binary.

    Returns
    -------
    str
        Transformed number into binary.

    """

    b_n = []
    while number:
        number, r = divmod(number, 2)
        b_n.insert(0, str(r))

    return ''.join(b_n)


def bintonumber(bin_number):
    """Transform from binary to integer number.
    
    Iterating over a string binary number calc the integer number
    via decomposition into sum of powers of two.

    Parameters
    ----------
    bin_number : str
        Number to transform into integer.

    Returns
    -------
    int
        Transformed number into integer.

    """
    
    return sum([int(bit) * 2 ** idx for idx, bit in enumerate(bin_number[::-1])])