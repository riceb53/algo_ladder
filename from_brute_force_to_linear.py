# Given two arrays, return a new array that contains the intersection of the two arrays. The intersection means the values that are contained in both of the arrays. Do not use the "&", or any built-in intersection methods.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5], [1, 3, 5, 7, 9]
# Output: [1, 3, 5]


# def intersection(nums1, nums2):
#     common_numbers = []
#     nums1_dict = {}
#     # loop through make dict for nums1
#     for num in nums1:
#         nums1_dict[num] = True
#     # loop through nums2 check if value is in dict, if it is, add to list
#     for num in nums2:
#         if num in nums1_dict:
#             common_numbers.append(num)
#     return common_numbers

# print(intersection([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]) == [1, 3, 5])


# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all the values in one array are contained within the other.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false

# def subset(nums1, nums2):
#     # make 2 dicts?
#     nums1_dict = {}
#     nums2_dict = {}
#     for num1 in nums1:
#         nums1_dict[num1] = True
    
#     for num2 in nums2:
#         nums2_dict[num2] = True
    
#     num1_subset_of_nums2 = True
#     for num1 in nums1:
#         if num1 not in nums2_dict:
#             num1_subset_of_nums2 = False

#     num2_subset_of_nums1 = True
#     for num2 in nums2:
#         if num2 not in nums1_dict:
#             num2_subset_of_nums1 = False
    
#     return num2_subset_of_nums1 or num1_subset_of_nums2

    
# print(subset([1, 2, 3, 4, 5, 6], [6, 3, 2]) == True)
# print(subset([1, 2, 3, 4, 5, 6], [6, 3, 7]) == False)


# A given array has one pair of duplicate values. Return the first duplicate value.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [5, 2, 9, 7, 2, 6]
# Output: 2

# def duplicates(list):
#     dict = {}
#     for element in list:
#         if element in dict:
#             return element
#         else:
#             dict[element] = True    


# print(duplicates([5, 2, 9, 7, 2, 6]) == 2)

# A given string contains all the letters from the alphabet except for one. Return the missing letter.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: “The quick brown box jumps over a lazy dog”
# Output: “f”

# def all_letters_but_one(string):
#     all_letters = {
#         'a': True,
#         'b': True,
#         'c': True,
#         'd': True,
#         'e': True,
#         'f': True,
#         'g': True,
#         'h': True,
#         'i': True,
#         'j': True,
#         'k': True,
#         'l': True,
#         'm': True,
#         'n': True,
#         'o': True,
#         'p': True,
#         'q': True,
#         'r': True,
#         's': True,
#         't': True,
#         'u': True,
#         'v': True,
#         'w': True,
#         'x': True,
#         'y': True,
#         'z': True,
#     }
#     for char in string:
#         if char != ' ' and char in all_letters:
#             all_letters.pop(char.lower())
    
#     # print(next(iter(all_letters)))
#     return next(iter(all_letters))


# print(all_letters_but_one("The quick brown box jumps over a lazy dog") == 'f')

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Examples:

# s = "leetcode"
# return 0.
# (The "l" is the first character that only appears once in the string, and appears at index 0.)

# s = "loveleetcode",
# return 2.
# (The "l" and "o" are repeated, so the first non-repeating character is the "v", which is at index 2.)

# Note: You may assume the string contain only lowercase letters.

# do char counts
# loop through list again and find the first one with count of 1
# def first_non_repeating(string):
#     char_counts = {}
#     for char in string:
#         char_counts[char] = char_counts.get(char, 0) + 1
    
#     for i, char in enumerate(string):
#         if char_counts[char] == 1:
#             return i


# print(first_non_repeating("leetcode") == 0)
# print(first_non_repeating("loveleetcode") == 2)


# This is the same exercise as Two Sum I, but you must now solve it in linear time.

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# this doesn't deal with putting them in the correct order
# def two_sum(nums):
#     previous_numbers = {}
#     for num in nums:
#         target = 10 - num
#         if target in previous_numbers:
#             print(num, target)
#             return [target, num]
#         else:
#             previous_numbers[num] = True
#     return False
    
# print(two_sum([2, 5, 3, 1, 0, 7, 11]) == [3, 7])
# print(two_sum([1, 2, 3, 4, 5]) == False)

#  This is very similar to ETL #3, but you must now accomplish the task in linear time (O(N)).

# Given an array of Youtube videos, for example:

# [
# {title: 'How to Make Wood', author_id: 4, views: 6},
# {title: 'How to Seem Perfect', author_id: 4, views: 111},
# {title: 'Review of the New "Unbreakable Mug"', author_id: 2, views: 202},
# {title: 'Why Pigs Stink', author_id: 1, views: 12}
# ]

# and an array of authors, for example:

# [
# {id: 1, first_name: 'Jazz', last_name: 'Callahan'},
# {id: 2, first_name: 'Ichabod', last_name: 'Loadbearer'},
# {id: 3, first_name: 'Saron', last_name: 'Kim'},
# {id: 4, first_name: 'Teena', last_name: 'Burgess'},
# ]

# Return a new array of videos in the following format, and only include videos that have at least 100 views:

# [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, author_name: 'Ichabod Loadbearer' },
# ]

# def etl3(videos, users):
#     users_dict = {}
#     filtered_videos = []
#     for user in users:
#         users_dict[user["id"]] = user['first_name'] + " " + user['last_name']
    
#     for video in videos:
#         if video['views'] > 100:
#             new_video = {}
#             new_video['author_name'] = users_dict[video['author_id']]
#             new_video['views'] = video['views']
#             new_video['title'] = video['title']
#             filtered_videos.append(new_video)    
#     return filtered_videos




# print(etl3([
# {"title": 'How to Make Wood', "author_id": 4, "views": 6},
# {"title": 'How to Seem Perfect', "author_id": 4, "views": 111},
# {"title": 'Review of the New "Unbreakable Mug"', "author_id": 2, "views": 202},
# {"title": 'Why Pigs Stink', "author_id": 1, "views": 12}
# ], [
# {"id": 1, "first_name": 'Jazz', "last_name": 'Callahan'},
# {"id": 2, "first_name": 'Ichabod', "last_name": 'Loadbearer'},
# {"id": 3, "first_name": 'Saron', "last_name": 'Kim'},
# {"id": 4, "first_name": 'Teena', "last_name": 'Burgess'},
# ]) == [
# {"title": 'How to Seem Perfect', "views": 111, "author_name": 'Teena Burgess' },
# {"title": 'Review of the New "Unbreakable Mug"', "views": 202, "author_name": 'Ichabod Loadbearer' },
# ])