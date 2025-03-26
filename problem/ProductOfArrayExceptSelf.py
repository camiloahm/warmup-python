import logging
from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class ProductOfArrayExceptSelf:

    def bruteProductOfArrayExceptSelf(self, nums: List[int]) -> List[int]:

        result = [int]
        for i in range(len(nums)):
            helper = 1
            for j in range(len(nums)):
                if i != j:
                    helper *= nums[j]
            result.append(helper)

        return result

    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        left = {}
        right = {}
        return None


if __name__ == '__main__':
    solution = ProductOfArrayExceptSelf()

    print(solution.bruteProductOfArrayExceptSelf([1, 2, 3, 4]))
    print(solution.bruteProductOfArrayExceptSelf([-1, 1, 0, -3, 3]))
    assert solution.bruteProductOfArrayExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.bruteProductOfArrayExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    #
    # logging.info(solution.productOfArrayExceptSelf([1, 2, 3, 4]))
    # logging.info(solution.productOfArrayExceptSelf([-1, 1, 0, -3, 3]))
    # assert solution.productOfArrayExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    # assert solution.productOfArrayExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
