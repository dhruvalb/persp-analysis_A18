def smallest_factor(n):
    '''
    Return the smallest prime factor of the positive integer n.
    '''

    if n == 1: 
        return 1
    
    end =  int(n**0.5 + 1)   #updated the end of range to incld. upto sqrt(n)
    for i in range(2, end):
        if n % i == 0: 
            return i
    
    return n

def test_smallest_factor():
    # Case #1: When value is 1 
    assert smallest_factor(1) == 1
    # Case 
    assert smallest_factor(2) == 2
    # Case #2: Even number 
    assert smallest_factor(6) == 2, "failed for even number"
    # Case #3: Odd number
    assert smallest_factor(13) == 13, "failed for odd number"