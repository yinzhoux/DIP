import math

def number_decompose_closest(n: int):
    '''
    Calculate a, b 
        s.t.
            a * b = n
            a - b >= 0
            a - b is as small as possible.
    
    Parameters:
        @n: The number to decompose.
    '''
    assert n > 0, f'n must be bigger than zero.'

    root = math.isqrt(n)

    for b in range(root, 0, -1):
        if ((int)(n / b)) * b == n:
            return ((int)(n/b), b)
        
    assert False, 'Error occurred.'

    