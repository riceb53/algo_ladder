# Write a function that returns the sum of all numbers in a given array.

# NOTE: Do not use any built-in language functions that do this automatically for you.

# Input: [1, 2, 3, 4]
# Output: 10

# Explanation: (1 + 2 + 3 + 4) = 10

# def reduce_sum(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# print(reduce_sum([1,2,3,4]))


# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]


# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

# def less_than_100(nums):
#     under_100 = []
#     for num in nums:
#         if num < 100:
#             under_100.append(num)
#     return under_100

# print(less_than_100([99, 101, 88, 4, 2000, 50]) == [99, 88, 4, 50])

# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

# def doubled(nums):
#     i = 0
#     for i in range(len(nums)):
#         nums[i] *= 2
#         i += 1
#     return nums

# print(doubled([4, 2, 5, 99, -4]) == [8, 4, 10, 198, -8])

# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20


# def greatest(nums):
#     largest_so_far = nums[0]
#     for num in nums:
#         if num > largest_so_far:
#             largest_so_far = num
#     return largest_so_far

# print(greatest([5, 17, -4, 20, 12]) == 20)


# Write a function that accepts an array of numbers and returns the product of all the numbers.

# Input: [1, 2, 3, 4]
# Output: 24

# Explanation: (1 x 2 x 3 x 4) = 24
# def reduce_product(nums):
#     product = 1
#     for num in nums:
#         product *= num
#     return product

# print(reduce_product([1,2,3,4]) == 24)

# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# def reverse(nums):
#     reversed_list = []
#     for num in reversed(nums):
#         reversed_list.append(num)
#     return reversed_list


# print(reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])

# Given an array of numbers, write a function that returns a new array in which only select numbers from the original array are included, based on the following details:

# The new array should always start with the first number from the original array. The next number that should be included depends on what the first number is. The first number dictates how many spaces to the right the computer should move to pick the next number. For example, if the first number is 2, then the next number that the computer should select would be two spaces to the right. This number gets added to the new array. If this next number happens to be a 4, then the next number after that is the one four spaces to the right. And so on and so forth until the end of the array is reached.

# Input:
# [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]

# Output:
# [2, 3, 1, 2, 2, 1, 5, 2, 2]


# def new_array_maker(nums):
#     i = 0
#     new_array = []
#     while i < len(nums):
#         new_array.append(nums[i])
#         i += nums[i]
#     return new_array
    

# print(new_array_maker([2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]) == [2, 3, 1, 2, 2, 1, 5, 2, 2])

