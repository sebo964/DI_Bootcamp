def subsetsum(numbers: list, target: int) -> bool:
    sorted_list = sorted(numbers)
    for i in range(len(sorted_list)):
        X = sorted_list[i]
        for j in range(i+1, len(sorted_list)):
            Y = sorted_list[j]
            if X + Y == target:
                print (sorted_list)
                print("True")
                return True

    print(sorted_list)
    print("False")
    return False

# Given a list of numbers and a target, write a function to determine if the target can be calculated by summing together any 2 numbers in the list.
# The function should return True if the target can be calculated and False if not.

# For ease of analysis and to see whats going on, we will also print True and the 2 numbers, or False.
# def subsetsum(numbers: list, target: int) -> bool:
#     # <your code here>
# Notes:

# The list is of arbitrary length.
# The list is unsorted.
# The list may contain both positive and negative integers.
# There may be duplicated numbers.
# Example Outputs

nums = [12, -7, 20, 1, 4, -10, -1]


subsetsum(nums, 1) # True, 1 and 4



# chat gpt refactored code 

def subsetsum1(numbers: list, target: int) -> bool:
    sorted_list = sorted(numbers)
    left, right = 0, len(sorted_list) - 1
    while left < right:
        curr_sum = sorted_list[left] + sorted_list[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False

print (subsetsum1(nums, 10))
