# Practice using Python's floor operator //
# Goal: Count the number of digits in a given number
# https://docs.python.org/3/library/functions.html


def countDigits(num):
    num = abs(num)
    digitCount = 0
    while num != 0:
        num //= 10
        digitCount += 1
    return digitCount

n1 = int(input("Number? "))

print(f"There are {countDigits(n1)} numbers in {n1}")