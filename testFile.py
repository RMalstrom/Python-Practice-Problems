"""
R. Malstrom
CMSC-1380

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

Date Last Modified: 9.24.2024
"""
import time

userNum = int(input("Please enter a number: "))

start = time.time()

numList = range(1,userNum)
doctoredList = []

for x in numList:
    if userNum % x == 0:
        doctoredList.append(x)

print(doctoredList)

end = time.time()
print(end - start)