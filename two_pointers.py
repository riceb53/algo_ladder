# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

# def combinations(chars1, chars2):
#     all_combinations = []
#     for char1 in chars1:
#         for char2 in chars2:
#             all_combinations.append(char1 + char2)
#     return all_combinations
            


# print(combinations(["a", "b", "c"], ["d", "e", "f", "g"]) == ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"])


# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

# def combinations2(chars):
#     all_combinations = []
#     for i in range(len(chars)):        
#         for j in range(len(chars)):
#             if i != j:
#                 all_combinations.append(chars[i] + chars[j])
#     return all_combinations


# print(combinations2(["a", "b", "c", "d"]) == ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"])


# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)


# def largest_product(nums):
#     largest_product_so_far = nums[0] * nums[1]
#     for i in range(len(nums)):
#         for j in range(len(nums)):            
#             product =  nums[i] * nums[j]
#             if i != j and product > largest_product_so_far:
#                 largest_product_so_far = product    
#     return largest_product_so_far



# print(largest_product([5, -2, 1, -9, -7, 2, 6]) == 63)

# def largest_product_efficient(nums):
#     max1 = float('-inf')
#     max2 = float('-inf')
#     min1 = float('inf')
#     min2 = float('inf')

#     for num in nums:
#         if num > max1:
#             max2 = max1
#             max1 = num
#         elif num > max2:
#             max2 = num
        
#         if num < min1:
#             min2 = min1
#             min1 = num
#         elif num < min2:
#             min2 = num

#     return max(min1 * min2, max1 * max2)
# print(largest_product_efficient([5, -2, 1, -9, -7, 2, 6]) == 63)


# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# def sum_to_ten(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j and nums[i] + nums[j] == 10:
#                 return [nums[i], nums[j]]            
#     return False           
        



# print(sum_to_ten([2, 5, 3, 1, 0, 7, 11]) == [3, 7])
# print(sum_to_ten([1, 2, 3, 4, 5]) == False)

# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]

# def merge_sorted_lists(nums1, nums2):
#     i = 0
#     j = 0
#     final = []
#     while i < len(nums1):
#         while j < len(nums2):
#             # pdb.set_trace()
#             if nums1[i] < nums2[j]:
#                 final.append(nums1[i])
#                 i += 1
#                 break
#             else:
#                 final.append(nums2[j])
#                 j += 1
#     final.extend(nums1[i:])
#     final.extend(nums2[j:])    
#     return final
# print(merge_sorted_lists([1, 5, 8], [6, 9]) == [1, 5, 6, 8, 9])


# Given an array of numbers, return true if the array is a "100 Coolio Array", or false if it is not.

# A "100 Coolio Array" meets the following criteria:

# Its first and last numbers add up to 100,
# Its second and second-to-last numbers add up to 100,
# Its third and third-to-last numbers add up to 100,
# and so on and so forth.

# Here are examples of 100 Coolio Arrays:

# [1, 2, 3, 97, 98, 99]
# [90, 20, 70, 100, 30, 80, 10]

# def coolio_100(nums):
#     i = 0
#     j = len(nums) - 1
#     while i <= j:        
#         if nums[i] + nums[j] != 100:
#             if i == j and nums[i] == 100:
#                 pass
#             else:
#                 return False
#         i += 1
#         j -= 1
#     return True

# print(coolio_100([1, 2, 3, 97, 98, 99]) == True)
# print(coolio_100([90, 20, 70, 100, 30, 80, 10]) == True)




# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

# def common_prefix(words):
#     first_word = words[0]
#     common_prefix = ""
#     for i in range(len(first_word)):
#         for word in words:
#             if word[i] != first_word[i]:
#                 return common_prefix
#         common_prefix += first_word[i]
#     return common_prefix

#     # check to make sure string is long enough
    


# print(common_prefix(["flower","flow","flight"]) == "fl")
# print(common_prefix(["dog","racecar","car"]) == "")