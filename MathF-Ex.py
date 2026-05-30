import math

# 1) 2(pi)r = Circumference

"""
radius = float(input("Enter the Radius : "))
Circumference = 2 * math.pi * radius

print(f"The Circumference is {round(Circumference, 2)} cm")

"""
# 2) Area = pi * r^2
"""
Radius = float(input("Enter the Radius : "))
Area = math.pi * Radius**2
print(f"The Radius is {round(Area, 2)} cm")
print(math.pi)

"""
# 3) RootOver(A^2 +B^2) Hypotenuese

A = int(input("Enter a Number : "))
B = int(input("Enter Another Number : "))

C  = math.sqrt(A**2 + B**2)

print(f"Hypotenuese is {C} ")