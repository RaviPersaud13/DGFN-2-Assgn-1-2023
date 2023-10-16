# DGFN-2-Assgn-1-2023
# Ravi Persaud
# This imports specific functions that calculate the area
# and volume of specific shapes. Then uses the base calculations 
# for each shape and test the cases for that specific value.
# Cited from the lectures and assertion lab.
from A_V_calc import calculate_area_of_circle, calculate_volume_of_sphere, calculate_area_of_rectangle, calculate_volume_of_cylinder, calculate_area_of_triangle

def test_calculate_area_of_circle():
    assert calculate_area_of_circle(1) == 3.14
    assert calculate_area_of_circle(2) == 12.56

def test_calculate_volume_of_sphere():
    assert round(calculate_volume_of_sphere(1), 2) == 4.19
    assert round(calculate_volume_of_sphere(2), 2) == 33.49

def test_calculate_area_of_rectangle():
    assert calculate_area_of_rectangle(2, 3) == 6
    assert calculate_area_of_rectangle(4, 5) == 20

def test_calculate_volume_of_cylinder():
    assert round(calculate_volume_of_cylinder(1, 2), 2) == 6.28
    assert round(calculate_volume_of_cylinder(2, 4), 2) == 50.24

def test_calculate_area_of_triangle():
    assert calculate_area_of_triangle(3, 4) == 6.0
    assert calculate_area_of_triangle(5, 6) == 15.0
