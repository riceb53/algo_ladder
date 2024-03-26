# Write a function that returns the reverse of a given string.

# Input: “abcde”
# Output: “edcba”

# def reverse_string(string):
#     string_reversed = ""
#     for char in reversed(string):
#         string_reversed += char
#     return string_reversed


# print(reverse_string("abcde") == "edcba")

# Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.

# Input: “i hate $ but i love money i know i know im crazy”
# Output: true

# Input: “abcdefghijklmnopqrstuvwxyz”
# Output: false

# def find_dollar(string):
#     for char in string:
#         if char == "$":
#             return True
#     return False

# print(find_dollar("abcdefghijklmnopqrstuvwxyz") == False)

# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

# def alternate_capitals(string):
#     new_string = ""
#     for i in range(len(string)):
#         if i % 2 == 0:
#             new_string += string[i]
#         else:
#             new_string += string[i].upper()    
#     return new_string

# print(alternate_capitals("hello, how are your porcupines today?") == "hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?")

# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

# def duplicate(string):
#     chars_dict = {}
#     for char in string:
#         if char in chars_dict:
#             return char
#         else:
#             chars_dict[char] = True

# print(duplicate("abcdefghhijkkloooop") == "h")

# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

# def palindrome(string):
#     i = 0
#     j = len(string) - 1
#     while i <= j:        
#         if string[i] != string[j]:
#             return False
#         i += 1
#         j -= 1
#     return True


# print(palindrome("racecar") == True)
# print(palindrome("baloney") == False)


# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.

# Input: "ABCDEFG", "ABCXEOG"
# Output: 2

# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different (the D and F in the first string), we return 2.

# Input: "ABCDEFG", "ABCDEFG",
# Output: 0

# def different_strings(string1, string2):
#     difference_count = 0
#     for i in range(len(string1)):
#         if string1[i] != string2[i]:
#             difference_count += 1
#     return difference_count
        


# print(different_strings("ABCDEFG", "ABCDEFG") == 0)

# # Given a string of words, write a function that returns a new string that contains the words in reverse order.

# # Input: “popcorn is so cool isn’t it yeah i thought so”
# # Output: “so thought i yeah it isn’t cool so is popcorn”

# def reverse_sentence(string):
#     words = string.split()
#     reversed_words = ""
#     for word in reversed(words):
#         reversed_words += (word + " ")    
#     return reversed_words[:-1]

# print(reverse_sentence("popcorn is so cool isn’t it yeah i thought so") == "so thought i yeah it isn’t cool so is popcorn")

