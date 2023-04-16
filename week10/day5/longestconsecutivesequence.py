# For this problem, we will look at space complexity as well as time complexity.
# Problem Statement

# Given an unsorted list of integers, find the length of the longest consecutive number sequence that could be constructed from numbers in the list.

# def longest_sequence(nums: list) -> int:
#     # <your code here>
# Notes:

# The list is of arbitrary length.
# The list is unsorted.
# The list may contain both positive and negative integers.
# There may be duplicated numbers.
# Example

# Input: [6, 4, 100, 5, 200, 2, 3]
# Explanation: The longest consecutive elements sequence is [2, 3, 4, 5, 6]. (Giving a length of 5)
# Output: 5

def longest_sequence(nums: list) -> int:
    sorted_nums = sorted(nums)
    longest_len = 0
    current_len = 1
    
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i-1] + 1:
            current_len += 1
        elif sorted_nums[i] != sorted_nums[i-1]:
            longest_len = max(longest_len, current_len)
            current_len = 1
    
    return max(longest_len, current_len)

print(longest_sequence([6, 4, 100, 5, 7, 2, 3]))



def longest_sequence_gpt(nums: list) -> int:
    num_map = {}
    longest_len = 0
    
    for num in nums:
        num_map[num] = True
        
    for num in nums:
        if num_map.get(num-1, False):
            continue
            
        current_num = num
        current_len = 1
        
        while num_map.get(current_num+1, False):
            current_num += 1
            current_len += 1
            
        longest_len = max(longest_len, current_len)
    
    return longest_len
