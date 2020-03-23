import numpy as np


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


def sphericaltocartesian(radius, theta, psi):
    """Change of coordinate base.
    
    Change from an spherical base to cartesian coordinates.

    Parameters
    ----------
    radius : float
        Lenght of the vector.
    
    theta : float
        Angle from z-axis to vector.
    
    psi : float
        Angle from x-axis to the proyection of the vector in plane x-y.

    Returns
    -------
    tuple(float, float, float)
        Transformed coordinates into cartesians (x, y, z).

    """
    
    x = radius * np.sin(psi) * np.cos(theta)
    y = radius * np.sin(psi) * np.sin(theta)
    z = radius * np.cos(psi)
    return x, y, x