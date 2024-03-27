# # Given a string, find the most commonly occurring letter.

# # Input: “peter piper picked a peck of pickled peppers”
# # Output: “p”

# def most_common_letter(string):
#     char_counts = {}
#     for char in string:
#         if char == " ":
#             continue
#         else:
#             if char in char_counts:
#                 char_counts[char] += 1
#             else:
#                 char_counts[char] = 1    
#     return max(char_counts, key=char_counts.get)


# print(most_common_letter("peter piper picked a peck of pickled peppers") == "p")


# # Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# # Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# # Output: {"Dewey" => 6, "Truman" => 5}

# # Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

# def string_counter(strings):
#     string_counts = {}
#     for string in strings:
#         if string in string_counts:
#             string_counts[string] += 1
#         else:
#             string_counts[string] = 1
#     return string_counts


# print(string_counter(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]) == {"Dewey": 6, "Truman": 5})



# # Given a hash, where the keys are strings representing food items, and the values are numbers representing the price of each food, return the amount someone would pay if they'd order one of each food from the entire menu.

# # Input: {"hot dog" => 2, "hamburger" => 3, "steak sandwich" => 5, "fries" => 1, "cole slaw" => 1, "soda" => 2}

# # Output: 14
# # Explanation: If someone would order one of everything on the menu, they'd pay a total of 14 (the sum of all the hash's values).

# def food_cost(food_dict):
#     cost = 0
#     for key in food_dict:
#         cost += food_dict[key]
#     return cost

# print(food_cost({"hot dog": 2, "hamburger": 3, "steak sandwich": 5, "fries": 1, "cole slaw": 1, "soda": 2}) == 14)




# Given an array of hashes that represent a list of social media posts, return a new array that only contains the posts that have at least 1000 likes.

# Input: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

# Output: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# ]
# def popular_posts(posts):
#     filtered_posts = []
#     for post in posts:        
#         if post["likes"] > 1000:
#             filtered_posts.append(post)
#     return filtered_posts

# print(popular_posts([{"title": 'Me Eating Pizza', "submitted_by": "Joelle P.", "likes": 1549},{"title": 'i never knew how cool i was until now', "submitted_by": "Lyndon Johnson", "likes": 3},{"title": 'best selfie evar!!!', "submitted_by": "Patti Q.", "likes": 1092},{"title": 'Mondays are the worst', "submitted_by": "Aunty Em", "likes": 644}]) == [
#     {"title": 'Me Eating Pizza', "submitted_by": "Joelle P.", "likes": 1549},
#     {"title": 'best selfie evar!!!', "submitted_by": "Patti Q.", "likes": 1092},
# ])

# Given a DNA strand, return its RNA complement (per RNA transcription).

# Both DNA and RNA strands are a sequence of nucleotides. Here we're representing the sequences with single-letter characters (e.g. a sample strand may look like: "AGCA".)

# Given a string representing a DNA strand, provide its transcribed RNA strand, according to the following pattern:

# G becomes C
# C becomes G
# T becomes A
# A becomes U

# So based on all this, here's a sample input/output:

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'

# def dna_to_rna(dna_strand):
#     conversion = {
#         "G": "C",
#         "C": "G",
#         "T": "A",
#         "A": "U"
#     }
#     rna_strand = ""
#     for char in dna_strand:
#         rna_strand += conversion[char]
#     return rna_strand


# print(dna_to_rna('ACGTGGTCTTAA') == 'UGCACCAGAAUU')




# Given an array of social media posts and a hash of users, return a list of posts (as an array of hashes) that replaces the submitted_by id number as the person's actual name.

# For example, given this array of posts (note that the submitted_by is an id number):

# [
# {title: 'Me Eating Pizza', submitted_by: 231, likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: 989, likes: 3},
# {title: 'best selfie evar!!!', submitted_by: 111, likes: 1092},
# {title: 'Mondays are the worst', submitted_by: 403, likes: 644}
# ]

# And this hash of users (the key is the id number and the value is the user's real name):

# users = {403 => "Aunty Em", 231 => "Joelle P.", 989 => "Lyndon Johnson", 111 => "Patti Q."}

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]
# def add_author(posts, users):
#     for i in range(len(posts)):
#         posts[i]["submitted_by"] = users[posts[i]["submitted_by"]]    
#     return posts
        

# print(add_author([
# {"title": 'Me Eating Pizza', "submitted_by": 231, "likes": 1549},
# {"title": 'i never knew how cool i was until now', "submitted_by": 989, "likes": 3},
# {"title": 'best selfie evar!!!', "submitted_by": 111, "likes": 1092},
# {"title": 'Mondays are the worst', "submitted_by": 403, "likes": 644}
# ],  {403: "Aunty Em", 231: "Joelle P.", 989: "Lyndon Johnson", 111: "Patti Q."}) == [
# {"title": 'Me Eating Pizza', "submitted_by": "Joelle P.", "likes": 1549},
# {"title": 'i never knew how cool i was until now', "submitted_by": "Lyndon Johnson", "likes": 3},
# {"title": 'best selfie evar!!!', "submitted_by": "Patti Q.", "likes": 1092},
# {"title": 'Mondays are the worst', "submitted_by": "Aunty Em", "likes": 644}
# ])


# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false


# def anagram_checker(word1, word2):
#     word1_dict = {}
#     word2_dict = {}
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] in word1_dict:
#             word1_dict[word1[i]] += 1
#         else:
#             word1_dict[word1[i]] = 1

#         if word2[i] in word2_dict:
#             word2_dict[word2[i]] += 1
#         else:
#             word2_dict[word2[i]] = 1
#     return word1_dict == word2_dict


# print(anagram_checker("silent", "listen") == True)
# print(anagram_checker("frog", "bear") == False)