"""
Hometask for labaratory lesson
22.11.2024
"""
import math

# task N 4
# def is_leap(year):
#     """
#         Defines if year is leap
#     """

#     if year == 0:
#         return "Invalid year"
#     if year < -46:
#         return "There weren't such concept"

#     if (year % 400 == 0
#         or (year % 4 == 0 and year % 100 != 0)):
#         return "Is leap"
#     else: return "Isn't leap"

# print(
#     is_leap(
#         int(input(
#             "Enter a year to define if it is leap: "
#         ))
#     )
# )

# def find_angle(a, b, c):
#     cosin = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
#     print('cosin: ', cosin)
#     if cosin > 1 or cosin < -1:
#         return 180
#     return math.acos(cosin) * 180 / math.pi

# def check_triangle(a, b, c): # the lines of triangle
#     if a <= 0 or b <= 0 or c <= 0:
#         return "Not a triangle"
    
#     if find_angle(a, b, c) + find_angle(a, c, b) + find_angle(b, c, a) != 180:
#         return "Not a triangle"
#     return "It is a triangle"

# print(find_angle(8, 11, 6))

# line_a = float(input("Enter length of first line (a): "))
# line_b = float(input("Enter length of second line (b): "))
# line_c = float(input("Enter length of third line (c): "))
# print(check_triangle(line_a, line_b, line_c))


