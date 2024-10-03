"""
R. Malstrom

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.

Last modified: 10.3.2024
"""

a = [5, 10, 15, 20, 25]

b = [a[0],a[a.__len__() - 1]]

print(b)
