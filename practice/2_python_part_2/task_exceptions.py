"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
import typing

class DivisionByOneException(Exception):
    def __init__(self, message="Deletion on 1 gets the same result"):
        super().__init__(message)

def division(x: int, y: int) -> typing.Union[None, int]:
    try:
        if y==0:
            print("Division by 0")
            return None
        elif y==1:
            raise DivisionByOneException()
        else:
            return print(x//y)
            #return result
    except DivisionByOneException as e:
        print(e)
    finally:
        print("Division Finished")

division(1,0)
division(1,1)
division(2,2)