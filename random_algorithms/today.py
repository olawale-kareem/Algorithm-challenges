# Task
# Mary is a famous shopkeeper who sells n items in her shop. She assigns each item a unique popularity rating in the inclusive range from 1 to n.

# The shop only has one shelf, so the items are displayed array-style in a single row spanning from left to right in a random order. She wants to rearrange the items on the shelf by decreasing popularity rating such that the rating for the i item is always greater than the popularity rating of the (i + 1) item. Mary can swap any two items, i and j, in a single operation.

# Specification
# minimum_swaps(ratings)
# Parameters
# ratings: Array (of Integers) - an array of numbers indicating the popularity rating of each item on the shelf.

# Return Value
# Integer - denotes the minimum number of swap operations Mary must perform to order all n items by decreasing popularity rating.

# Constraints
# n = number of items in ratings array

# each rating value (arri) will be unique

# 1 ≤ n ≤ 2 × 105

# 1 ≤ arri ≤ n

# Examples
# ratings	Return Value
# Example #1	[3,1,2]	1
# Example #2	[3,1,2,4]	2
# Explanation for Example #1
# Mary can perform the following minimal sequence of swap operations to successfully sort all 3 items by decreasing popularity rating: [3, 1, 2] → [3, 2, 1].

# Thus, we return 1 as our answer.

# Explanation for Example #2
# Mary can perform the following minimal sequence of swap operations to successfully sort all 4 items by decreasing popularity rating: [3, 1, 2, 4] → [3, 4, 2, 1] → [4, 3, 2, 1].

# Thus, we return 2 as our answer.





##  Test

# import unittest
# from solution import minimum_swaps

# class TestMinimumSwaps(unittest.TestCase):
#     def test_should_handle_single_swap(self):
#         """ should handle single swap """
#         self.assertEqual(minimum_swaps([3, 1, 2]), 1)

#     def test_should_handle_multiple_swaps(self):
#         """ should handle multiple swaps """
#         self.assertEqual(minimum_swaps([3, 1, 2, 4]), 2)



##
# make an array from the idx of the last ele

def minimum_swaps(ratings: list) -> int:
    if len(ratings) == 1:
        return len(ratings)
    else:
        old_list = ratings
        last_ele = ratings[-1]
        prev_idx = old_list.index(last_ele)
        new_list = sorted(ratings)[::-1]
        now_idx = new_list.index(last_ele)


    if now_idx == 0:
        return abs(prev_idx - 1)
    return abs( prev_idx - now_idx)

   # use the idx and create a list
   # get the difference of the two list




   
    

n =[3, 1, 2]   
p = [3, 1, 2, 4]

print(minimum_swaps(n))
print(minimum_swaps(p))


# def minimum_swaps(ratings: list) -> int:
#        old_list = ratings
#    last_ele = ratings[-1]
#    prev_idx = old_list.index(last_ele)
#    new_list = sorted(ratings)[::-1]
#    now_idx = new_list.index(last_ele)

#    prev_pos = [None for i in range(prev_idx)]
#    if now_idx == 0:
#        now_idx = 1
#    new_pos = [None for i in range(now_idx)]

#    return(len(prev_pos)-len(new_pos))