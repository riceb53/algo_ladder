

# Write a function that returns whether a given number is a prime number.

# def prime(num):
#     starting_index = num // 2
#     while starting_index > 1:                  
#         val = num / starting_index
#         if isinstance(val, float) and val.is_integer():
#            return False
#         starting_index -= 1
#     return True 
        



# print(prime(211) == True)
# print(prime(51) == False)

# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".


# def fizzbuzz(num):
#     for i in range(1, num + 1):
#         if i % 15 == 0:
#             print("FIZZBUZZ")
#         elif i % 5 == 0:
#             print("BUZZ")
#         elif i % 3 == 0:
#             print("FIZZ")
#         else:
#             print(i)

# fizzbuzz(50)



# Write a function that gives the Nth number of the Fibonacci Sequence. The Fibonacci sequence begins with 0 and 1, and every number thereafter is the sum of the previous two numbers. So the sequence goes like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on until infinity...

# Input: 9
# Output: 21 (as this is the 9th number of the Fibonacci Sequence)

# Activity

# def fib_iterative(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])    
#     return fib_sequence[-1]

# print(fib_iterative(9) == 21)

# def fib_recursive(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib_recursive(n - 1) + fib_recursive(n - 2)
    
# print(fib_recursive(9))


# Given a year, report if it is a leap year.

# The tricky thing here is that a leap year in the Gregorian calendar occurs:

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
# For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

# If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.


# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True            
#             return False            
#         return True
#     return False



# print(is_leap_year(1997) == False)
# print(is_leap_year(1996) == True)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# def sum_of_multiples(n):
#     calculated_sum = 0
#     for i in range(1,n):
#         if i % 3 == 0 or i % 5 == 0:
#            calculated_sum += i
#     return calculated_sum 



# print(sum_of_multiples(10) == 23)
# print(sum_of_multiples(1000) == 233168)



# The Collatz Conjecture or 3x+1 problem can be summarized as follows:

# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

# Given a number n, return the number of steps required to reach 1.

# Examples
# Starting with n = 12, the steps would be as follows:

# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Resulting in 9 steps. So for input n = 12, the return value would be 9.

# def collatz(n):
#     i = 0
#     while True:
#         if n == 1:
#             return i
#         if n % 2 == 0:
#             n /= 2
#         else:
#             n = (3 * n) + 1
#         i += 1


# print(collatz(12) == 9)

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# def largest_palindrome(digits):
#     max_num = (10 ** digits) - 1
#     max_num_2 = max_num
#     largest_palindrome = 0
#     while max_num > 0:
#         while max_num_2 > 0:
#             product = max_num * max_num_2
#             product_str = str(product)
#             if product_str == product_str[::-1]:
#                 if product > largest_palindrome:
#                     largest_palindrome = product 
#             max_num_2 -= 1
#         max_num_2 = (10 ** digits) - 1
#         max_num -= 1
#     return largest_palindrome

# print(largest_palindrome(3) == 906609)