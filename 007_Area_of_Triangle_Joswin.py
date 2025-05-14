def area_of_triangle(b, h):
    return round((1/2) * b * h, 1)

b = float(input("Enter base of triangle : "))
h = float(input("Enter height of triangle : "))

print(area_of_triangle(b, h))