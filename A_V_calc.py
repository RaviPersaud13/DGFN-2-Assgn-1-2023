# DGFN-2-Assgn-1-2023
# Ravi Persaud
# This code allows the user to input values to calculate
# either the area of a circle, rectangle, or triangle, and
# the volume of a sphere and cylinder.
# Cited from lecture and ChatGPT (asked how to properly implement the formulas in)

# Defines functions for calculating area and volume for different shapes
def calculate_area_of_circle(radius):
    return 3.14 * radius**2

def calculate_volume_of_sphere(radius):
    return (4/3) * 3.14 * radius**3

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_volume_of_cylinder(radius, height):
    return 3.14 * radius**2 * height

def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

# Start of program
if __name__ == "__main__":
    view_option = "default"

    while True:
        # Display menu
        print("A/V Calculator Menu")
        print("Enter Q/q to quit")
        print(f"Enter V/v to change the calculated view or D/d for {view_option} view.")
        print()

        user_input = input("Select an option: ")

        if user_input.lower() == 'q':
            # If 'q' is entered, exit the program
            break

        elif user_input.lower() == 'v':
            # If 'v' is entered, set the view_option to 'calculated'
            view_option = "calculated"
            print("View option set to 'calculated'")
            
            # Display options for Level 1
            print("1. Calculate Area of Circle")
            print("2. Calculate Volume of Sphere")
            print("3. Calculate Area of Rectangle")
            print("4. Calculate Volume of Cylinder")
            print("5. Calculate Area of Triangle")
            print()
            
            shape_choice = input("Select a shape (1-5): ")
            
            if shape_choice == '1':
                # Calculates area of a circle
                try:
                    radius = float(input("Enter the radius: "))
                    result = round(calculate_area_of_circle(radius), 2)
                    print(f"The area of the circle with radius {radius} is (3.14 * {radius}^2) = {result}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif shape_choice == '2':
                # Calculates volume of a sphere
                try:
                    radius = float(input("Enter the radius: "))
                    result = round(calculate_volume_of_sphere(radius), 2)
                    print(f"The volume of the sphere with radius {radius} is ((4/3) * 3.14 * {radius}^3) = {result}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif shape_choice == '3':
                # Calculates area of rectangle
                try:
                    length = float(input("Enter the length: "))
                    width = float(input("Enter the width: "))
                    result = round(calculate_area_of_rectangle(length, width), 2)
                    print(f"The area of the rectangle with length {length} and width {width} is ({length} * {width}) = {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for length and width.")

            elif shape_choice == '4':
                # Calculates volume of a cylinder
                try:
                    radius = float(input("Enter the radius: "))
                    height = float(input("Enter the height: "))
                    result = round(calculate_volume_of_cylinder(radius, height), 2)
                    print(f"The volume of the cylinder with radius {radius} and height {height} is (3.14 * {radius}^2 * {height}) = {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for radius and height.")

            elif shape_choice == '5':
                # Calculates area of a triangle
                try:
                    base = float(input("Enter the base length: "))
                    height = float(input("Enter the height: "))
                    result = round(calculate_area_of_triangle(base, height), 2)
                    print(f"The area of the triangle with base {base} and height {height} is (0.5 * {base} * {height}) = {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for base and height.")

            else:
                print("Invalid choice. Please select a shape (1-6).")

            
        elif user_input.lower() == 'd':
            view_option = "default"
            print(f"View option set to '{view_option}'")
            
            # Display options for Level 1
            print("1. Calculate Area of Circle")
            print("2. Calculate Volume of Sphere")
            print("3. Calculate Area of Rectangle")
            print("4. Calculate Volume of Cylinder")
            print("5. Calculate Area of Triangle")
            print()

            shape_choice = input("Select a shape (1-5): ")

            if shape_choice == '1':
                # Calculates area of a circle
                try:
                    radius = float(input("Enter the radius: "))
                    result = round(calculate_area_of_circle(radius), 2)
                    print(f"The area of the circle is {result}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif shape_choice == '2':
                # Calculates volume of a sphere
                try:
                    radius = float(input("Enter the radius: "))
                    result = round(calculate_volume_of_sphere(radius), 2)
                    print(f"The volume of the sphere is {result}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            elif shape_choice == '3':
                # Calculates area of a rectangle
                try:
                    length = float(input("Enter the length: "))
                    width = float(input("Enter the width: "))
                    result = round(calculate_area_of_rectangle(length, width), 2)
                    print(f"The area of the rectangle is {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for length and width.")

            elif shape_choice == '4':
                # Calculates volume of a cylinder
                try:
                    radius = float(input("Enter the radius: "))
                    height = float(input("Enter the height: "))
                    result = round(calculate_volume_of_cylinder(radius, height), 2)
                    print(f"The volume of the cylinder is {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for radius and height.")

            elif shape_choice == '5':
                # Calculates area of a triangle
                try:
                    base = float(input("Enter the base length: "))
                    height = float(input("Enter the height: "))
                    result = round(calculate_area_of_triangle(base, height), 2)
                    print(f"The area of the triangle is {result}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for base and height.")

            else:
                print("Invalid choice. Please select a shape (1-6).")

            print()
