from geometry import triangle_area, square_area, circle_area

def test_triangle():
    # Verification: If base=10 and height=5, area must be 25.0
    assert triangle_area(10, 5) == 25.0

def test_square():
    # Verification: If side=4, area must be 16
    assert square_area(4) == 16

def test_circle():
    # Verification for the new function from Role B
    # Using a small delta for float comparison is good practice
    assert circle_area(1) == 3.141592653589793