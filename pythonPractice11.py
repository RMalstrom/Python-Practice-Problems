"""
R. Malstrom

Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.

Last modified: 10.3.2024
"""
userNum = int(input("Please enter a number to check. "))
numList = range(1,userNum)
primeCount = 0
for i in numList:
    if userNum % i == 0:
        primeCount = primeCount + 1
if primeCount > 2:
    print(f"{userNum} is not prime")
else:
    print(f"{userNum} is a prime")