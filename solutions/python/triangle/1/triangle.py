def is_valid_triangle(sides):
    a, b, c = sides
    
    # All sides must be > 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Triangle inequality rule
    if a + b < c or a + c < b or b + c < a:
        return False
    
    return True


def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    
    a, b, c = sides
    return a != b and b != c and a != c