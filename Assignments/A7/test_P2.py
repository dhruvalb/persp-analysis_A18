
def month_length(month, leap_year=False):

    '''
    Return the number of days in the given month.
    '''  

    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July", "August", "October", "December"}:
        return 31

    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None

def test_month_length():
    assert month_length("September", False) == 30
    assert month_length("September", True) == 30
    
    assert month_length("January", False) == 31 
    assert month_length("January", True) == 31

    assert month_length("February", False) == 28
    assert month_length("February", True) == 29

    assert month_length("Dhruval", False) == None    


