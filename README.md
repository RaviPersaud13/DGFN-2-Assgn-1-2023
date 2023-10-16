# DGFN-2-Assgn-1-2023
# Ravi Persaud
# 
from A_V_calc import calculate_area_of_circle, calculate_volume_of_sphere, calculate_area_of_rectangle, calculate_volume_of_cylinder, calculate_area_of_triangle

def test_calculate_area_of_circle():
    assert calculate_area_of_circle(1) == 3.14
    assert calculate_area_of_circle(2) == 12.56
