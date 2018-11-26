import pytest

def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

def test_operate():
    assert operate(5, 2, "+") == 7
    assert operate(4,3, "-") == 1
    assert operate(4, 1, "*") == 4
    assert operate(4, 2, "/") == 2

    with pytest.raises(TypeError) as excinfo:
        operate(5, 2, 7)   
    assert excinfo.value.args[0] == "oper must be a string"

    with pytest.raises(ZeroDivisionError) as excinfo:
        operate(4, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    
    with pytest.raises(ValueError) as excinfo:
        operate(2, 2, '**)
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"